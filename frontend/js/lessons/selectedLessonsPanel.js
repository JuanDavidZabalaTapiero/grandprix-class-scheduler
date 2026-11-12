import { getLessons } from "./state.js";

function formatLessonDate(dateValue) {
  const [year, month, day] = dateValue.split("-").map(Number);
  const date = new Date(year, month - 1, day);

  return new Intl.DateTimeFormat("es-CO", {
    weekday: "long",
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
  }).format(date);
}

function getInstructorAndVehicle(lesson) {
  const select = document.getElementById(`select-${lesson.instructor_id}`);

  if (!select) {
    return { instructorName: "", vehicleLabel: "" };
  }

  const option = Array.from(select.options).find(
    (item) => item.value === String(lesson.instructor_vehicle_id),
  );

  return {
    instructorName: select.dataset.instructorName || "",
    vehicleLabel: option?.textContent.trim() || "",
  };
}

function createLessonItem(lesson) {
  const item = document.createElement("li");
  item.className = "list-group-item";

  const dateAndTime = document.createElement("div");
  dateAndTime.className = "fw-semibold";
  dateAndTime.textContent = `${formatLessonDate(lesson.date)} · ${lesson.hour.slice(0, 5)}`;

  item.appendChild(dateAndTime);

  const { instructorName, vehicleLabel } = getInstructorAndVehicle(lesson);
  const details = [];

  if (instructorName) {
    details.push(`Instructor: ${instructorName}`);
  }

  if (vehicleLabel) {
    details.push(`Vehículo: ${vehicleLabel}`);
  }

  if (details.length) {
    const detailText = document.createElement("small");
    detailText.className = "text-muted d-block";
    detailText.textContent = details.join(" · ");
    item.appendChild(detailText);
  }

  return item;
}

export function renderSelectedLessons() {
  const list = document.getElementById("selected-lessons-list");
  const count = document.getElementById("selected-lessons-count");
  const emptyMessage = document.getElementById("selected-lessons-empty");

  if (!list || !count || !emptyMessage) return;

  const lessons = getLessons()
    .slice()
    .sort((a, b) => {
      const dateOrder = a.date.localeCompare(b.date);
      if (dateOrder !== 0) return dateOrder;

      const timeOrder = a.hour.localeCompare(b.hour);
      if (timeOrder !== 0) return timeOrder;

      return Number(a.instructor_id) - Number(b.instructor_id);
    });

  list.replaceChildren(...lessons.map(createLessonItem));
  count.textContent = String(lessons.length);

  emptyMessage.classList.toggle("d-none", lessons.length > 0);
  list.classList.toggle("d-none", lessons.length === 0);
}

export function initSelectedLessonsPanel() {
  renderSelectedLessons();
}
