<?php
session_start();
require '1-dbconnection.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $action = $_POST['action'];
    $username = $_POST['username'];
    $password = $_POST['password'];

    if ($action === 'register') {
        $query = "SELECT * FROM users WHERE username = '$username'";
        $result = mysqli_query($mysqli, $query);

        if (mysqli_num_rows($result) > 0) {
            echo "Username already exists. Choose another one.";
        } else {
            $query = "INSERT INTO users (username, password) VALUES ('$username', '$password')";
            if (mysqli_query($mysqli, $query)) {
                echo "Registration successful. Please log in.";
            } else {
                echo "Error during registration.";
            }
        }
    } elseif ($action === 'login') {
        $query = "SELECT * FROM users WHERE username = '$username'";
        $result = mysqli_query($mysqli, $query);
        $user = mysqli_fetch_assoc($result);
        if($user['username'] && $password == $user['password']){
            $_SESSION['user_id'] = $user['user_id'];
            $_SESSION['username'] = $user['username'];
            header("Location: 4-menu.php");
            exit();
        } else {
            echo "Invalid username or password.";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login or Register</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="bg-light text-dark">
    <div class="container my-4">
        <hr>
        <div class="row">
            <!-- Login Form -->
            <div class="col-md-6">
                <h3>Login</h3>
                <form method="POST">
                    <input type="hidden" name="action" value="login">
                    <div class="mb-3">
                        <label for="loginUsername" class="form-label">Username</label>
                        <input type="text" name="username" id="loginUsername" class="form-control" required>
                    </div>
                    <div class="mb-3">
                        <label for="loginPassword" class="form-label">Password</label>
                        <input type="password" name="password" id="loginPassword" class="form-control" required>
                    </div>
                    <button type="submit" class="btn btn-primary">Login</button>
                </form>
            </div>

            <!-- Register Form -->
            <div class="col-md-6">
                <h3>Register</h3>
                <form method="POST">
                    <input type="hidden" name="action" value="register">
                    <div class="mb-3">
                        <label for="registerUsername" class="form-label">Username</label>
                        <input type="text" name="username" id="registerUsername" class="form-control" required>
                    </div>
                    <div class="mb-3">
                        <label for="registerPassword" class="form-label">Password</label>
                        <input type="password" name="password" id="registerPassword" class="form-control" required>
                    </div>
                    <button type="submit" class="btn btn-success">Register</button>
                </form>
            </div>
        </div>
    </div>
</body>
</html>
