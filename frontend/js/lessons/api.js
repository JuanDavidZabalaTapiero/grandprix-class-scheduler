import { fetchJSON } from "../core/api.js";

export async function getSchedule(date) {
  const json = await fetchJSON(`/api/lessons?date=${encodeURIComponent(date)}`);
  return json;
}

export async function createLessons(data) {
  const json = await fetchJSON("/api/lessons", {
    method: "POST",
    body: JSON.stringify(data),
  });
  return json;
}

export async function updateLessons(data) {
  const json = await fetchJSON("/api/lessons", {
    method: "PUT",
    body: JSON.stringify(data),
  });
  return json;
}

export async function deleteLessons(data) {
  const json = await fetchJSON("/api/lessons/delete", {
    method: "POST",
    body: JSON.stringify(data),
  });
  return json;
}

export async function saveChanges(data) {
  const json = await fetchJSON("/api/lessons/change", {
    method: "POST",
    body: JSON.stringify(data),
  });
  return json;
}
