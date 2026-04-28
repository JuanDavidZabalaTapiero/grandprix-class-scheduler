import { getSchedule } from "./api.js";
import { showFlash } from "../ui/flash.js";
import { renderSchedule } from "./ui.js";
import { getScheduleRefs, setScheduleRefs } from "./scheduleRefs.js";


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
// RE-RENDER
// =========================

export function rerenderSchedule() {
    const { dateInput, container } = getScheduleRefs();
    if (!dateInput || !container) return;

    loadSchedule(dateInput, container);
}


// =========================
// INICIALIZACIÓN
// =========================

export function initSchedule({ dateId, containerId }) {

    // === ELEMENTOS ===
    const date = document.getElementById(dateId);
    const container = document.getElementById(containerId);

    if (!date || !container) return;

    // === GUARDAR REFS ===
    setScheduleRefs({ dateInput: date, container: container });

    // === CARGA INICIAL ===
    loadSchedule(date, container);

    // === EVENTO CHANGE ===
    date.addEventListener("change", () => loadSchedule(date, container));
}
