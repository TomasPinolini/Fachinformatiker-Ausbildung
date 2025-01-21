<?php
$conn = mysqli_connect("localhost", "root", "", "singleuser_crud");

// Initialize message
$message = "";

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $id = intval($_POST['id']); // Get the ID from the form input
    $description = trim($_POST['description']); // Get and sanitize the description

    // Check if both fields are provided
    if (!empty($id) && !empty($description)) {
        // Update query
        $sql = "UPDATE first SET description = '$description' WHERE id = $id";

        // Execute the query
        if (mysqli_query($conn, $sql)) {
            $message = "Description updated successfully!";
        } else {
            $message = "Error updating description: " . mysqli_error($mysqli);
        }
    } else {
        $message = "Both ID and Description are required!";
    }
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Update Data</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Update Description</h1>
        <form method="POST" class="mt-4">
            <!-- ID Input -->
            <div class="mb-3">
                <label for="id" class="form-label">ID</label>
                <input type="number" name="id" id="id" class="form-control" required placeholder="Enter ID">
            </div>
            <!-- Description Input -->
            <div class="mb-3">
                <label for="description" class="form-label">New Description</label>
                <input type="text" name="description" id="description" class="form-control" required placeholder="Enter New Description">
            </div>
            <!-- Submit Button -->
            <button type="submit" class="btn btn-primary">Update</button>
        </form>
        <!-- Message Display -->
        <?php if (!empty($message)): ?>
            <div class="alert alert-info mt-3"><?= htmlspecialchars($message) ?></div>
        <?php endif; ?>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>