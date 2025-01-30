<?php
session_start();
require '../4-2-1-dbconnection.php'; 
$message = "";

// Check if the user is logged in
if (!isset($_SESSION['user_id']) || !isset($_SESSION['db_user']) || !isset($_SESSION['db_pass'])) {
    die("You must be logged in to create a chat.");
}

// Establish a database connection using the logged-in user's credentials
$mysqli = connect($_SESSION['db_user'], $_SESSION['db_pass']);

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize chat name
    $chat_name = htmlspecialchars($_POST['chat_name']);
    $created_by = $_SESSION['user_id']; // Get the user ID from the session

    // Use prepared statement to insert the chat
    $sql = "INSERT INTO chats (chat_name, created_by) VALUES (?, ?)";
    $stmt = $mysqli->prepare($sql);

    if ($stmt) {
        $stmt->bind_param("si", $chat_name, $created_by); // Bind parameters
        if ($stmt->execute()) {
            $message = "Chat created successfully!";
        } else {
            $message = "Error creating chat: " . $stmt->error;
        }
        $stmt->close();
    } else {
        $message = "Error preparing statement: " . $mysqli->error;
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Chat</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="bg-light text-dark">
    <div class="container mt-5">
        <h1 class="text-center">Create a Chat</h1>
        <form method="POST" class="mt-4">
            <div class="mb-3">
                <label for="chat_name" class="form-label">Chat Name</label>
                <input type="text" name="chat_name" id="chat_name" class="form-control" required>
            </div>
            <button type="submit" class="btn btn-success mt-3">Create Chat</button>
        </form>

        <!-- Show Success/Error Message -->
        <?php if (!empty($message)): ?>
            <div class="alert alert-info mt-3"><?= htmlspecialchars($message) ?></div>
        <?php endif; ?>

        <div class="mt-3">
            <a href="../4-2-4-menu.php" class="btn btn-dark">Back to Menu</a>
        </div>
    </div>
</body>
</html>
