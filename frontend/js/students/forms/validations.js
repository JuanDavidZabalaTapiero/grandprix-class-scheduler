export function normalizeSearchTerm(term) {
    return term.trim().toUpperCase();
}

export function validateSearchTerm(term) {
    if (!term || term.length < 2) {
        return "Ingrese al menos 2 caracteres";
    }

    return null; // VÁLIDO
}