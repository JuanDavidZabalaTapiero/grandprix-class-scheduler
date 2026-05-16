export function onInputChange(input, callback) {
    if (!input) return;

    input.addEventListener("input", (event) => {
        callback(event.target.value);
    });
}