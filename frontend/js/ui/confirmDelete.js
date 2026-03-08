export function attachDeleteConfirmation(container, formClass = "delete-form", entityName = "registro") {
    if (!container) return;

    container.addEventListener("submit", function (e) {
        
        // FORM
        const form = e.target;
        if (!form.classList.contains(formClass)) return;

        // DETENER SUBMIT
        e.preventDefault();

        // ALERTA
        Swal.fire({
            title: `¿Eliminar ${entityName}?`,
            text: "Esta acción no se puede deshacer",
            icon: "warning",
            showCancelButton: true,
            confirmButtonText: "Sí, eliminar",
            cancelButtonText: "Cancelar",
            reverseButtons: true,
        }).then(result => {
            if (result.isConfirmed) {
                form.submit();
            }
        });
    })
}