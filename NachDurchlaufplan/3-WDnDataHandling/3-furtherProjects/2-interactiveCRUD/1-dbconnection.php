<?php
function connect($db_user, $db_pass) {
    $mysqli = new mysqli(hostname: "localhost", username: $db_user, password: $db_pass, database: "multiuser_crud");
    if ($mysqli->connect_error) {
        die("Connection failed: " . $mysqli->connect_error);
    }
    return $mysqli;
}
?>
