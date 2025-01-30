<?php
    session_start();
    require '1-dbconnection.php';

    $_SESSION['chat_id'] = "";

    // Check if the user is logged in
    if (!isset($_SESSION['user_id']) || !isset($_SESSION['db_user']) || !isset($_SESSION['db_pass'])) {
        die("You must be logged in to access the menu.");
    }

    // Establish a database connection using the logged-in user's credentials
    $mysqli = connect($_SESSION['db_user'], $_SESSION['db_pass']);

    // Fetch user ID and username
    $user_id = $_SESSION['user_id'];
    $username = $_SESSION['username'];

    // Fetch chats the user belongs to
    $sqlChats = "SELECT c.chat_id, c.chat_name 
                FROM chats c
                JOIN chat_participants cp ON c.chat_id = cp.chat_id
                WHERE cp.user_id = ?";
    $stmt = $mysqli->prepare($sqlChats);
    $stmt->bind_param("i", $user_id);
    $stmt->execute();
    $result = $stmt->get_result();
    $chats = $result->fetch_all(MYSQLI_ASSOC);
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
        <h1 class="text-center">Welcome, <?= htmlspecialchars($username) ?></h1>

        <!-- Display Chats -->
        <h3 class="mt-4">Your Chats</h3>
        <?php if (!empty($chats)): ?>
            <ul class="list-group mb-4">
                <?php foreach ($chats as $chat): ?>
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        <?= htmlspecialchars($chat['chat_name']) ?>
                        <a href="5-options/5-setChat.php?chat_id=<?= htmlspecialchars($chat['chat_id']) ?>" class="btn btn-sm btn-primary">Enter</a>
                    </li>
                <?php endforeach; ?>
            </ul>
        <?php else: ?>
            <p class="text-muted">You are not part of any chats yet.</p>
        <?php endif; ?>

        <!-- Existing Options -->
        <div class="mt-4">
            <a href="5-options/1-createChat.php" class="btn btn-primary d-block mb-2">Create Chat</a>
            <a href="5-options/2-joinChats.php" class="btn btn-primary d-block mb-2">Join Chats</a>
            <a href="5-options/3-viewChats.php" class="btn btn-primary d-block mb-2">View All Chats</a>
        </div>

        <!-- Logout Button -->
        <div class="mt-4">
            <a href="6-logout.php" class="btn btn-danger d-block">Logout</a>
        </div>
    </div>
</body>
</html>
