import { showLessonsModal } from "./ui.js";

export function initShowLessonsModal() {
  const buttons = document.querySelectorAll(".show-modal");

  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      showLessonsModal(button);
    });
  });
}
