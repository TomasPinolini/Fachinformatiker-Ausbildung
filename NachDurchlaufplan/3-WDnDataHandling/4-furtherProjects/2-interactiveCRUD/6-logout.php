<?php
session_start();
if (session_status() === PHP_SESSION_ACTIVE) {
    session_unset();
    session_destroy();
}

header("Location: 4-2-3-login_register.php");
exit;
?>
