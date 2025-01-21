<?php
session_start();
require '../1-dbconnection.php';

// Check if the user is logged in
if (!isset($_SESSION['user_id'])) {
    die("You must be logged in to view chats.");
}

$user_id = $_SESSION['user_id'];

// Fetch chats the user is part of
$joinedChatsQuery = "SELECT c.chat_id, c.chat_name 
                     FROM chats c
                     JOIN chat_participants cp ON c.chat_id = cp.chat_id
                     WHERE cp.user_id = $user_id";
$joinedChatsResult = mysqli_query($mysqli, $joinedChatsQuery);

// Fetch chats the user is NOT part of
$otherChatsQuery = "SELECT c.chat_id, c.chat_name 
                    FROM chats c
                    WHERE c.chat_id NOT IN (
                        SELECT cp.chat_id 
                        FROM chat_participants cp 
                        WHERE cp.user_id = $user_id
                    )";
$otherChatsResult = mysqli_query($mysqli, $otherChatsQuery);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>View Chats</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="bg-light text-dark">
    <div class="container mt-5">
        <h1 class="text-center">Chats</h1>

        <!-- Section: Chats User is Part Of -->
        <h3 class="mt-4">Chats You Are Part Of</h3>
        <?php if (mysqli_num_rows($joinedChatsResult) > 0): ?>
            <ul class="list-group">
                <?php while ($chat = mysqli_fetch_assoc($joinedChatsResult)): ?>
                    <li class="list-group-item">
                        <?= htmlspecialchars($chat['chat_name']) ?>
                    </li>
                <?php endwhile; ?>
            </ul>
        <?php else: ?>
            <p class="text-muted">You are not part of any chats yet.</p>
        <?php endif; ?>

        <!-- Section: Chats User is NOT Part Of -->
        <h3 class="mt-4">Other Chats</h3>
        <?php if (mysqli_num_rows($otherChatsResult) > 0): ?>
            <ul class="list-group">
                <?php while ($chat = mysqli_fetch_assoc($otherChatsResult)): ?>
                    <li class="list-group-item">
                        <?= htmlspecialchars($chat['chat_name']) ?>
                        <a href="8-chat.php?chat_id=<?= $chat['chat_id'] ?>" class="btn btn-sm btn-primary float-end">Join</a>
                    </li>
                <?php endwhile; ?>
            </ul>
        <?php else: ?>
            <p class="text-muted">No other chats available.</p>
        <?php endif; ?>

        <div class="mt-3">
            <a href="../4-menu.php" class="btn btn-dark">Back to Menu</a>
        </div>
    </div>
</body>
</html>
