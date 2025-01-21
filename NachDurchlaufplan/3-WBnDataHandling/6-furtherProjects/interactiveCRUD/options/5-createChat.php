<?php
session_start();
require '../1-dbconnection.php'; 
$message = "";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $chat_name = htmlspecialchars($_POST['chat_name']);
    $created_by = $_SESSION['user_id']; // Get the user ID from the session

    $sql = "INSERT INTO chats (chat_name, created_by) VALUES ('$chat_name', $created_by)";
    if (mysqli_query($mysqli, $sql)) {
        $message = "Chat created successfully!";
    } else {
        $message = "Error creating chat: " . mysqli_error($conn);
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

        <?php if (!empty($message)): ?>
            <div class="alert alert-info mt-3"><?= htmlspecialchars($message) ?></div>
        <?php endif; ?>

        <div class="mt-3">
            <a href="../4-menu.php" class="btn btn-dark">Back to Menu</a>
        </div>
    </div>
</body>
</html>