<?php
    session_start();
    $idClient = $_SESSION["id_users"];
    include("../7-dbconnection.php"); 

    $sqlPr = "SELECT * FROM products WHERE state = '1'";
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
            <h1 style="color: white;">Welcome, <?= htmlspecialchars($_SESSION['email'])?></h1>
        </div>
    </nav>
    <!-- Main Content -->
    <div class="container mt-5">
        <h3>Update Product State</h3>
        <form action="" method="post">
            <div class="table-responsive">
                <table class="table table-bordered table-striped">
                    <thead class="table-dark">
                        <tr>
                            <th style="width: 10%;">Select</th>
                            <th style="width: 80%;">Description</th>
                            <th style="width: 20%;">Price</th>
                        </tr>    
                    </thead>
                    <tbody>
                        <?php foreach ($prods as $prod): ?>
                            <tr>
                                <td style="width: 10%;">
                                    <input type="checkbox" value="<?= $prod["id_products"]?>" name="purchases[]" />
                                </td>
                                <td style="width: 80%;"><?= htmlspecialchars($prod["description"]) ?></td>
                                <td style="width: 20%;"><?= htmlspecialchars($prod["price"]) ?></td>
                            </tr>
                        <?php endforeach; ?>
                    </tbody>
                </table>
            </div>
            <button type="submit" value="SubmitPur" name="SubmitPur" class="btn btn-primary">Purchase</button>
        </form>
    </div>

    <a href="../15-logout.php" class="btn btn-danger">Logout</a>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>

<?php
    if (isset($_POST["SubmitPur"])) {
        foreach ($_POST["purchases"] as $idP) {
            $sqlNewPur = "INSERT into purchases (id_users, id_product) VALUES ('$idClient', '$idP')";
            mysqli_query($mysqli, $sqlNewPur);
        }
    }
?>