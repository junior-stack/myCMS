document.addEventListener("DOMContentLoaded", () => {
  const maxLines = 5; // 👈 number of visible lines before collapsing

  document.querySelectorAll("pre > code").forEach((codeBlock) => {
    const pre = codeBlock.parentNode;
    const lineCount = codeBlock.textContent.split("\n").length;

    if (lineCount > maxLines) {
      pre.classList.add("collapsible");
      pre.style.maxHeight = `${maxLines * 1.5}em`; // adjust line height factor

      // Create toggle button
      const button = document.createElement("button");
      button.className = "code-toggle";
      button.textContent = "Show more";

      button.addEventListener("click", () => {
        if (pre.classList.contains("expanded")) {
          pre.classList.remove("expanded");
          pre.style.maxHeight = `${maxLines * 1.5}em`;
          button.textContent = "Show more";
        } else {
          pre.classList.add("expanded");
          pre.style.maxHeight = pre.scrollHeight + "px";
          button.textContent = "Show less";
        }
      });

      // Insert after pre
      pre.parentNode.insertBefore(button, pre.nextSibling);
    }
  });
});
