export function attachDeleteConfirmation(container) {
    if (!container) return;

    container.addEventListener("submit", function (e) {
        const form = e.target;

        if (!form.classList.contains("student-delete-form")) return;

        e.preventDefault();

        Swal.fire({
            title: "¿Eliminar alumno?",
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
    });
}