import { onInputChange } from "../students/events.js";
import { handleStudentsAutocomplete } from "../students/controller.js";

export function initStudentAutocomplete(input, container) {
  onInputChange(input, (value) => {
    handleStudentsAutocomplete(value, container, input);
  });

  // FOCUS AL PRIMER ITEM
  input.addEventListener("keydown", (event) => {
    if (event.key === "ArrowDown") {
      const firstItem = container.querySelector(".list-group-item");
      if (firstItem) {
        event.preventDefault();
        firstItem.focus();
      }
    }
  });
}
