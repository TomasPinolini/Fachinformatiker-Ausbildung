<?php
    session_start();
    require '../1-dbconnection.php';

    // Check if the user is logged in
    if (!isset($_SESSION['user_id']) || !isset($_SESSION['db_user']) || !isset($_SESSION['db_pass'])) {
        die("Invalid access. Please log in.");
    }

    // Establish a database connection using the logged-in user's credentials
    $mysqli = connect($_SESSION['db_user'], $_SESSION['db_pass']);
    $user_id = $_SESSION['user_id'];

    // Fetch chats the user is part of
    $sqlJoinedChats = "SELECT c.chat_id, c.chat_name 
                    FROM chats c
                    JOIN chat_participants cp ON c.chat_id = cp.chat_id
                    WHERE cp.user_id = ?";
    $stmtJoined = $mysqli->prepare($sqlJoinedChats);
    $stmtJoined->bind_param("i", $user_id);
    $stmtJoined->execute();
    $resultJoined = $stmtJoined->get_result();
    $joinedChats = $resultJoined->fetch_all(MYSQLI_ASSOC);
    $stmtJoined->close();

    // Fetch chats the user is NOT part of
    $sqlOtherChats = "SELECT c.chat_id, c.chat_name 
                    FROM chats c
                    WHERE c.chat_id NOT IN (
                        SELECT cp.chat_id 
                        FROM chat_participants cp 
                        WHERE cp.user_id = ?
                    )";
    $stmtOther = $mysqli->prepare($sqlOtherChats);
    $stmtOther->bind_param("i", $user_id);
    $stmtOther->execute();
    $resultOther = $stmtOther->get_result();
    $otherChats = $resultOther->fetch_all(MYSQLI_ASSOC);
    $stmtOther->close();
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
        <?php if (!empty($joinedChats)): ?>
            <ul class="list-group mb-4">
                <?php foreach ($joinedChats as $chat): ?>
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        <?= htmlspecialchars($chat['chat_name']) ?>
                        <form method="POST" action="5-4-chat.php" class="d-inline">
                            <input type="hidden" name="chat_id" value="<?= htmlspecialchars($chat['chat_id']) ?>">
                            <button type="submit" class="btn btn-sm btn-primary">Enter</button>
                        </form>
                    </li>
                <?php endforeach; ?>
            </ul>
        <?php else: ?>
            <p class="text-muted">You are not part of any chats yet.</p>
        <?php endif; ?>

        <!-- Section: Chats User is NOT Part Of -->
        <h3 class="mt-4">Other Chats</h3>
        <?php if (!empty($otherChats)): ?>
            <ul class="list-group mb-4">
                <?php foreach ($otherChats as $chat): ?>
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        <?= htmlspecialchars($chat['chat_name']) ?>
                        <a href="5-2-joinChats.php" class="btn btn-sm btn-success">Join</a>
                    </li>
                <?php endforeach; ?>
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
