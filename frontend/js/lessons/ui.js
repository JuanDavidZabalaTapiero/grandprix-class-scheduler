import { selectedLessons, changeMode, lessonsToChange } from "./state.js";
import {
  handleLessonClick,
  handleRegisteredClick,
} from "./events/cellEvents.js";
import { applyLessonStyles } from "./styles.js";

export function renderSchedule(container, lessons, date, totals = {}) {
  if (!container) return;

  container.innerHTML = "";

  lessons.forEach((row) => {
    const tr = document.createElement("tr");

    const hourTd = document.createElement("td");
    hourTd.textContent = row.hour_formatted;
    tr.appendChild(hourTd);

    row.instructors.forEach((item) => {
      const lessonTd = document.createElement("td");
      const isBlocked = item.is_blocked || item.is_time_blocked;

      if (item.lesson) {
        lessonTd.textContent = `${item.lesson.student} (${item.lesson.category}) | ${item.lesson.vehicle_license} (${item.lesson.vehicle_type})`;

        lessonTd.addEventListener("click", () => {
          handleRegisteredClick({ lesson: item.lesson });
        });

        applyLessonStyles(lessonTd, item.lesson);

        if (isBlocked) {
          lessonTd.classList.add("cell-blocked");
          lessonTd.title = item.is_blocked
            ? "Clase en un día bloqueado"
            : "Clase en un horario bloqueado";
        }

        if (
          changeMode.active &&
          changeMode.selection.origin &&
          changeMode.selection.origin.id === item.lesson.id
        ) {
          lessonTd.classList.add("change-origin");
        }

        if (
          changeMode.active &&
          changeMode.selection.target === item.lesson.id
        ) {
          lessonTd.classList.add("change-target");
        }

        const isChosen = lessonsToChange.some(
          (change) =>
            change.originId === item.lesson.id ||
            change.target === item.lesson.id,
        );

        if (isChosen) {
          lessonTd.classList.add("change-chosen");
        }
      } else if (isBlocked) {
        lessonTd.classList.add("cell-blocked");
        lessonTd.title = item.is_blocked
          ? "Instructor bloqueado durante todo el día"
          : "Instructor bloqueado en este horario";
      } else {
        lessonTd.addEventListener("click", () => {
          handleLessonClick({ lessonTd, row, item });
        });

        const selected = selectedLessons.some(
          (lesson) =>
            lesson.date === date &&
            lesson.hour === row.hour &&
            lesson.instructor_id === item.id,
        );

        if (selected) {
          lessonTd.classList.add("selected");
        }

        const target = changeMode.selection.target;

        if (
          changeMode.active &&
          target &&
          typeof target === "object" &&
          target.date === date &&
          target.hour === row.hour &&
          target.instructor_id === item.id
        ) {
          lessonTd.classList.add("change-target");
        }

        const isChosenTarget = lessonsToChange.some((change) => {
          const target = change.target;

          return (
            typeof target === "object" &&
            target.date === date &&
            target.hour === row.hour &&
            target.instructor_id === item.id
          );
        });

        if (isChosenTarget) {
          lessonTd.classList.add("change-chosen");
        }
      }

      tr.appendChild(lessonTd);
    });

    container.appendChild(tr);
  });

  const totalTr = document.createElement("tr");

  const totalLabelTd = document.createElement("td");
  totalLabelTd.textContent = "Total";
  totalLabelTd.classList.add("fw-bold");
  totalTr.appendChild(totalLabelTd);

  if (lessons.length > 0) {
    lessons[0].instructors.forEach((item) => {
      const td = document.createElement("td");
      td.textContent = totals[item.id] || 0;
      td.classList.add("fw-bold");
      totalTr.appendChild(td);
    });
  }

  container.appendChild(totalTr);
}
