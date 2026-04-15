// === CONTENEDOR ===
function createFlash(containerId, type, message, timeout = null) {
    const container = document.getElementById(containerId);
    if (!container) return;

    const alert = document.createElement("div");
    alert.className = `alert alert-${type} alert-dismissible fade show mb-2`;
    alert.innerHTML = `${message}<button type="button" class="btn-close" data-bs-dismiss="alert"></button>`;

    container.appendChild(alert);

    // AUTO-DELETE
    if (timeout) {
        setTimeout(() => {
            alert.classList.remove("show");
            alert.classList.add("fade");

            setTimeout(() => alert.remove(), 150);
        }, timeout);
    }
}


// NORMAL
export function showFlash(type, message) {
    createFlash("flash-container", type, message);
}

// FIXED
export function showFlashFixed(type, message) {
    createFlash("flash-container-fixed", type, message, 3000);
}