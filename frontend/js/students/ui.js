export function renderStudentsAutocomplete(container, students, input) {
  if (!container) return;

  // LIMPIAR CONTENEDOR
  container.innerHTML = "";

  // MOSTRAR DATOS
  students.forEach((student) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className =
      "list-group-item list-group-item-action d-flex align-items-center gap-2";

    button.innerHTML = `
            <div class="fw-semibold">${student.name}</div>
            <small class="text-muted">
                ${student.document_id}
            </small>
        `;

    // EVENTO CLICK
    button.addEventListener("click", () => {
      input.value = student.name;
      container.innerHTML = "";
    });

    container.appendChild(button);
  });
}

export function renderStudents(container, students) {
  if (!container) return;

  // TEMPLATES
  const template = document.getElementById("student-item-template");

  // DATASETS
  const editBaseUrl = container.dataset.editUrlBase;
  const deleteBaseUrl = container.dataset.deleteUrlBase;
  const enrollmentUrl = container.dataset.enrollmentUrlBase;

  // LIMPIAR CONTENEDOR
  container.innerHTML = "";

  // ARRAY VACÍO
  if (!students.length) {
    container.innerHTML = `<div class="alert alert-info">No se encontraron estudiantes</div>`;
    return;
  }

  // ARRAY CON DATOS
  students.forEach((s) => {
    const clone = template.content.cloneNode(true);

    clone.querySelector(".student-name").textContent = s.name;
    clone.querySelector(".student-document").textContent = s.document_id;
    clone.querySelector(".student-edit-btn").href = editBaseUrl.replace(
      "0",
      s.id,
    );
    clone.querySelector(".student-delete-form").action = deleteBaseUrl.replace(
      "0",
      s.id,
    );

    // MATRICULAS
    const enrollmentContainer = clone.querySelector(".student-enrollments");

    if (s.enrollments.length > 0) {
      s.enrollments.forEach((e) => {
        const btn = document.createElement("a");

        btn.href = enrollmentUrl.replace("0", e.id);
        btn.textContent = e.category;
        btn.className = "btn btn-outline-primary w-100 text-center";

        enrollmentContainer.appendChild(btn);
      });
    } else {
      enrollmentContainer.innerHTML =
        "<div class='alert alert-info mb-0'>No tiene matrículas registradas</div>";
    }

    container.appendChild(clone);
  });
}
