import { autocompleteStudents } from "./api.js";
import { renderStudentsAutocomplete } from "./ui.js";

export async function handleStudentsAutocomplete(value, container, input) {
    // MENOS DE 3 CARACTERES
    if (value.length < 3) {
        container.innerHTML = "";
        return;
    }

    // CONSULTAR API
    const students = await autocompleteStudents(value);

    // RENDERIZAR
    renderStudentsAutocomplete(container, students, input);
}