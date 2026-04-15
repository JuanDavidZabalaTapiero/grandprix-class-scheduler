import { handleLessonClick } from "./events.js";
import { selectedLessons } from "./state.js";

export function renderSchedule(container, lessons, date) {
    if (!container) return;

    // LIMPIAR CONTENEDOR
    container.innerHTML = "";

    // RENDER
    lessons.forEach(row => {
        const tr = document.createElement("tr");

        // HORA
        const hourTd = document.createElement("td");
        hourTd.textContent = row.hour
        tr.appendChild(hourTd);

        // CLASES
        row.instructors.forEach(item => {
            const lessonTd = document.createElement("td");

            if (item.lesson) {

                // === CLASE OCUPADA ===
                lessonTd.textContent = `${item.lesson.student} (${item.lesson.category}) | ${item.lesson.vehicle_license} (${item.lesson.vehicle_type})`;
                
            } else {

                // === CLASE DISPONIBLE ===

                // VERIFICAR SELECCIÓN
                const hour = row.hour;
                const instructorId = item.id;

                const selected = selectedLessons.some(l => l.date === date && l.hour === hour && l.instructor_id === instructorId)

                if (selected) {
                    lessonTd.classList.add("selected");
                }

                // EVENTO
                lessonTd.addEventListener("click", () => {
                    handleLessonClick({ lessonTd, row, item })
                });
            }

            tr.appendChild(lessonTd);
        })

        container.appendChild(tr);
    })
}