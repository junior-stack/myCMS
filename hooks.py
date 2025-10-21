# hooks.py
import re
from mkdocs.plugins import BasePlugin

# Pattern to match ```lang group:groupName ... ```
GROUP_PATTERN = re.compile(
    r"```(\w+)\s+group:([^\n]+)\n(.*?)```",
    re.DOTALL
)

# FOLD_PATTERN = re.compile(r"(```\w+)(?:\s+group:[^\n]+)?\s+fold")
FOLD_PATTERN = re.compile(r"(```\w+)(\s+group:[^\n]+)?\s+fold")

HEADER_PATTERN = re.compile(r'^(#+)', re.MULTILINE)

BULLET_PATTERN = re.compile(r":\n-", re.DOTALL)

def remove_fold_flags(content: str) -> str:
    """
    Removes ' fold' from code block opening lines.
    Works with:
    ```python fold
    ```python group:foo fold
    """
    return FOLD_PATTERN.sub(r"\1\2", content)

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
    def repl(match):
        lang = match.group(1).strip()
        # group = match.group(2).strip()
        code = match.group(3)
        code = "\n".join("    " + line for line in code.splitlines())
        return f'=== "{lang}"\n    ```{lang}\n{code}\n    ```\n'

    return GROUP_PATTERN.sub(repl, content)


def increase_header_level(content: str) -> str:
    """
    Adds one more '#' to each Markdown header line.
    '# H1' -> '## H2', etc.
    """
    def repl(match):
        hashes = match.group(1)
        return '#' + hashes  # add one more '#'
    return HEADER_PATTERN.sub(repl, content)


def transform_Bullet_start(content: str) -> str:
    return BULLET_PATTERN.sub(r":\n\n-", content)

def on_page_markdown(markdown, page, config, files):
    # Runs on each page before conversion to HTML
    content = remove_fold_flags(markdown)
    content = transform_group_tabs(content)
    content = increase_header_level(content)
    content = transform_Bullet_start(content)
    return content

# if __name__ == "__main__":
#     file_path ="./docs/Algorithm.md"
#     with open(file_path, "r", encoding="utf-8") as f:
#         file_content = f.read()
#         my_string = remove_fold_flags(file_content)
#         my_string = transform_group_tabs(my_string)
#         with open("my_file.md", "w", encoding="utf-8") as file_object:
#             # Write the string to the file
#             file_object.write(my_string)


        # pattern = r":\n-"
        # matches = re.findall(pattern, file_content, flags=re.DOTALL)
        # print("matches: ", matches)
        # for lang, groupName, content in matches:
        #     print("lange: ", lang)
        #     print("groupName: ", groupName)
        
    