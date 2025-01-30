<?php
// Start the session
session_start();

// Destroy the session
session_destroy();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Session Destroy</title>
</head>
<body>
    <h1>Session Destroyed</h1>
    <p>You have successfully logged out.</p>
    <a href="2-2-session_start.php">Start a New Session</a>
</body>
</html>