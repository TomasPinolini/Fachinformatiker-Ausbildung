<?php
$login_invalid = false;
$dueno_no_ap = false;
$validated = true;
$error_message = '';
$registration_error = '';
$mysqli = require __DIR__ . "/7-dbconnection.php";

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    if (isset($_POST["login"])) {
        $postemail = $mysqli->real_escape_string($_POST["email"]);
        $postpassword = $mysqli->real_escape_string($_POST["password"]);

        $sql = "SELECT * FROM users WHERE email = ?";
        $stmt = $mysqli->prepare($sql);
        $stmt->bind_param("s", $postemail);
        $stmt->execute();
        $result = $stmt->get_result();
        
        if ($result && $result->num_rows > 0) {
            $user = $result->fetch_assoc();
            if ($postpassword === $user["password"]) {
                $_SESSION = $user;
                    header("Location: 9-homepage_dbconnection.php");
                    exit;
                }
        }else {
            $login_invalid = true;
            $error_message = "Usuario o contraseña incorrecto, intente de nuevo.";
        }
    } elseif (isset($_POST["register"])) {
        $email = filter_input(INPUT_POST, "email");
        $birthdate = filter_input(INPUT_POST, "birthdate");
        $password = filter_input(INPUT_POST, "password");
        echo $email, $birthdate, $password;

        if (!$mysqli) {
            die("Failed to connect to MySQL: " . mysqli_connect_error());
        }

        $sql = "INSERT INTO users (email, birthdate, password) VALUES (?, ?, ?)";

        $stmt = $mysqli->stmt_init();

        if (!$stmt->prepare($sql)) {
            die("SQL error: " . $mysqli->error);
        }

        $stmt->bind_param("sss", $email, $birthdate, $password,);

        if ($stmt->execute()) {
            header("Location: 9-homepage_dbconnection.php");
        } else {
            if ($mysqli->errno === 1062) {
                die("Email already taken.");
            } else {
                die("SQL error: " . $mysqli->error);
            }
        }
    }
}
    
?>
<!DOCTYPE html>
<html>
<head>
    <title>Login and Registration</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <!-- Login Section -->
        <section id="login" class="mb-5">
            <h1 class="text-center">Login Page</h1>
            <form class="mt-4" method="POST">
                <div class="mb-3">
                    <label for="email" class="form-label">Email:</label>
                    <input type="email" id="email" name="email" class="form-control" placeholder="Enter your email">
                </div>
                <div class="mb-3">
                    <label for="password" class="form-label">Password:</label>
                    <input type="password" id="password" name="password" class="form-control" placeholder="Enter your password">
                </div>
                <button type="submit" name="login" value="Sign in" class="btn btn-primary w-100">Login</button>
            </form>
        </section>

        <!-- Registration Section -->
        <section id="registration">
            <h1 class="text-center">Registration Page</h1>
            <form class="mt-4" method="POST">
                <div class="mb-3">
                    <label for="email" class="form-label">Email:</label>
                    <input type="email" id="email" name="email" class="form-control" placeholder="Enter your email">
                </div>
                <div class="mb-3">
                    <label for="birth" class="form-label">Birthdate:</label>
                    <input type="date" id="birthdate" name="birthdate" class="form-control" placeholder="Enter your birthdate">
                </div>
                <div class="mb-3">
                    <label for="password" class="form-label">Password:</label>
                    <input type="password" id="password" name="password" class="form-control" placeholder="Enter your password">
                </div>
                <button type="submit" name="register" value="Ingresar" class="btn btn-success w-100">Register</button>
            </form>
        </section>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>