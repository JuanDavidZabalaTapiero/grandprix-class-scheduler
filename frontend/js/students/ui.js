export function renderStudents(container, students) {
    if (!container) return;

    // DATASETS
    const baseUrl = container.dataset.editUrlBase;

    // LIMPIAR CONTENEDOR
    container.innerHTML = "";

    // ARRAY VACÍO
    if (!students.length) {
        container.innerHTML = `<div class="alert alert-info">No se encontraron estudiantes</div>`;
        return;
    }

    // ARRAY CON DATOS
    const list = document.createElement("div");
    list.className = "d-flex flex-column gap-2";

    students.forEach(s => {
        const item = document.createElement("div");
        item.className = "d-flex align-items-center justify-content-between px-3 py-2 border rounded-3 bg-white";

        const editUrl = baseUrl.replace("0", s.id);
        item.innerHTML = `
        <div class="d-flex align-items-center gap-3">
            <span class="fw-semibold">${s.name}</span>
            <span class="text-secondary small">${s.document_id}</span>
        </div>
        
        <a href="${editUrl}" class="btn btn-sm btn-light border d-inline-flex align-items-center gap-1">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pen" viewBox="0 0 16 16">
                <path d="m13.498.795.149-.149a1.207 1.207 0 1 1 1.707 1.708l-.149.148a1.5 1.5 0 0 1-.059 2.059L4.854 14.854a.5.5 0 0 1-.233.131l-4 1a.5.5 0 0 1-.606-.606l1-4a.5.5 0 0 1 .131-.232l9.642-9.642a.5.5 0 0 0-.642.056L6.854 4.854a.5.5 0 1 1-.708-.708L9.44.854A1.5 1.5 0 0 1 11.5.796a1.5 1.5 0 0 1 1.998-.001m-.644.766a.5.5 0 0 0-.707 0L1.95 11.756l-.764 3.057 3.057-.764L14.44 3.854a.5.5 0 0 0 0-.708z"/>
            </svg>
        
            <span>Editar</span>
        </a>
        `;

        list.appendChild(item);
    });

    container.appendChild(list);
}