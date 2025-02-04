<?php
    session_start();  
    $mysqli = require __DIR__ . "../1-dbconnection.php";
    if (!$mysqli) {die("Database connection failed: " . mysqli_connect_error());}
    $idAdmin = $_SESSION["id_users"];

    $sqlPr = "SELECT * FROM products WHERE id_admin = '$idAdmin'";
    $prods = mysqli_query($mysqli, $sqlPr);
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
        <a href="5-admin_update.php" class="btn btn-secondary">Update products state</a>
    </div>

    <!-- Main container -->
    <div class="container mt-5">
        <h3>New Product</h3>
        <form action="" method="POST" class="mb-5">
            <div class="mb-3">
                <label for="descPr" class="form-label">Describe the product:</label>
                <input type="text" name="descPr" id="descPr" class="form-control" required />
            </div>
            <div class="mb-3">
                <label for="pricePr" class="form-label">Insert the product's price:</label>
                <input type="text" name="pricePr" id="pricePr" class="form-control" required />
            </div>
            <button type="submit" value="SubmitPr" name="SubmitPr" class="btn btn-primary">Add Product</button>
        </form>
    </div>

    <!-- Log out button -->
    <div class="container mt-5">
        <a href="4-logout.php" class="btn btn-danger">Logout</a>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>

<?php
    if (isset($_POST["SubmitPr"])) {
        $descPr = filter_input(INPUT_POST, "descPr", FILTER_SANITIZE_STRING);
        $pricePr = filter_input(INPUT_POST, "pricePr", FILTER_VALIDATE_FLOAT);

        if (empty($descPr)) {
            echo "<div class='alert alert-danger mt-3'>A description for the product is necessary.</div>";
        } elseif ($pricePr === false) {
            echo "<div class='alert alert-danger mt-3'>The price must be a valid number.</div>";
        } else {
            $sql = "INSERT INTO products (description, price, id_admin, state) 
                    VALUES ('$descPr', '$pricePr', '$idAdmin', '1')";
            if (mysqli_query($mysqli, $sql)) {
                echo "<div class='alert alert-success mt-3'>Product added successfully.</div>";
            } else {
                echo "<div class='alert alert-danger mt-3'>Error: " . mysqli_error($mysqli) . "</div>";
            }
        }
    }

    if (isset($_POST["SubmitSt"])) {
        foreach ($_POST["changes"] as $value) {
            list($state, $id) = explode(" ", $value);
            $newSt = ($state === '1') ? '0' : '1';
            $sqlUpdateState = "UPDATE products SET state = '$newSt' WHERE id_products = '$id'";
            mysqli_query($mysqli, $sqlUpdateState);
        }
    }

?>
