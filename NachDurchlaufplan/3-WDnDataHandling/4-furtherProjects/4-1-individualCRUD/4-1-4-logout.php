<?php
session_start();
session_unset();
session_destroy();
header("Location: 4-1-3-type_user_login.php");
exit;
?>
