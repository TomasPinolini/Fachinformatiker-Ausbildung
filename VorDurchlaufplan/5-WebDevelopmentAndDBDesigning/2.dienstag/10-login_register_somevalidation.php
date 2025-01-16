<?php
$login_invalid = false;
$dueno_no_ap = false;
$validated = true;
$error_message = '';
$registration_error = '';
$mysqli = require __DIR__ . "/7-dbconnection.php";

function isValidPassword($password) {
    return preg_match('/[A-Za-z]/', $password) && preg_match('/[0-9]/', $password);
}

function isValidEmail($email) {
    return filter_var($email, FILTER_VALIDATE_EMAIL);
}

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    if (isset($_POST["login"])) {
        $postemail = $mysqli->real_escape_string(trim($_POST["email"]));
        $postpassword = $mysqli->real_escape_string(trim($_POST["password"]));

        if (empty($postemail) || empty($postpassword)) {
            $login_invalid = true;
            $error_message = "All fields are required.";
        } elseif (!isValidEmail($postemail)) {
            $login_invalid = true;
            $error_message = "Invalid email format.";
        } else {
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
                } else {
                    $login_invalid = true;
                    $error_message = "Incorrect email or password.";
                }
            } else {
                $login_invalid = true;
                $error_message = "User does not exist.";
            }
        }
    } elseif (isset($_POST["register"])) {
        $email = trim(filter_input(INPUT_POST, "email"));
        $birthdate = trim(filter_input(INPUT_POST, "birthdate"));
        $password = trim(filter_input(INPUT_POST, "password"));

        if (empty($email) || empty($birthdate) || empty($password)) {
            $registration_error = "All fields are required.";
        } elseif (!isValidEmail($email)) {
            $registration_error = "Invalid email format.";
        } elseif (!isValidPassword($password)) {
            $registration_error = "Password must include both letters and numbers.";
        } else {
            $sql = "INSERT INTO users (email, birthdate, password) VALUES (?, ?, ?)";
            $stmt = $mysqli->stmt_init();

            if (!$stmt->prepare($sql)) {
                die("SQL error: " . $mysqli->error);
            }

            $stmt->bind_param("sss", $email, $birthdate, $password);

            if ($stmt->execute()) {
                header("Location: 9-homepage_dbconnection.php");
                exit;
            } else {
                if ($mysqli->errno === 1062) {
                    $registration_error = "Email already taken.";
                } else {
                    die("SQL error: " . $mysqli->error);
                }
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
            <?php if ($login_invalid): ?>
                <div class="alert alert-danger"><?php echo htmlspecialchars($error_message); ?></div>
            <?php endif; ?>
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
            <?php if (!empty($registration_error)): ?>
                <div class="alert alert-danger"><?php echo htmlspecialchars($registration_error); ?></div>
            <?php endif; ?>
            <form class="mt-4" method="POST">
                <div class="mb-3">
                    <label for="email" class="form-label">Email:</label>
                    <input type="email" id="email" name="email" class="form-control" placeholder="Enter your email">
                </div>
                <div class="mb-3">
                    <label for="birth" class="form-label">Birthdate:</label>
                    <input type="date" id="birthdate" name="birthdate" class="form-control">
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
