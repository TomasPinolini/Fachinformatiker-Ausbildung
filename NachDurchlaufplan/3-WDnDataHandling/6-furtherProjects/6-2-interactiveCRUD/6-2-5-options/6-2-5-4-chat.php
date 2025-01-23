<?php
session_start();
require '../1-dbconnection.php';

// Check if the user is logged in and a chat is selected
if (!isset($_SESSION['user_id']) || !isset($_SESSION['chat_id']) || !isset($_SESSION['db_user']) || !isset($_SESSION['db_pass'])) {
    die("Invalid access. Please log in and select a chat.");
}

// Establish a database connection using the logged-in user's credentials
$mysqli = connect($_SESSION['db_user'], $_SESSION['db_pass']);
$user_id = $_SESSION['user_id'];
$chat_id = $_SESSION['chat_id'];

// Fetch the chat name using the chat_id
$sqlChat = "SELECT chat_name FROM chats WHERE chat_id = ?";
$stmtChat = $mysqli->prepare($sqlChat);
$stmtChat->bind_param("i", $chat_id);
$stmtChat->execute();
$resultChat = $stmtChat->get_result();

if ($resultChat && $resultChat->num_rows > 0) {
    $chat = $resultChat->fetch_assoc();
    $chat_name = htmlspecialchars($chat['chat_name']); // Sanitize chat name
} else {
    die("Chat not found.");
}
$stmtChat->close();

// Fetch chat messages
$sqlMessages = "SELECT m.content, m.sent_at, u.username 
                FROM messages m
                JOIN users u ON m.sender_id = u.user_id
                WHERE m.chat_id = ?
                ORDER BY m.sent_at ASC";
$stmtMessages = $mysqli->prepare($sqlMessages);
$stmtMessages->bind_param("i", $chat_id);
$stmtMessages->execute();
$resultMessages = $stmtMessages->get_result();
$messages = $resultMessages->fetch_all(MYSQLI_ASSOC);
$stmtMessages->close();

// Initialize warning message
$warningMessage = null;

// Handle message submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['content']) && trim($_POST['content']) !== '') { // Check if content is set and not empty
        $content = htmlspecialchars(trim($_POST['content'])); // Sanitize and trim input

        // Insert the message into the database
        $sqlInsert = "INSERT INTO messages (chat_id, sender_id, content) VALUES (?, ?, ?)";
        $stmtInsert = $mysqli->prepare($sqlInsert);
        $stmtInsert->bind_param("iis", $chat_id, $user_id, $content);
        $stmtInsert->execute();
        $stmtInsert->close();

        // Refresh the page to show the new message
        header("Location: " . $_SERVER['PHP_SELF']);
        exit;
    } else {
        // Set a warning message for empty input
        $warningMessage = "Message content cannot be empty.";
    }
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

        <!-- Display Warning Message -->
        <?php if (isset($warningMessage)): ?>
            <div class="alert alert-warning"><?= htmlspecialchars($warningMessage) ?></div>
        <?php endif; ?>

        <!-- Chat Messages -->
        <div class="border p-3 mb-4" style="height: 300px; overflow-y: auto;">
            <?php if (!empty($messages)): ?>
                <?php foreach ($messages as $msg): ?>
                    <p>
                        <strong><?= htmlspecialchars($msg['username']) ?></strong>: 
                        <?= htmlspecialchars($msg['content']) ?>
                        <small class="text-muted"><?= htmlspecialchars($msg['sent_at']) ?></small>
                    </p>
                <?php endforeach; ?>
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
