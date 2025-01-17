<?php
session_start();
session_unset();
session_destroy();
header("Location: 13-type_user_login.php");
exit;
?>
