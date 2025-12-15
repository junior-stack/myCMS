# hooks.py
import re
from textwrap import dedent
import urllib.parse
from mkdocs.plugins import BasePlugin

x_intent = "https://x.com/intent/tweet"
fb_sharer = "https://www.facebook.com/sharer/sharer.php"

# Pattern to match ```lang group:groupName ... ```
CODE_BLOCK_PATTERN = re.compile(
    r"```(\w+)\s+([^\n]+)\n(.*?)```",
    re.DOTALL
)

CALLOUT_PATTERN = re.compile(r"> \[!(\w+)\]([+|-])?([^\n]+)?\n>(.*?)\n[^>]", re.DOTALL)


HEADER_PATTERN = re.compile(r'^(#+)', re.MULTILINE)

BULLET_PATTERN = re.compile(r":\n([1-])", re.DOTALL)

PICTURE_PATTERN = re.compile(r"!\[\[(.*?)\]\]", re.DOTALL)

TABS_PATTERN = re.compile(r"~~~tabs\s*(.*?)~~~", re.DOTALL)

TAB_PATTERN = r"---\s*tab\s*"


def transform_group_tabs(content: str) -> str:
    """
    Convert Obsidian Codeblock Customizer syntax:
    ```python group:foo
    ...
    ```
    into MkDocs Material tabs syntax:
    === "Python"
    ```python
    ...
    ```
    """
    FILE_PATTERN =r"file:([^\s]+)"
    def repl(match):
        lang = match.group(1).strip()
        flags = match.group(2).strip()
        code = match.group(3)
        tab_title = lang
        if "group:" in flags:
            code = "\n".join("\t" + line for line in code.splitlines())
            tab_title = lang
            if "file:" in flags:
                tab_title = re.search(FILE_PATTERN, flags).group(1)
            return f'=== "{tab_title}"\n\t```{lang}\n{code}\n\t```\n'
        elif "file:" in flags:
            title = re.search(FILE_PATTERN, flags).group(1)
            return f'```{lang} title="{title}"\n{code}\n\t```\n'
        elif "fold" in flags:
            return f'```{lang}\n{code}\n```\n'
        else:
            return match.group(0)  # no change

    return CODE_BLOCK_PATTERN.sub(repl, content)


def increase_header_level(content: str) -> str:
    """
    Adds one more '#' to each Markdown header line.
    '# H1' -> '## H2', etc.
    """
    def repl(match):
        hashes = match.group(1)
        return '#' + hashes  # add one more '#'
    return HEADER_PATTERN.sub(repl, content)

def convert_tabs_block(content: str) -> str:
    def replace_block(match):
        block = match.group(1)
        tabs = re.split(TAB_PATTERN, block)
        converted = []
        for tab in tabs:
            tab = tab.strip()
            if not tab:
                continue
            lines = tab.split("\n", 1)
            if not lines:
                continue
            title = lines[0].strip()
            content = lines[1].rstrip() if len(lines) > 1 else ""
            indented = "\n\t" + content.replace("\n", "\n\t")
            converted.append(f'=== "{title}"{indented}')
        return "\n".join(converted)
    return TABS_PATTERN.sub(replace_block, content)


def transform_Bullet_start(content: str) -> str:
    return BULLET_PATTERN.sub(r":\n\n\1", content)

def parse_picture(content: str) -> str:
    def repl(match):
        pic = match.group(1)
        return f"![](../images/{pic})"
    return PICTURE_PATTERN.sub(repl, content)

def parse_callouts(content: str) -> str:
    def repl(match):
        callout_type = match.group(1).lower()
        isCollapsed = match.group(2)
        title = match.group(3)
        calloutcontent = match.group(4).strip()
        
        calloutheader = f"???+ {callout_type} "
        if isCollapsed == "-":
            calloutheader = f"??? {callout_type} "
        if title:
            calloutheader += f'"{title.strip()}"'
        return calloutheader + "\n\t" + calloutcontent.replace("\n>", "\n\t") + "\n"
        
    return CALLOUT_PATTERN.sub(repl, content)

def transform(content: str) -> str:
    content = transform_Bullet_start(content)
    content = parse_callouts(content)
    content = convert_tabs_block(content)
    content = transform_group_tabs(content)
    content = increase_header_level(content)
    content = parse_picture(content)
    return content

def on_page_markdown(markdown, page, config, files):
    # Runs on each page before conversion to HTML
    if not page.file.src_uri.startswith("posts/"):
        return markdown
    
    page_url = config.site_url + page.url
    page_title = urllib.parse.quote(page.title+'\n')
    
    return transform(markdown) + dedent(f"""
    <div style="text-align: center; margin-top: 20px;">
    <h2>Share this post:</h2>
    </div>
    [Share on :simple-x:]({x_intent}?text={page_title}&url={page_url}){{ .md-button }}
    [Share on :simple-facebook:]({fb_sharer}?u={page_url}){{ .md-button }}
    """)

# if __name__ == "__main__":
#     file_path ="./docs/posts/exp.md"
#     with open(file_path, "r", encoding="utf-8") as f:
#         file_content = f.read()
#         my_string = parse_callouts(file_content)
#         print(my_string)
#         with open("my_file.md", "w", encoding="utf-8") as file_object:
#             # Write the string to the file
#             file_object.write(my_string)


        # pattern = r":\n-"
        # matches = re.findall(pattern, file_content, flags=re.DOTALL)
        # print("matches: ", matches)
        # for lang, groupName, content in matches:
        #     print("lange: ", lang)
        #     print("groupName: ", groupName)
        
    