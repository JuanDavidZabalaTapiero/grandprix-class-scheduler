export function showLessonsModal(button) {
  const instructor = button.dataset.instructor;

  const date = button.dataset.date;

  const lessons = JSON.parse(button.dataset.lessons);

  // =========================================
  // TITLE
  // =========================================

  const title = document.getElementById("lessonsModalTitle");
  title.innerText = `${instructor} | ${date}`;

  // =========================================
  // CONTENT
  // =========================================

  const content = document.getElementById("lessonsModalContent");

  let html = `
    <div class="table-responsive">
    <table class="table table-bordered align-middle text-center">
        <thead class="table-light">
            <tr>
                <th>Hora</th>
                <th>Alumno</th>
                <th>Categoría</th>
                <th>Estado</th>
                <th>$</th>
            </tr>
        </thead>
    <tbody>
    `;

  for (const lesson of lessons) {
    html += `
        <tr>
            <td>${lesson.start_time}</td>
            <td>${lesson.student}</td>
            <td>${lesson.category}</td>
            <td>${lesson.lesson_status}</td>
            <td>
                <span class="badge text-bg-success">Pagada</span>
            </td>
        </tr>
        `;
  }

  html += `
    </tbody>
    </table>
    </div>
    `;

  content.innerHTML = html;
}
