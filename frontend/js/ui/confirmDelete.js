import { confirmAction } from "./alert.js";

export function attachDeleteConfirmation(container, formClass = "delete-form", entityName = "registro") {
    if (!container) return;

    container.addEventListener("submit", async function (e) {

        // FORM
        const form = e.target;
        if (!form.classList.contains(formClass)) return;

        // DETENER SUBMIT
        e.preventDefault();

        // ALERTA
        const confirmed = await confirmAction({
            title: `¿Eliminar ${entityName}?`,
            confirmText: "Sí, eliminar"
        });

        if (confirmed) {
            form.submit();
        }
    })
}