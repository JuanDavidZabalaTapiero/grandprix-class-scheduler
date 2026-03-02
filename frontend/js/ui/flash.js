export function showFlash(type, message) {
    const container = document.getElementById("flash-container");

    if (!container) return;

    const alert = document.createElement("div");
    alert.className = `alert alert-${type} alert-dismissible fade show`;
    alert.innerHTML = `${message} <button type="button" class="btn-close" data-bs-dismiss="alert"></button>`;

    container.appendChild(alert);
}