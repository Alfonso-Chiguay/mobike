var ctx = document.getElementById('myChart').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
                datasets: [{
                    label: 'Cantidad de usuarios Mobike',
                    maxBarThickness: 100,
                    data: [18, 54, 210, 321, 365, 498, 598, 456, 654, 600, 700, 786],
                    backgroundColor: [
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(54, 162, 235, 0.2)'
                    ],
                    borderColor: [
                        'rgba(54, 162, 235, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(54, 162, 235, 1)',             
                    ],
                    hoverBackgroundColor: [
                        'rgba(54, 200, 255, 1)',
                        'rgba(54, 200, 255, 1)',
                        'rgba(54, 200, 255, 1)',
                        'rgba(54, 200, 255, 1)',
                        'rgba(54, 200, 255, 1)',
                        'rgba(54, 200, 255, 1)',
                        'rgba(54, 200, 255, 1)',
                        'rgba(54, 200, 255, 1)',
                        'rgba(54, 200, 255, 1)',
                        'rgba(54, 200, 255, 1)',
                        'rgba(54, 200, 255, 1)',
                        'rgba(54, 200, 255, 1)',
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });


        var ctx_2 = document.getElementById('myChart2').getContext('2d');
        var myChart_2 = new Chart(ctx_2, {
            type: 'bar',
            data: {
                labels: ['Ñuñoa', 'La Reina', 'Providencia'],
                datasets: [{
                    label: 'Cantidad de usuarios Mobike por comuna',
                    maxBarThickness: 150,
                    data: [250, 126, 332],
                    backgroundColor: [
                        'rgba(255, 150, 56, 0.4)',
                        'rgba(255, 150, 56, 0.4)',
                        'rgba(255, 150, 56, 0.4)',
                    ],
                    borderColor: [
                        'rgba(255, 150, 56, 0.6)',
                        'rgba(255, 150, 56, 0.6)',
                        'rgba(255, 150, 56, 0.6)',            
                    ],
                    hoverBackgroundColor: [
                        'rgba(255, 180, 70, 0.6)',
                        'rgba(255, 180, 70, 0.6)',
                        'rgba(255, 180, 70, 0.6)',
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });


        var ctx_3 = document.getElementById('myChart3').getContext('2d');
        var myChart_3 = new Chart(ctx_3, {
            type: 'bar',
            data: {
                labels: ['Ñuñoa', 'La Reina', 'Providencia'],
                datasets: [{
                    label: 'Ganancias mensuales (Enero de 2021) por comuna',
                    maxBarThickness: 150,
                    data: [1978351, 1521889, 2165656],
                    backgroundColor: [
                        'rgba(100, 255, 56, 0.2)',
                        'rgba(100, 255, 56, 0.2)',
                        'rgba(100, 255, 56, 0.2)',
                    ],
                    borderColor: [
                        'rgba(100, 255, 56, 0.6)',
                        'rgba(100, 255, 56, 0.6)',
                        'rgba(100, 255, 56, 0.6)',            
                    ],
                    hoverBackgroundColor: [
                        'rgba(150, 255, 100, 0.6)',
                        'rgba(150, 255, 100, 0.6)',
                        'rgba(150, 255, 100, 0.6)',
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });