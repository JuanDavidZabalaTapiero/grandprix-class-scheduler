export async function fetchJSON(url, options = {}) {
  const token = document.querySelector('meta[name="csrf-token"]')?.content;

  // == HEADERS ===
  const headers = {
    "Content-Type": "application/json",
  };

  // CSRF
  if (options.method && options.method !== "GET") {
    headers["X-CSRFToken"] = token;
  }

  // === RESPONSE ===
  const res = await fetch(url, {
    ...options,
    headers,
  });

  let json;

  // ERRORS
  try {
    json = await res.json();
  } catch {
    throw new Error("Respuesta inválida del servidor");
  }

  if (!res.ok) {
    throw new Error(json.message);
  }

  // OK
  return json;
}
