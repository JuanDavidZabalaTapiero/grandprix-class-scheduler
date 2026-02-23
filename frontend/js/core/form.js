export function attachLoadingOnSubmit(formId, options = {}) {
    const form = document.getElementById(formId);
    if (!form) return;

    const {
        buttonId,
        spinnerId,
        textId,
    } = options;

    form.addEventListener("submit", () => {
        const btn = document.getElementById(buttonId);
        const spinner = document.getElementById(spinnerId);
        const text = document.getElementById(textId);

        if (!btn || !spinner || !text) return;

        btn.disabled = true;
        spinner.classList.remove("d-none");
        text.classList.add("d-none")
    })
}