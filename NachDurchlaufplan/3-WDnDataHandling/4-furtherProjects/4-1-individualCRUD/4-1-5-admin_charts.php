<?php
    session_start();  
    // include("../1-dbconnection.php");
    $mysqli = require __DIR__ . "../4-1-1-dbconnection.php";
    if (!$mysqli) {die("Database connection failed: " . mysqli_connect_error());}
    $idAdmin = $_SESSION["id_users"];

    $purPerMonth = [];
    for($i = 1; $i <= 12; $i++){
        $month = str_pad($i, 2, '0', STR_PAD_LEFT);
        $sqlPur = "SELECT COUNT(*) AS count 
        FROM purchases 
        WHERE purchase_date BETWEEN '2024-$month-01' AND LAST_DAY('2024-$month-01')";
        $purchases = mysqli_query($mysqli, $sqlPur);
        if($purchases){
            $row = mysqli_fetch_assoc($purchases); 
            $count = $row['count']; 
            $purPerMonth[] = $count;
        }else {
            echo "Error: " . mysqli_error($mysqli);
        }
    }
    
    print_r($purPerMonth);
    mysqli_close($mysqli);

    $jsArray = json_encode($purPerMonth);

    $jsContent = "const purchaseCounts = $jsArray;";

    $jsFilePath = "/4-1-6-purchaseData.js";
    if (file_put_contents($jsFilePath, $jsContent)) {
        echo "JavaScript file has been updated: $jsFilePath";
    } else {
        echo "Failed to write to the JavaScript file.";
    }

?>

<!DOCTYPE html>
<html>
<head>
    <title>Homepage</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">My Website</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#about">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#services">Services</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#contact">Contact</a>
                    </li>
                </ul>
            </div>
            <h1 class="text-white">Welcome, <?= htmlspecialchars($_SESSION['email']) ?></h1>
        </div>
    </nav>

    <!-- Buttons -->
    <div class="container mt-5">
        <a href="5-admin_create.php" class="btn btn-primary">Create a product</a>
        <a href="5-admin_update.php" class="btn btn-primary">Update products state</a>
    </div>

    <!-- Main container -->
    <div class="container mt-5">
    
    <script>
        const { AgCharts } = agCharts;

        function formatNumber(value) {
        value /= 1000_000;
        return `${Math.floor(value)}M`;
        }

        const options = {
        container: document.getElementById("myChart"),
        data: getData(),
        title: {
            text: "Total Visitors to Museums and Galleries",
        },
        footnote: {
            text: "Source: Department for Digital, Culture, Media & Sport",
        },
        series: [
            {
            type: "bar",
            xKey: "year",
            yKey: "visitors",
            label: {
                formatter: ({ value }) => formatNumber(value),
            },
            },
        ],
        axes: [
            {
            type: "category",
            position: "bottom",
            title: {
                text: "Year",
            },
            },
            {
            type: "number",
            position: "left",
            title: {
                text: "Total Visitors",
            },
            label: {
                formatter: ({ value }) => formatNumber(value),
            },
            },
        ],
        };

        AgCharts.create(options);
    </script>

    </div>
    <!-- Log out button -->
    <div class="container mt-5">
        <a href="4-logout.php" class="btn btn-danger">Logout</a>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>

<?php
    

?>
