<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "5-phpandsql";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "INSERT INTO first (description) VALUES ('uno');";
$sql .= "INSERT INTO first (description) VALUES ('dos');";
$sql .= "INSERT INTO first (description) VALUES ('tres');";


if ($conn->multi_query($sql) === TRUE) {
  echo "New records created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>