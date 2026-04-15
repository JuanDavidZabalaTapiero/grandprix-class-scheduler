import { fetchJSON } from "../core/api.js";

export async function getSchedule(date) {
    const json = await fetchJSON(`/api/lessons?date=${encodeURIComponent(date)}`);
    return json.data;
}

export async function createLessons(data) {
    const json = await fetchJSON("/api/lessons", { method: "POST", body: JSON.stringify(data) });
    return json;
}