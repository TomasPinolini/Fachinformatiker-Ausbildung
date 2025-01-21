<?php
session_start();
require 'dbconnection.php';

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit();
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat Room</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container my-4">
        <h1>Welcome, <?= $_SESSION['username'] ?>!</h1>
        <div id="chat-box" class="border p-3 mb-3" style="height: 300px; overflow-y: scroll;">
            <!-- Messages will be dynamically loaded here -->
        </div>
        <form id="chat-form">
            <input type="text" id="message" class="form-control mb-2" placeholder="Type your message..." required>
            <button type="submit" class="btn btn-primary">Send</button>
        </form>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/jquery/dist/jquery.min.js"></script>
    <script>
        // Load messages dynamically
        function loadMessages() {
            $.get("fetch_messages.php", function(data) {
                $("#chat-box").html(data);
                $("#chat-box").scrollTop($("#chat-box")[0].scrollHeight); // Auto-scroll to the bottom
            });
        }

        // Send a new message
        $("#chat-form").submit(function(e) {
            e.preventDefault();
            const message = $("#message").val();
            $.post("send_message.php", { message: message }, function() {
                $("#message").val("");
                loadMessages();
            });
        });

        // Auto-refresh messages every 2 seconds
        setInterval(loadMessages, 2000);
    </script>
</body>
</html>
