document.addEventListener('DOMContentLoaded', function () {
    // Temperature Data for the Chart
    const ctx = document.getElementById('temperatureChart').getContext('2d');
    const temperatureChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            datasets: [{
                label: 'Temperature (°C)',
                data: [22, 24, 20, 25, 30, 35, 33, 30, 28, 26, 23, 20],
                borderColor: '#f59e0b',  /* Updated line color to match theme */
                fill: false,
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: true,
                    labels: {
                        color: '#ffffff'  /* Text color in the legend */
                    }
                }
            },
            scales: {
                x: {
                    ticks: {
                        color: '#ffffff'  /* X-axis labels color */
                    },
                    grid: {
                        color: '#4a5568'  /* Grid color */
                    }
                },
                y: {
                    ticks: {
                        color: '#ffffff'  /* Y-axis labels color */
                    },
                    grid: {
                        color: '#4a5568'  /* Grid color */
                    }
                }
            }
        }
    });

    // Toggle Button Functionality
    const toggleButton = document.getElementById('toggleButton');
    let isOn = false;

    toggleButton.addEventListener('click', function () {
        isOn = !isOn;
        this.textContent = isOn ? 'Turn Off' : 'Turn On';
        this.classList.toggle('active');
    });

    // Example: Dynamically Update Temperature (this could be updated from a real API)
    setInterval(() => {
        const currentTemperature = document.getElementById('currentTemperature');
        const newTemp = (Math.random() * 10 + 20).toFixed(1); // Random temperature between 20 and 30
        currentTemperature.textContent = `${newTemp}°C`;
    }, 3000);
});
