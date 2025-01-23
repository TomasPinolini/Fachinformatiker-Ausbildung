<?php
session_start();
require '../1-dbconnection.php';

// Check if the user is logged in
if (!isset($_SESSION['user_id']) || !isset($_SESSION['db_user']) || !isset($_SESSION['db_pass'])) {
    die("You must be logged in to view and join chats.");
}

// Establish a database connection using the logged-in user's credentials
$mysqli = connect($_SESSION['db_user'], $_SESSION['db_pass']);
$user_id = $_SESSION['user_id'];

// Fetch chats the user is NOT part of using prepared statements
$sqlChats = "SELECT c.chat_id, c.chat_name 
             FROM chats c
             WHERE c.chat_id NOT IN (
                 SELECT cp.chat_id 
                 FROM chat_participants cp 
                 WHERE cp.user_id = ?
             )";
$stmt = $mysqli->prepare($sqlChats);
$stmt->bind_param("i", $user_id);
$stmt->execute();
$result = $stmt->get_result();
$chats = $result->fetch_all(MYSQLI_ASSOC);

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['joinChats']) && !empty($_POST['selected_chats'])) {
    $stmtInsert = $mysqli->prepare("INSERT INTO chat_participants (chat_id, user_id, role) VALUES (?, ?, 'member')");
    foreach ($_POST['selected_chats'] as $chat_id) {
        $chat_id = intval($chat_id); // Sanitize input
        $stmtInsert->bind_param("ii", $chat_id, $user_id);
        $stmtInsert->execute();
    }
    $stmtInsert->close();

    // Redirect back to refresh the list
    header("Location: " . $_SERVER['PHP_SELF']);
    exit;
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Join Chats</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <!-- Page Header -->
    <div class="container mt-5">
        <h1 class="text-center">Join Chats</h1>
    </div>

    <!-- Chat List Form -->
    <div class="container mt-4">
        <form method="POST">
            <div class="table-responsive">
                <table class="table table-bordered table-striped">
                    <thead class="table-dark">
                        <tr>
                            <th style="width: 10%;">Select</th>
                            <th style="width: 90%;">Chat Name</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php if (!empty($chats)): ?>
                            <?php foreach ($chats as $chat): ?>
                                <tr>
                                    <td>
                                        <input type="checkbox" name="selected_chats[]" value="<?= htmlspecialchars($chat['chat_id']) ?>">
                                    </td>
                                    <td><?= htmlspecialchars($chat['chat_name']) ?></td>
                                </tr>
                            <?php endforeach; ?>
                        <?php else: ?>
                            <tr>
                                <td colspan="2" class="text-center">No chats available to join.</td>
                            </tr>
                        <?php endif; ?>
                    </tbody>
                </table>
            </div>
            <button type="submit" name="joinChats" class="btn btn-success">Join Selected Chats</button>
        </form>
    </div>

    <!-- Back Button -->
    <div class="container mt-3">
        <a href="../4-menu.php" class="btn btn-dark">Back to Menu</a>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
