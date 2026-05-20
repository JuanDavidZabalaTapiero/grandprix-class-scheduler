export function renderSpinner(container) {
  if (!container) return;

  container.innerHTML = `
        <div class="text-center p-3">
            <div class="spinner-border text-primary"></div>
        </div>
    `;
}
