
document.addEventListener("DOMContentLoaded", () => {
    const textArea = document.getElementById("text");
    const charCount = document.getElementById("char-count");
    const clearButton = document.getElementById("clear-btn");
    const exampleButtons = document.querySelectorAll(".example");

    if (!textArea || !charCount || !clearButton) {
        console.error("Required elements were not found.");
        return;
    }

    function updateCharacterCount() {
        const count = textArea.value.length;
        charCount.textContent =
            `${count} character${count === 1 ? "" : "s"}`;
    }

    textArea.addEventListener("input", updateCharacterCount);

    clearButton.addEventListener("click", () => {
        textArea.value = "";
        updateCharacterCount();
        textArea.focus();
    });

    exampleButtons.forEach((button) => {
        button.addEventListener("click", () => {
            textArea.value = button.dataset.text || "";
            updateCharacterCount();
            textArea.focus();
        });
    });

    updateCharacterCount();
});
