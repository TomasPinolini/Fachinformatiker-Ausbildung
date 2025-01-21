<?php
session_start();
require '1-dbconnection.php';

// Check if the user is logged in
if (!isset($_SESSION['user_id'])) {
    die("You must be logged in to access the menu.");
}

$user_id = $_SESSION['user_id'];

// Fetch chats the user belongs to
$sqlChats = "SELECT c.chat_id, c.chat_name 
             FROM chats c
             JOIN chat_participants cp ON c.chat_id = cp.chat_id
             WHERE cp.user_id = $user_id";
$chats = mysqli_query($mysqli, $sqlChats);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Menu</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="bg-light text-dark">
    <div class="container mt-5">
        <h1 class="text-center">Menu</h1>
        
        <!-- Existing Options -->
        <div class="mt-4">
            <a href="options/5-createChat.php" class="btn btn-primary d-block mb-2">Create Chat</a>
            <a href="options/6-joinChats.php" class="btn btn-primary d-block mb-2">Join Chats</a>
            <a href="options/7-viewChats.php" class="btn btn-primary d-block mb-2">View My Chats</a>
        </div>
    </div>
    <a href="10-logout.php" class="btn btn-danger">Logout</a>
</body>
</html>
