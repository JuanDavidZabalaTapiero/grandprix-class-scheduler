import { showInputError, clearValidation } from "../forms/validation.js";
import {
  normalizeSearchTerm,
  validateSearchTerm,
} from "../students/forms/validations.js";
import { searchStudents } from "../students/api.js";
import { renderStudents } from "../students/ui.js";
import { showFlash } from "../ui/flash.js";
import { renderSpinner } from "../ui/loading.js";
import { attachDeleteConfirmation } from "../ui/confirmDelete.js";

export function initStudentSearch({
  formId,
  inputId,
  resultsId,
  containerAutocompleteID,
}) {
  // === ELEMENTOS ===
  const form = document.getElementById(formId);
  const input = document.getElementById(inputId);
  const results = document.getElementById(resultsId);
  const containerAutocomplete = document.getElementById(
    containerAutocompleteID,
  );

  if (!form || !input || !results) return;

  // REGISTRAR EVENTO: ALERT
  attachDeleteConfirmation(results, "student-delete-form", "alumno");

  form.addEventListener("submit", async (e) => {
    // === FORM ===
    e.preventDefault();

    // VACIAR AUTOCOMPLETE
    containerAutocomplete.innerHTML = "";

    // TÉRMINO
    const term = input.value;

    // NORMALIZACIÓN
    const normalized = normalizeSearchTerm(term);

    // VALIDACIÓN
    clearValidation(input);

    const error = validateSearchTerm(normalized);
    if (error) {
      showInputError(input, error);
      return;
    }

    // === FETCH ===

    // SPINNER
    renderSpinner(results);

    try {
      const students = await searchStudents(normalized);

      // RENDERIZAR
      renderStudents(results, students);
    } catch (err) {
      results.innerHTML = "";
      showFlash("danger", err.message);
    }
  });
}
