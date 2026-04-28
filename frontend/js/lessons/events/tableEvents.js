import { toggleLessonsToDelete, changeLesson } from "../state.js";

export function initLessonTableEvents() {
    document.addEventListener("change", (e) => {

        const target = e.target;

        // =========================
        // CHECKBOX DELETE
        // =========================
        if (target.matches(".lesson-checkbox")) {
            toggleLessonsToDelete(target);
            return;
        }

        // =========================
        // INPUTS (SELECT / CHECKBOX)
        // =========================
        if (target.matches(".lesson-input")) {
            changeLesson(target);
            return;
        }

    });
}