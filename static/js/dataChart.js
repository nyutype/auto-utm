document.addEventListener("DOMContentLoaded", function() {
    const data = {{ data|tojson }};
    const ctx = document.getElementById('dataChart').getContext('2d');
    const dataChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.x_values, // your x-values
            datasets: [{
                label: 'Load (kN) vs. Crosshead (mm)',
                data: data.y_values, // your y-values
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Populate table headers
    let headers = document.getElementById('headers');
    data.columns.forEach(col => {
        let header = document.createElement('th');
        header.textContent = col;
        headers.appendChild(header);
    });

    // Populate table body
    let tableBody = document.getElementById('table-body');
    data.rows.forEach(row => {
        let tr = document.createElement('tr');
        row.forEach(cell => {
            let td = document.createElement('td');
            td.textContent = cell;
            tr.appendChild(td);
        });
        tableBody.appendChild(tr);
    });
});