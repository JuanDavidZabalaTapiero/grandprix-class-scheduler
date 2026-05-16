import { fetchJSON } from "../core/api.js";

export async function autocompleteStudents(term) {
    const json = await fetchJSON(`/api/students/autocomplete?search=${encodeURIComponent(term)}`);
    return json.data;
}

export async function searchStudents(term) {
    const json = await fetchJSON(`/api/students?search=${encodeURIComponent(term)}`);
    return json.data;
}
