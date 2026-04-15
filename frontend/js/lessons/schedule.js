import { getSchedule } from "./api.js";
import { showFlash } from "../ui/flash.js";
import { renderSchedule } from "./ui.js";

// =========================
// CARGAR CLASES
// =========================

export async function loadSchedule(dateInput, container) {
    try {
        const data = await getSchedule(dateInput.value);
        renderSchedule(container, data, dateInput.value);
    } catch (err) {
        container.innerHTML = "";
        showFlash("danger", err.message);
    }
}

// =========================
// INICIALIZACIÓN
// =========================

export function initSchedule({ dateId, containerId }) {

    // === ELEMENTOS ===
    const date = document.getElementById(dateId);
    const container = document.getElementById(containerId);

    if (!date || !container) return;

    // === CARGA INICIAL ===
    loadSchedule(date, container);

    // === EVENTO CHANGE ===
    date.addEventListener("change", () => loadSchedule(date, container));
}