// =========================
// STATE (GLOBAL)
// =========================

// SELECTED
export const selectedLessons = [];

// EDITED
export const editedLessons = {};

// DELETE
export const lessonsToDelete = [];

// CHANGE MODE
export const changeMode = {
    active: false,
    selection: {
        origin: null,
        target: null // id | {object}
    }
};

export const lessonsToChange = [];


// =========================
// HELPERS
// =========================

function removeFromArray(arr, value) {
    const idx = arr.indexOf(value);
    if (idx !== -1) arr.splice(idx, 1);
}


// =========================
// VALIDATIONS
// =========================

export function validateSlot(lesson, occupiedVehicles = [], options = {}) {

    const { ignoreVehicleId = null } = options;

    // DB
    if (occupiedVehicles.includes(Number(lesson.vehicle_id)) && Number(lesson.vehicle_id) !== Number(ignoreVehicleId)) {
        return "duplicate-db";
    }

    // LOCAL
    const existsSameSlot = selectedLessons.some(l =>
        l.date === lesson.date &&
        l.hour === lesson.hour &&
        l.vehicle_id === lesson.vehicle_id
    );

    if (existsSameSlot) {
        return "duplicate";
    }

    return true;
}


// =========================
// SELECTED LESSONS
// =========================

export function toggleLesson(lesson, occupiedVehicles = []) {

    // YA EXISTE → REMOVE
    const index = selectedLessons.findIndex(l =>
        l.date === lesson.date &&
        l.hour === lesson.hour &&
        l.instructor_id === lesson.instructor_id
    );

    if (index >= 0) {
        selectedLessons.splice(index, 1);
        return false;
    }

    // === VEHÍCULO OCUPADO ===
    const result = validateSlot(lesson, occupiedVehicles);

    if (result !== true) {
        return result;
    }

    // AGREGAR
    selectedLessons.push(lesson);
    return true;
}

export function getLessons() {
    return selectedLessons;
}


// =========================
// EDITED LESSONS
// =========================

export function changeLesson(element) {

    // == DATA ==
    const lessonId = element.dataset.id;
    const field = element.dataset.field;

    let value;

    // DETECTAR TIPO DE INPUT
    if (element.type === "checkbox") {
        value = element.checked;
    } else {
        value = Number(element.value);
    }

    // == GUARDAR ==
    if (!editedLessons[lessonId]) {
        editedLessons[lessonId] = {};
    }
    editedLessons[lessonId][field] = value;
}

export function getEditedLessons() {
    return Object.entries(editedLessons).map(([id, data]) => ({ id: Number(id), ...data })); // ARRAY
}


// =========================
// TO DELETE LESSONS
// =========================

export function toggleLessonsToDelete(checkbox) {
    const lessonId = checkbox.dataset.id;
    const checked = checkbox.checked; // TRUE / FALSE

    // === ALL ===
    if (lessonId === "all") {

        const allCheckboxes = document.querySelectorAll(".lesson-checkbox");

        allCheckboxes.forEach(cb => {
            if (cb.dataset.id === "all") return;

            // CAMBIO DE VALOR
            cb.checked = checked;

            // AÑADIR / QUITAR
            const id = Number(cb.dataset.id);
            if (checked) {
                if (!lessonsToDelete.includes(id)) {
                    lessonsToDelete.push(id);
                }
            } else {
                removeFromArray(lessonsToDelete, id);
            }
        });

        return;
    }

    // === INDIVIDUAL ===
    const id = Number(lessonId);
    if (checked) {
        lessonsToDelete.push(id);
    } else {
        removeFromArray(lessonsToDelete, id);
    }
}

export function getLessonsToDelete() {
    return lessonsToDelete;
}


// =========================
// CHANGE LESSONS
// =========================

export function toggleChangeMode() {
    changeMode.active = !changeMode.active;

    if (!changeMode.active) {
        changeMode.selection.origin = null;
        changeMode.selection.target = null;
    }
}

export function getLessonsToChange() {
    return lessonsToChange;
}