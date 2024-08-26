<!DOCTYPE html>
<html>
<head>
    <title>User Roles Report</title>
    <script src="https://cdn.jsdelivr.net/npm/apexcharts"></script>
</head>
<body>

<h2>User Roles Report</h2>
<div id="chart"></div>

<script>
// Fetch the JSON data from the file
fetch('Report.json')
    .then(response => response.json())
    .then(data => {
        // Initialize an empty object to store the role counts
        var roleCounts = {};

        // Loop through the data to count the occurrences of each role
        data.forEach(function(item) {
            var role = item.role_name;
            if (roleCounts[role]) {
                roleCounts[role]++;
            } else {
                roleCounts[role] = 1;
            }
        });

        // Extract roles and counts into separate arrays for ApexCharts
        var roles = Object.keys(roleCounts);  // Extract role names (e.g., ['Noob', 'Admin', ...])
        var userCounts = Object.values(roleCounts);  // Extract counts (e.g., [1, 1, ...])

        console.log('Roles:', roles);  // Debugging: Log roles
        console.log('User Counts:', userCounts);  // Debugging: Log user counts

        // Configure the ApexChart
        var options = {
            chart: {
                type: 'bar'
            },
            series: [{
                name: 'Users',
                data: userCounts
            }],
            xaxis: {
                categories: roles
            },
            title: {
                text: 'Number of Users per Role'
            }
        };

        // Render the chart
        var chart = new ApexCharts(document.querySelector("#chart"), options);
        chart.render();
    })
    .catch(error => console.error('Error loading JSON:', error));
</script>

</body>
</html>