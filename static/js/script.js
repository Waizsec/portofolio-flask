document.getElementById('fetch-button').addEventListener('click', function () {
    const url = document.getElementById('url-input').value;

    fetch(url)
        .then(response => response.text())
        .then(data => {
            const jsonData = JSON.parse(data);
            const tableBody = document.querySelector('#data-table tbody');
            tableBody.innerHTML = '';

            jsonData.forEach(item => {
                const row = document.createElement('tr');
                row.classList.add('tr-custom');
                for (const key in item) {
                    if (item.hasOwnProperty(key)) {
                        const cell = document.createElement('td');
                        cell.textContent = item[key];
                        row.appendChild(cell);
                    }
                }
                tableBody.appendChild(row);
            });

        })
        .catch(error => {
            console.error("Error fetching data:", error);
        });
});