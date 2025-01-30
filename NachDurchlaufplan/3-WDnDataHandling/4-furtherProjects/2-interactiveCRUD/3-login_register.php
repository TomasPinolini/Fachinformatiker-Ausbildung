<?php
session_start();
require '4-2-1-dbconnection.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = $_POST['username'];
    $password = $_POST['password'];
    $action = $_POST['action'];

    // Admin connection to manage MySQL user accounts
    $adminConn = connect('root', ''); // Use your MySQL admin credentials

    if ($action === 'register') {
        // Sanitize input
        $username = $adminConn->real_escape_string($username);
        $password = $adminConn->real_escape_string($password);

        // Check if MySQL user already exists
        $stmt = $adminConn->prepare("SELECT User FROM mysql.user WHERE User = ?");
        $stmt->bind_param("s", $username);
        $stmt->execute();
        $result = $stmt->get_result();

        if ($result->num_rows > 0) {
            echo "Username already exists as a MySQL user. Choose another one.";
        } else {
            // Create MySQL user
            $createUserQuery = "CREATE USER '$username'@'localhost' IDENTIFIED BY '$password'";
            $adminConn->query($createUserQuery) === TRUE;
            $grantPrivilegesQuery = "GRANT ALL PRIVILEGES ON multiuser_crud.* TO '$username'@'localhost'";
            $adminConn->query($grantPrivilegesQuery) === TRUE;
            
            // Register the user in the application database (users table)
            $stmt = $adminConn->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
            $stmt->bind_param("ss", $username, $password);
            if ($stmt->execute()) {
                echo "Registration successful. Please log in.";
            } else {
                echo "Error during registration: " . $stmt->error;
            }
        }
    } elseif ($action === 'login') {
        // Attempt to connect using user-provided credentials
        try {
            $userConn = connect($username, $password); // Dynamic credentials
            $_SESSION['db_user'] = $username;
            $_SESSION['db_pass'] = $password;

            // Check if user exists in the application database
            $stmt = $userConn->prepare("SELECT * FROM users WHERE username = ?");
            $stmt->bind_param("s", $username);
            $stmt->execute();
            $result = $stmt->get_result();
            $user = $result->fetch_assoc();

            if ($user) {
                $_SESSION['user_id'] = $user['user_id'];
                $_SESSION['username'] = $user['username'];
                header("Location: 4-2-4-menu.php");
                exit();
            } else {
                echo "Invalid credentials or user not found.";
            }
        } catch (Exception $e) {
            echo "Login failed: " . $e->getMessage();
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
