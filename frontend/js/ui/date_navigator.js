export function initDateNavigator({ inputId, prevId, nextId }) {
  const input = document.getElementById(inputId);
  const prevBtn = document.getElementById(prevId);
  const nextBtn = document.getElementById(nextId);

  if (!input || !prevBtn || !nextBtn) return;

  function changeDate(days) {
    const [year, month, day] = input.value.split("-").map(Number);

    const current = new Date(year, month - 1, day);
    current.setDate(current.getDate() + days);

    const pad = (n) => String(n).padStart(2, "0");

    const formatted = `${current.getFullYear()}-${pad(current.getMonth() + 1)}-${pad(current.getDate())}`;

    input.value = formatted;

    // DISPARAR CHAGE
    input.dispatchEvent(new Event("change"));
  }

  prevBtn.addEventListener("click", () => changeDate(-1));
  nextBtn.addEventListener("click", () => changeDate(1));
}
