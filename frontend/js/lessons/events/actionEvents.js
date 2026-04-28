import { showFlashFixed } from "../../ui/flash.js";
import { getLessons, getEditedLessons, getLessonsToDelete, getLessonsToChange } from "../state.js";
import { createLessons, updateLessons, deleteLessons, saveChanges } from "../api.js";


// =========================
// GUARDAR CLASES
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
            location.href = location.href;

        } catch (err) {
            showFlashFixed("danger", err.message);
        }
    })
}


// =========================
// ACTUALIZAR CLASES
// =========================

export function initUpdateLessons({ buttonId }) {
    const btn = document.getElementById(buttonId);
    if (!btn) return;

    btn.addEventListener("click", async () => {

        // === DATA ===
        const payload = getEditedLessons();
        const enrollmentId = btn.dataset.enrollmentId;

        // === FETCH ===
        try {
            const res = await updateLessons({
                enrollment_id: enrollmentId,
                lessons: payload,
            });

            // RECARGAR PÁGINA
            location.href = location.href;

        } catch (err) {
            showFlashFixed("danger", err.message);
        }
    })
}


// =========================
// ELIMINAR CLASES
// =========================

export function initBulkDeleteLessons({ buttonId }) {
    const btn = document.getElementById(buttonId);
    if (!btn) return;

    btn.addEventListener("click", async () => {

        // === DATA ===
        const lessons = getLessonsToDelete();

        if (!lessons.length) {
            showFlashFixed("warning", "Selecciona al menos una clase");
            return;
        }

        const enrollmentId = btn.dataset.enrollmentId;

        // === FETCH ===
        try {
            const res = await deleteLessons({
                enrollment_id: enrollmentId,
                lessons: lessons
            });

            // RECARGAR PÁGINA
            location.href = location.href;

        } catch (err) {
            showFlashFixed("danger", err.message);
        }
    });
}


// =========================
// CAMBIAR CLASES
// =========================

export function initSaveChanges({ buttonId }) {
    const btn = document.getElementById(buttonId);
    if (!btn) return;

    btn.addEventListener("click", async () => {

        // === DATA ===
        const data = getLessonsToChange();

        if (!data.length) {
            showFlashFixed("warning", "Realiza al menos un cambio");
            return;
        }

        // === FETCH ===
        try {
            const res = await saveChanges(data);

            // RECARGAR PÁGINA
            location.href = location.href;

        } catch (err) {
            showFlashFixed("danger", err.message);
        }
    });
}