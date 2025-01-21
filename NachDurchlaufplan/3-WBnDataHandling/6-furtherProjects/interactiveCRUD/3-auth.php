<?php
session_start();
require 'dbconnection.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $action = $_POST['action']; // Either 'login' or 'register'

    if ($action === 'register') {
        // Registration logic
        $username = htmlspecialchars($_POST['username']);
        $password = htmlspecialchars($_POST['password']);
        $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

        // Check if username exists
        $stmt = $conn->prepare("SELECT * FROM users WHERE username = ?");
        $stmt->bind_param("s", $username);
        $stmt->execute();
        $result = $stmt->get_result();

        if ($result->num_rows > 0) {
            echo "Username already exists. Please choose another one.";
        } else {
            // Insert new user
            $stmt = $conn->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
            $stmt->bind_param("ss", $username, $hashedPassword);
            if ($stmt->execute()) {
                echo "Registration successful. Please log in.";
            } else {
                echo "Error during registration: " . $stmt->error;
            }
        }
    } elseif ($action === 'login') {
        // Login logic
        $username = htmlspecialchars($_POST['username']);
        $password = htmlspecialchars($_POST['password']);

        // Check if user exists
        $stmt = $conn->prepare("SELECT * FROM users WHERE username = ?");
        $stmt->bind_param("s", $username);
        $stmt->execute();
        $result = $stmt->get_result();
        $user = $result->fetch_assoc();

        if ($user && password_verify($password, $user['password'])) {
            $_SESSION['user_id'] = $user['id_user'];
            $_SESSION['username'] = $user['username'];
            header("Location: chatroom.php");
            exit();
        } else {
            echo "Invalid credentials.";
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
        <h1 class="text-center">Login or Register</h1>
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
