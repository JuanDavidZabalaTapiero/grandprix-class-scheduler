import { selectedLessons, changeMode, lessonsToChange } from "./state.js";
import {
  handleLessonClick,
  handleRegisteredClick,
} from "./events/cellEvents.js";
import { applyLessonStyles } from "./styles.js";

export function renderSchedule(
  container,
  rows,
  selectedDate,
  totals = {},
  availabilityByDay = {},
) {
  if (!container) {
    return;
  }

  const date = new Date(`${selectedDate}T00:00:00`);
  const weekday = (date.getDay() + 6) % 7;
  const intervals = availabilityByDay[String(weekday)] || [];
  const availableHours = getAvailableHours(intervals);
  const availableTimes = availabilityByDay[String(weekday)] || [];

  container.innerHTML = "";

  // FUNCIÓN AUXILIAR
  function getAvailableHours(intervals) {
    const hours = new Set();

    intervals.forEach(({ start, end }) => {
      const [startHour, startMinute] = start.split(":").map(Number);
      const [endHour, endMinute] = end.split(":").map(Number);

      const startMinutes = startHour * 60 + startMinute;
      const endMinutes = endHour * 60 + endMinute;

      for (
        let hour = startHour;
        hour * 60 < endMinutes && hour * 60 >= startMinutes;
        hour += 1
      ) {
        hours.add(`${String(hour).padStart(2, "0")}:00`);
      }
    });

    return hours;
  }

  rows.forEach((row) => {
    const tr = document.createElement("tr");
    const hourCell = document.createElement("td");

    hourCell.textContent = row.hour_formatted;
    tr.appendChild(hourCell);

    row.instructors.forEach((instructor) => {
      const cell = document.createElement("td");
      const isBlocked = instructor.is_blocked || instructor.is_time_blocked;
      const isAvailable = availableHours.has(row.hour.slice(0, 5));

      if (
        isAvailable &&
        !instructor.lesson &&
        !instructor.is_blocked &&
        !instructor.is_time_blocked
      ) {
        cell.classList.add("student-available");
      }

      if (instructor.lesson) {
        cell.textContent =
          `${instructor.lesson.student} (${instructor.lesson.category}) | ` +
          `${instructor.lesson.vehicle_license} (${instructor.lesson.vehicle_type})`;

        cell.addEventListener("click", () => {
          handleRegisteredClick({ lesson: instructor.lesson });
        });

        applyLessonStyles(cell, instructor.lesson);

        if (isBlocked) {
          cell.classList.add("cell-blocked");
          cell.title = instructor.is_blocked
            ? "Clase en un día bloqueado"
            : "Clase en un horario bloqueado";
        }

        if (
          changeMode.active &&
          changeMode.selection.origin?.id === instructor.lesson.id
        ) {
          cell.classList.add("change-origin");
        }

        if (
          changeMode.active &&
          changeMode.selection.target === instructor.lesson.id
        ) {
          cell.classList.add("change-target");
        }

        if (
          lessonsToChange.some(
            (lesson) =>
              lesson.originId === instructor.lesson.id ||
              lesson.targetId === instructor.lesson.id,
          )
        ) {
          cell.classList.add("change-chosen");
        }
      } else if (isBlocked) {
        cell.classList.add("cell-blocked");
        cell.title = instructor.is_blocked
          ? "Instructor bloqueado durante todo el día"
          : "Instructor bloqueado en este horario";
      } else {
        if (isAvailable) {
          cell.classList.add("student-available");
        }

        cell.addEventListener("click", () => {
          handleLessonClick({
            lessonTd: cell,
            row,
            item: instructor,
          });
        });

        const isSelected = selectedLessons.some(
          (lesson) =>
            lesson.date === selectedDate &&
            lesson.hour === row.hour &&
            lesson.instructor_id === instructor.id,
        );

        if (isSelected) {
          cell.classList.add("selected");
        }

        const target = changeMode.selection.target;

        if (
          changeMode.active &&
          target &&
          typeof target === "object" &&
          target.date === selectedDate &&
          target.hour === row.hour &&
          target.instructor_id === instructor.id
        ) {
          cell.classList.add("change-target");
        }

        const isChangeChosen = lessonsToChange.some(
          (lesson) =>
            typeof lesson.target === "object" &&
            lesson.target.date === selectedDate &&
            lesson.target.hour === row.hour &&
            lesson.target.instructor_id === instructor.id,
        );

        if (isChangeChosen) {
          cell.classList.add("change-chosen");
        }
      }

      tr.appendChild(cell);
    });

    container.appendChild(tr);
  });

  const totalRow = document.createElement("tr");
  const totalLabel = document.createElement("td");

  totalLabel.textContent = "Total";
  totalLabel.classList.add("fw-bold");
  totalRow.appendChild(totalLabel);

  if (rows.length > 0) {
    rows[0].instructors.forEach((instructor) => {
      const totalCell = document.createElement("td");

      totalCell.textContent = totals[instructor.id] || 0;
      totalCell.classList.add("fw-bold");
      totalRow.appendChild(totalCell);
    });
  }

  container.appendChild(totalRow);
}
