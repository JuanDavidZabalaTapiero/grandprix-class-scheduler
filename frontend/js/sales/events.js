import { getSales } from "./api.js";
import { createBarChart } from "./chart.js";
import { showFlashFixed } from "../ui/flash.js";

export function initGenerateChart({ buttonId, startDateId, endDateId, canvasId }) {

    const button = document.getElementById(buttonId);
    const canvas = document.getElementById(canvasId);

    if (!button || !canvas) return;

    const chart = createBarChart(canvas);

    // FUNCTION
    async function loadChart() {

        // DATA TO SEND
        const startDate = document.getElementById(startDateId).value;
        const endDate = document.getElementById(endDateId).value;

        try {

            // DATA RECEIVED
            const data = await getSales(
                startDate,
                endDate
            );

            // UPDATE CHART
            chart.data.labels = data.labels;
            chart.data.datasets[0].data = data.sales;
            chart.update();

        } catch (error) {
            showFlashFixed("danger", error.message);
        }
    }

    // BUTTON EVENT
    button.addEventListener("click", loadChart);

    // INITIAL LOAD
    loadChart();
}