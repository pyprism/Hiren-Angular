/**
 * Created by prism on 12/16/16.
 */
function graph() {
    $.ajax('/chart/', {
        contentType: 'application/json',
        success: function(data) {
            console.log(data);
            var myChart = Highcharts.chart('chart_full', {
                chart: {
                    type: 'spline',
                    zoomType: 'xy'
                },
                title: {
                    text: 'Yearly Emotional Graph'
                },
                subtitle: {
                    text: 'Current Year'
                },
                xAxis: {
                    categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
                        'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
                },
                //yAxis: {
                //    title: {
                //        text: 'Percentage %'
                //    }
                //},
                series: data
            });
        },
        error: function(data) {
            console.error(data);
        }
    });
    /*var myChart = Highcharts.chart('chart_full', {
     chart: {
     type: 'line'
     },
     title: {
     text: 'Yearly Emotional Graph'
     },
     subtitle: {
     text: 'Current Year'
     },
     xAxis: {
     categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
     'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
     },
     yAxis: {
     title: {
     text: 'Fruit eaten'
     }
     },
     series: [{
     name: 'Jane',
     data: [1, 0, 4, 9]
     }, {
     name: 'John',
     data: [5, 7, 3]
     }]
     });*/
}