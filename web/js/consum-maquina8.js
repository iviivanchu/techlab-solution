var testData = {
    "type": "line",
    "data": {
        "labels": [
            "10:00:00",
                                 "10:00:10",
                                 "10:00:20",
                                 "10:00:30",
                                 "10:00:40",
                                 "10:00:50",
                                 "10:00:60",
                                 "10:00:70",
                                 "10:00:80",
                                 "10:00:90",
                                 "11:00:00",
                                 "10:00:10",
                                 "10:00:20",
                                 "10:00:30",

        ],
        "datasets": [{
                                 "label": "Consum (mA)",
            "data": [65, 59, 80, 81, 56, 55, 70,100,10,20,54,87,23,96],
                                 "fill": false, //color de fons
                                 "borderColor": "#8fc04e",
                                 "lineTension": 0.1 // perque es noti una mica la corba
        }]
    },
    "options": {
        scales: {
            yAxes: [{
                ticks: {
                    min: 0
                }
            }]
        }
    }
};

var ctx = $("#consum-maq8").get(0).getContext("2d");

var myLineChart = new Chart(ctx, {
    type: 'line',
    data: testData.data,
    options: testData.options
});
