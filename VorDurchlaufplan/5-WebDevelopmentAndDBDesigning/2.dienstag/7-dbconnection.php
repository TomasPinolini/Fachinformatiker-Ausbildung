<?php

    $db_server = "localhost";
    $db_user = "root";
    $db_pass = "";
    $db_name = "5-wd&dbd";
    $conn = "";

    $mysqli  = new mysqli(hostname: $db_server, username: $db_user, password: $db_pass, database: $db_name);
    
    if ($mysqli->connect_error) {
        die("Connection failed: " . $mysqli->connect_error);
    }
    // else{
    //     echo "Done!";
    // }
    return $mysqli;

?>