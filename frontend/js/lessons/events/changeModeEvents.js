import { toggleChangeMode, changeMode, lessonsToChange } from "../state.js";
import { rerenderSchedule } from "../schedule.js";
import { showFlashFixed } from "../../ui/flash.js";

// =========================
// CAMBIAR CLASES
// =========================

export function initToggleChangeMode({ buttonId }) {
  const btn = document.getElementById(buttonId);
  if (!btn) return;

  btn.addEventListener("click", () => {
    toggleChangeMode();

    // RE-RENDER
    rerenderSchedule();

    if (changeMode.active) {
      showFlashFixed("info", "Modo cambio activado");
    } else {
      showFlashFixed("warning", "Modo cambio desactivado");
    }
  });
}

export function saveChange({ buttonId }) {
  const btn = document.getElementById(buttonId);
  if (!btn) return;

  btn.addEventListener("click", () => {
    if (!changeMode.active) {
      return;
    }

    const { origin, target } = changeMode.selection;

    if (!origin) {
      showFlashFixed("warning", "Selecciona una clase origen");
      return;
    }

    if (!target) {
      showFlashFixed("warning", "Selecciona el destino de la clase");
      return;
    }

    lessonsToChange.push({ originId: origin.id, target: target });

    // RESET
    changeMode.selection.origin = null;
    changeMode.selection.target = null;

    // RE-RENDER
    rerenderSchedule();
  });
}
