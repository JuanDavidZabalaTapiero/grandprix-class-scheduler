export const selectedLessons = [];

// =========================
// TOGGLE
// =========================

export function toggleLesson(lesson, occupiedVehicles = []) {

    // REMOVE
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
    
    // DB
    if (occupiedVehicles.includes(Number(lesson.vehicle_id))) {
        return "duplicate-db";
    }

    // FRONTEND 
    const existsSameSlot = selectedLessons.some(l =>
        l.date === lesson.date &&
        l.hour === lesson.hour &&
        l.vehicle_id === lesson.vehicle_id
    );

    if (existsSameSlot) {
        return "duplicate";
    }

    // AGREGAR
    selectedLessons.push(lesson);
    return true;
}

// =========================
// GET
// =========================

export function getLessons() {
    return selectedLessons;
}