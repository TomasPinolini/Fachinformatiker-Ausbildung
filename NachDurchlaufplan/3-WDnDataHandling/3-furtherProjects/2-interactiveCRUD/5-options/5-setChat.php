<?php
session_start();

// Ensure chat_id is provided in the URL
if (isset($_GET['chat_id'])) {
    $_SESSION["chat_id"] = $_GET['chat_id']; // Store chat ID in session
    header("Location: 4-chat.php"); // Redirect to chat page
    exit();
} else {
    echo "Invalid chat selection.";
    exit();
}
?>
