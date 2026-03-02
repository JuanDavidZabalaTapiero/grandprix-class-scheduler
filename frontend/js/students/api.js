export async function searchStudents(term) {
    const res = await fetch(`/api/students?search=${encodeURIComponent(term)}`);

    let json;

    // ERRORS
    try {
        json = await res.json();
    } catch {
        throw new Error("Respuesta inválida del servidor");
    }

    if (!res.ok) {
        throw new Error(json.message);
    }

    // OK
    return json.data;
}