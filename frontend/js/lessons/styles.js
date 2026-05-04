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

    // T-PRÁCTICO
    if (lesson.category === "T-PRÁCTICO") {
        lessonTd.classList.add("lesson-t-practico");
        return;
    }

    // M-DEFENSIVO
    if (lesson.category === "M-DEFENSIVO") {
        lessonTd.classList.add("lesson-m-defensivo");
        return;
    }

    // DEFAULT
    lessonTd.classList.add("lesson-default");
}
