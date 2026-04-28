export function applyLessonStyles(lessonTd, lesson) {

    // LIMPIAR CLASES PREVIAS
    lessonTd.className = "";

    // EXAMEN
    if (lesson.type === "EXAMEN") {
        lessonTd.classList.add("lesson-examen");
        return;
    }

    // REFUERZO
    if (lesson.category === "REFUERZO") {
        lessonTd.classList.add("lesson-refuerzo");
        return;
    }

    // DEFAULT
    lessonTd.classList.add("lesson-default");
}
