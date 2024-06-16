// Define a global variable to store the chart instance
let myChart;

// Replace this array with your list of countries
const countries = [
    "United States",
    "United Kingdom",
    "Sri Lanka",
    "Croatia",
    "France",
    "Greece",
    "Iran",
    "Nepal",
];

// Populate dropdown with options
const dropdown = document.getElementById('inputValue');
countries.forEach(country => {
    const option = document.createElement('option');
    option.value = country;
    option.textContent = country;
    dropdown.appendChild(option);
});

document.getElementById('userInputForm').addEventListener('submit', function (event) {
    // Prevent the default form submission
    event.preventDefault();

    // Get the user input value
    const inputValue = document.getElementById('inputValue').value;

    // Fetch JSON data from the API and display it
    fetch(`/elec_prod_by_country_API?inputValue=${inputValue}`)
        .then(response => response.json())
        .then(data => {
            const co2Data = data[inputValue];
            const chartData = {
                labels: Object.keys(co2Data),
                datasets: [{
                    label: 'Sources of electricity production in ' + inputValue,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1,
                    data: Object.values(co2Data),
                }],
            };

            // If the chart already exists, destroy it before creating a new one
            if (myChart) {
                myChart.destroy();
            }

            const ctx = document.getElementById('co2-chart').getContext('2d');
            myChart = new Chart(ctx, {
                type: 'bar',
                data: chartData,
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});