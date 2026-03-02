export function renderStudents(container, students) {
    if (!container) return;

    // LIMPIAR CONTENEDOR
    container.innerHTML = "";

    // ARRAY VACÍO
    if (!students.length) {
        container.innerHTML = `<div class="alert alert-info">No se encontraron estudiantes</div>`;
        return;
    }

    // ARRAY CON DATOS
    const list = document.createElement("div");
    list.className = "list-group shadow-sm";

    students.forEach(s => {
        const item = document.createElement("div");
        item.className = "list-group-item list-group-item-action d-flex justify-content-between align-items-center";
        item.innerHTML = `<div><h6 class="mb-0 fw-semibold">${s.name}</h6></div>`;
        list.appendChild(item);
    });

    container.appendChild(list);
}