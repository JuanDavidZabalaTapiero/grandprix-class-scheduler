export function showInputError(input, message) {
  input.classList.add("is-invalid");

  let feedback = input.parentElement.querySelector(".invalid-feedback");
  if (!feedback) {
    feedback = document.createElement("div");
    feedback.className = "invalid-feedback";
    input.parentElement.appendChild(feedback);
  }
  feedback.textContent = message;
}

export function clearValidation(input) {
  input.classList.remove("is-invalid");

  const feedback = input.parentElement.querySelector(".invalid-feedback");
  if (feedback) {
    feedback.remove();
  }
}
