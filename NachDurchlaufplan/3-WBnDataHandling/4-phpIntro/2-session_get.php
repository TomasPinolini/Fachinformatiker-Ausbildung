<?php
// Start the session
session_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Get Session</title>
</head>
<body>
    <h1>Retrieve Session Variables</h1>
    <?php
    if (isset($_SESSION['username']) && isset($_SESSION['email'])) {
        echo "Welcome, " . $_SESSION['username'] . "!<br>";
        echo "Your email is: " . $_SESSION['email'] . "<br>";
    } else {
        echo "No session variables are set.<br>";
    }
    ?>
    <a href="2-session_destroy.php">Logout</a>
</body>
</html>