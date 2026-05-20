export async function confirmAction({
  title = "¿Estás seguro?",
  text = "Esta acción no se puede deshacer",
  confirmText = "Sí, continuar",
  cancelText = "Cancelar",
  icon = "warning",
} = {}) {
  const result = await Swal.fire({
    title,
    text,
    icon,
    showCancelButton: true,
    confirmButtonText: confirmText,
    cancelButtonText: cancelText,
    reverseButtons: true,
  });

  return result.isConfirmed;
}
