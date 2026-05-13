export function createBarChart(canvas, labels = [], data = []) {
    return new Chart(canvas, {
        type: "bar",
        data: {
            labels,
            datasets: [{
                label: "Ventas",
                data
            }]
        }
    });
}