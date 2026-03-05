import { showInputError, clearValidation } from "../forms/validation.js";
import { normalizeSearchTerm, validateSearchTerm } from "../students/forms/validations.js";
import { searchStudents } from "../students/api.js";
import { renderStudents } from "../students/ui.js";
import { showFlash } from "../ui/flash.js";
import { renderSpinner } from "../ui/loading.js";
import { attachDeleteConfirmation } from "../students/components/confirmDelete.js";

export function initStudentSearch({ formId, inputId, resultsId }) {
    const form = document.getElementById(formId);
    const input = document.getElementById(inputId);
    const results = document.getElementById(resultsId);

    if (!form || !input || !results) return;

    // REGISTRAR EVENTO: ALERT
    attachDeleteConfirmation(results);

    form.addEventListener("submit", async (e) => {

        // === FORM ===
        e.preventDefault();

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

        // === RESULTADOS ===

        // SPINNER
        renderSpinner(results)

        // RENDERIZAR
        try {
            const students = await searchStudents(normalized);
            renderStudents(results, students);
        } catch (err) {
            results.innerHTML = "";
            showFlash("danger", err.message);
        }

    });
}