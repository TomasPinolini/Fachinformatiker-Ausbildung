<?php
// Connect to the database
$conn = mysqli_connect("localhost", "root", "", "singleuser_crud");

// Check the connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// Query to get rows with even IDs
$sql = "SELECT id, description FROM first WHERE MOD(id, 2) = 0";
$result = mysqli_query($conn, $sql);

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Filtered Table</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center mb-4">Filtered Table (Even IDs)</h1>
        <table class="table table-striped table-bordered">
            <thead class="table-dark">
                <tr>
                    <th>ID</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>
                <?php
                // Check if the query returned any rows
                if (mysqli_num_rows($result) > 0) {
                    // Loop through each row and display it in the table
                    while ($row = mysqli_fetch_assoc($result)) {
                        echo "<tr>";
                        echo "<td>" . htmlspecialchars($row['id']) . "</td>";
                        echo "<td>" . htmlspecialchars($row['description']) . "</td>";
                        echo "</tr>";
                    }
                } else {
                    // Display a message if no rows are found
                    echo "<tr><td colspan='2' class='text-center'>No data found</td></tr>";
                }
                ?>
            </tbody>
        </table>
    </div>
    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
<?php
// Close the database connection
mysqli_close($conn);
?>
