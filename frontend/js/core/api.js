export async function fetchJSON(url, options = {}) {
  // == HEADERS ===
  const headers = {
    "Content-Type": "application/json",
  };

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
