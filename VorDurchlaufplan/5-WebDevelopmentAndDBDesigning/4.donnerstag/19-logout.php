<?php
session_start();
session_unset();
session_destroy();
header("Location: 17-type_user_login.php");
exit;
?>
