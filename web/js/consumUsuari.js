const $grafica-pot = document.querySelector("#consumUsuari");
const etiquetes = ["Genere", "Febrer", "Març", "Abril"]

const consumMitja = {
    label: "Consum mitjà (mA)",
    data: [1, 2, 3, 4],
    backgroundColor: 'rgba(54, 162, 235, 0.2)',
    borderColor: 'rgba(54, 162, 235, 1)',
    borderWidth: 1,
};
const numReserves = {
    label: "Reserves",
    data: [4, 4, 5, 10],
    backgroundColor: 'rgba(255, 159, 64, 0.2)',
    borderColor: 'rgba(255, 159, 64, 1)',
    borderWidth: 1,
};

new Chart($grafica-pot, {
    type: 'bar',
    data: {
        labels: etiquetes,
        datasets: [
            numReserves,
            consumMitja,
        ]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }],
        },
    }
});
