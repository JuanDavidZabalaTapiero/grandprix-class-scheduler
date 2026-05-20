import { onInputChange } from "../students/events.js";
import { handleStudentsAutocomplete } from "../students/controller.js";

export function initStudentAutocomplete(input, container) {
  onInputChange(input, (value) => {
    handleStudentsAutocomplete(value, container, input);
  });
}
