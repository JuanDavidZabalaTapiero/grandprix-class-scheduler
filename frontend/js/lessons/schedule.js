import { getSchedule } from "./api.js";
import { showFlash } from "../ui/flash.js";
import { renderSchedule } from "./ui.js";
import { getScheduleRefs, setScheduleRefs } from "./scheduleRefs.js";

// =========================
// CARGAR CLASES
// =========================

export async function loadSchedule(
  dateInput,
  container,
  availabilityByDay = {},
) {
  try {
    const schedule = await getSchedule(dateInput.value);

    renderSchedule(
      container,
      schedule.lessons,
      dateInput.value,
      schedule.totals,
      availabilityByDay,
    );
  } catch (error) {
    container.innerHTML = "";
    showFlash("danger", error.message);
  }
}

// =========================
// RE-RENDER
// =========================

export function rerenderSchedule() {
  const { dateInput, container, availabilityByDay } = getScheduleRefs();

  if (dateInput && container) {
    loadSchedule(dateInput, container, availabilityByDay);
  }
}

// =========================
// INICIALIZACIÓN
// =========================

export function initSchedule({ dateId, containerId, availabilityByDay = {} }) {
  const dateInput = document.getElementById(dateId);
  const container = document.getElementById(containerId);

  if (!dateInput || !container) {
    return;
  }

  setScheduleRefs({
    dateInput,
    container,
    availabilityByDay,
  });

  loadSchedule(dateInput, container, availabilityByDay);

  dateInput.addEventListener("change", () => {
    loadSchedule(dateInput, container, availabilityByDay);
  });
}
