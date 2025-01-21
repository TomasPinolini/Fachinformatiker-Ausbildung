<?php
session_start();
require '../1-dbconnection.php';

// Check if the user is logged in and a chat is selected
if (!isset($_SESSION['user_id']) || !isset($_SESSION['chat_id'])) {
    die("Invalid access. Please select a chat.");
}

$user_id = $_SESSION['user_id'];
$chat_id = $_SESSION['chat_id'];

// Fetch the chat name using the chat_id
$sqlChat = "SELECT chat_name FROM chats WHERE chat_id = $chat_id";
$result = mysqli_query($mysqli, $sqlChat);

if ($result && mysqli_num_rows($result) > 0) {
    $chat = mysqli_fetch_assoc($result);
    $chat_name = htmlspecialchars($chat['chat_name']); // Sanitize chat name
} else {
    die("Chat not found.");
}

// Fetch chat messages
$sqlMessages = "SELECT m.content, m.sent_at, u.username 
                FROM messages m
                JOIN users u ON m.sender_id = u.user_id
                WHERE m.chat_id = $chat_id
                ORDER BY m.sent_at ASC";
$messages = mysqli_query($mysqli, $sqlMessages);

// Handle message submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $content = htmlspecialchars($_POST['content']);
    $sqlInsert = "INSERT INTO messages (chat_id, sender_id, content) VALUES ($chat_id, $user_id, '$content')";
    mysqli_query($mysqli, $sqlInsert);

    // Refresh the page to show the new message
    header("Location: " . $_SERVER['PHP_SELF']);
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?= $chat_name ?> - Chat Room</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center"><?= $chat_name ?></h1>
        <div class="border p-3 mb-4" style="height: 300px; overflow-y: auto;">
            <?php if (mysqli_num_rows($messages) > 0): ?>
                <?php while ($msg = mysqli_fetch_assoc($messages)): ?>
                    <p>
                        <strong><?= htmlspecialchars($msg['username']) ?></strong>: 
                        <?= htmlspecialchars($msg['content']) ?>
                        <small class="text-muted"><?= $msg['sent_at'] ?></small>
                    </p>
                <?php endwhile; ?>
            <?php else: ?>
                <p class="text-muted">No messages yet. Be the first to say something!</p>
            <?php endif; ?>
        </div>

        <!-- Message Input Form -->
        <form method="POST">
            <div class="mb-3">
                <textarea name="content" class="form-control" rows="3" placeholder="Type your message..." required></textarea>
            </div>
            <button type="submit" class="btn btn-success">Send</button>
        </form>
        <div class="mt-3">
            <a href="7-viewChats.php" class="btn btn-secondary">Back to Chats</a>
        </div>
    </div>
</body>
</html>
