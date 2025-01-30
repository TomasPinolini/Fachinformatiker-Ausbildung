<?php
// Start the session
session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Set session variables
    $_SESSION['username'] = htmlspecialchars($_POST['username']);
    $_SESSION['email'] = htmlspecialchars($_POST['email']);
    echo "Session variables are set!<br>";
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Session Start</title>
</head>
<body>
    <h1>Start Session</h1>
    <form method="POST">
        Username: <input type="text" name="username" required><br>
        Email: <input type="email" name="email" required><br>
        <button type="submit">Submit</button>
    </form>
    <a href="2-3-session_get.php">Go to Next Page</a>
</body>
</html>
