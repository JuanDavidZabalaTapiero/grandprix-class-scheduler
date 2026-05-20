import { showFlashFixed } from "../../ui/flash.js";
import { getScheduleRefs } from "../scheduleRefs.js";
import { changeMode, validateSlot, toggleLesson } from "../state.js";
import { rerenderSchedule } from "../schedule.js";

// =========================
// HELPERS
// =========================

function handleValidationResult(result) {
  if (result === "duplicate-db") {
    showFlashFixed("danger", "Ese vehículo ya está ocupado en ese horario");
    return false;
  }

  if (result === "duplicate") {
    showFlashFixed("warning", "Ese vehículo ya está asignado en ese horario");
    return false;
  }

  return true;
}

function isSameSlot(a, b) {
  return (
    a &&
    b &&
    a.date === b.date &&
    a.hour === b.hour &&
    a.instructor_id === b.instructor_id
  );
}

// =========================
// CLASE (TD)
// =========================

export function handleLessonClick({ lessonTd, row, item }) {
  // === DATA ===
  const { dateInput } = getScheduleRefs();

  const date = dateInput.value;
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
    instructor_vehicle_id: instructorVehicleId,
  };

  // =========================
  // 🟣 MODO CAMBIO
  // =========================

  if (changeMode.active) {
    const origin = changeMode.selection.origin;

    if (!origin) {
      changeMode.selection.target = null;
      return;
    }

    const currentTarget = changeMode.selection.target;

    // TOGGLE OFF
    if (isSameSlot(currentTarget, lessonData)) {
      changeMode.selection.target = null;
    } else {
      // VALIDACIÓN
      const ignoreVehicleId = origin.vehicle_id;

      const result = validateSlot(lessonData, row.vehicles_ids, {
        ignoreVehicleId,
      });

      if (!handleValidationResult(result)) return;

      changeMode.selection.target = lessonData;
    }

    // RE-RENDER
    rerenderSchedule();
    return;
  }

  // =========================
  // 🟢 MODO NORMAL
  // =========================

  const result = toggleLesson(lessonData, row.vehicles_ids);

  if (!handleValidationResult(result)) return;

  // RE-RENDER
  rerenderSchedule();
}

export function handleRegisteredClick({ lesson }) {
  if (!changeMode.active) return;

  const lessonId = lesson.id;
  const { origin, target } = changeMode.selection;

  // ORIGIN
  if (!origin) {
    changeMode.selection.target = null;

    changeMode.selection.origin = {
      id: lessonId,
      vehicle_id: lesson.vehicle_id,
    };
  } else if (origin.id === lessonId) {
    changeMode.selection.target = null;
    changeMode.selection.origin = null;
  }

  // TARGET
  else if (!target) {
    changeMode.selection.target = lessonId;
  } else if (target === lessonId) {
    changeMode.selection.target = null;
  }

  // RE-RENDER
  rerenderSchedule();
}
