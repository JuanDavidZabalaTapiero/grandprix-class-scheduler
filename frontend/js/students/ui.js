export function renderStudents(container, students) {
    if (!container) return;

    // TEMPLATES
    const template = document.getElementById("student-item-template");

    // DATASETS
    const editBaseUrl = container.dataset.editUrlBase;
    const deleteBaseUrl = container.dataset.deleteUrlBase;

    // LIMPIAR CONTENEDOR
    container.innerHTML = "";

    // ARRAY VACÍO
    if (!students.length) {
        container.innerHTML = `<div class="alert alert-info">No se encontraron estudiantes</div>`;
        return;
    }

    // ARRAY CON DATOS
    students.forEach(s => {
        const clone = template.content.cloneNode(true);

        clone.querySelector(".student-name").textContent = s.name;
        clone.querySelector(".student-document").textContent = s.document_id;
        clone.querySelector(".student-edit-btn").href = editBaseUrl.replace("0", s.id);
        clone.querySelector(".student-delete-form").action = deleteBaseUrl.replace("0", s.id);

        container.appendChild(clone);
    });
}