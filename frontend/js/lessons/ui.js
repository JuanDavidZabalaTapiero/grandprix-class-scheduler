import { selectedLessons, changeMode, lessonsToChange } from "./state.js";
import { handleLessonClick, handleRegisteredClick } from "./events/cellEvents.js";
import { applyLessonStyles } from "./styles.js";

export function renderSchedule(container, lessons, date, totals = {}) {
    if (!container) return;

    // LIMPIAR CONTENEDOR
    container.innerHTML = "";

    // RENDER
    lessons.forEach(row => {
        const tr = document.createElement("tr");

        // HORA
        const hourTd = document.createElement("td");
        hourTd.textContent = row.hour_formatted
        tr.appendChild(hourTd);

        // CLASES
        row.instructors.forEach(item => {
            const lessonTd = document.createElement("td");

            if (item.lesson) {

                // === CLASE OCUPADA ===

                // CONTENIDO
                lessonTd.textContent = `${item.lesson.student} (${item.lesson.category}) | ${item.lesson.vehicle_license} (${item.lesson.vehicle_type})`;

                // EVENTO
                lessonTd.addEventListener("click", () => { handleRegisteredClick({ lesson: item.lesson }) });


                // === CSS ===

                // NORMAL
                applyLessonStyles(lessonTd, item.lesson);

                // CHANGE MODE
                if (changeMode.active && changeMode.selection.origin && changeMode.selection.origin.id === item.lesson.id) {
                    lessonTd.classList.add("change-origin");
                }

                if (changeMode.active && changeMode.selection.target === item.lesson.id) {
                    lessonTd.classList.add("change-target");
                }

                // SELECTED IN CHANGE

                const isChosen = lessonsToChange.some(c => {
                    // ORIGIN
                    if (c.originId === item.lesson.id) return true;

                    // TARGET
                    if (c.target === item.lesson.id) return true;

                    return false;
                });

                if (isChosen) {
                    lessonTd.classList.add("change-chosen");
                }

            } else {

                // === CLASE DISPONIBLE ===

                // EVENTO
                lessonTd.addEventListener("click", () => { handleLessonClick({ lessonTd, row, item }) });

                // === CSS ===

                // VERIFICAR SELECCIÓN
                const hour = row.hour;
                const instructorId = item.id;
                const selected = selectedLessons.some(l => l.date === date && l.hour === hour && l.instructor_id === instructorId)

                if (selected) {
                    lessonTd.classList.add("selected");
                }

                // CHANGE MODE
                const target = changeMode.selection.target;

                if (changeMode.active && target && typeof target === "object" && target.date === date && target.hour === row.hour && target.instructor_id === item.id) {
                    lessonTd.classList.add("change-target");
                }

                // SELECTED TO CHANGE

                const isChosenTarget = lessonsToChange.some(c => {
                    const t = c.target;

                    return (
                        typeof t === "object" &&
                        t.date === date &&
                        t.hour === row.hour &&
                        t.instructor_id === item.id
                    );
                });

                if (isChosenTarget) {
                    lessonTd.classList.add("change-chosen");
                }
            }

            tr.appendChild(lessonTd);
        })

        container.appendChild(tr);
    })

    // =========================
    // FILA TOTAL
    // =========================

    const totalTr = document.createElement("tr");

    const totalLabelTd = document.createElement("td");
    totalLabelTd.textContent = "Total";
    totalLabelTd.classList.add("fw-bold");
    totalTr.appendChild(totalLabelTd);

    if (lessons.length > 0) {
        lessons[0].instructors.forEach(item => {
            const td = document.createElement("td");
            td.textContent = totals[item.id] || 0;
            td.classList.add("fw-bold");
            totalTr.appendChild(td);
        });
    }

    container.appendChild(totalTr);
}
