import { toggleLesson, selectedLessons, getLessons } from "./state.js";
import { showFlashFixed } from "../ui/flash.js";
import { createLessons } from "./api.js";

// =========================
// CLASE (TD)
// =========================

export function handleLessonClick({ lessonTd, row, item }) {

    // === DATA ===
    const date = document.getElementById("date-input").value;
    const hour = row.hour;

    const instructorId = item.id;
    const select = document.getElementById(`select-${instructorId}`);

    const vehicleId = select.selectedOptions[0].dataset.vehicleId;

    const instructorVehicleId = select?.value;

    const lessonData = {
        date: date,
        hour: hour,
        instructor_id: instructorId,
        vehicle_id: vehicleId,
        instructor_vehicle_id: instructorVehicleId
    };

    // TOGGLE
    const result = toggleLesson(lessonData, row.vehicles_ids);

    // === UX ===

    // DUPLICADO
    if (result === "duplicate-db") {
        showFlashFixed("danger", "Ese vehículo ya está ocupado en ese horario");
        return;
    }

    if (result === "duplicate") {
        showFlashFixed("warning", "Ese vehículo ya está asignado en ese horario");
        return;
    }

    // NORMAL
    lessonTd.classList.toggle("selected", result);

    console.log(selectedLessons);
}

// =========================
// GUARDAR CLASES (BTN)
// =========================

export function initSaveLessons({ buttonId }) {
    const btn = document.getElementById(buttonId);

    if (!btn) return;

    btn.addEventListener("click", async () => {

        // === DATA ===
        const lessons = getLessons();

        if (!lessons.length) {
            showFlashFixed("warning", "Selecciona al menos una clase");
            return;
        }

        const enrollmentId = btn.dataset.enrollmentId;

        // === FETCH ===
        try {
            const res = await createLessons({
                enrollment_id: enrollmentId,
                lessons: lessons
            });

            // RECARGAR PÁGINA
            window.location.reload();

        } catch (err) {
            showFlashFixed("danger", err.message);
        }
    })
}