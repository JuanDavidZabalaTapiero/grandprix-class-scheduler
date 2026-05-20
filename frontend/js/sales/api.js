import { fetchJSON } from "../core/api.js";

export async function getSales(startDate, endDate) {
  const params = new URLSearchParams({
    start_date: startDate,
    end_date: endDate,
  });

  const json = await fetchJSON(`/sales/get?${params}`);

  return json;
}
