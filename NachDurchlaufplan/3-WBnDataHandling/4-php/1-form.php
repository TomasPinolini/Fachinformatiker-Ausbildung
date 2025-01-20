<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form with Various Input Types</title>
</head>
<body>
    <form action="" method="POST">
        <!-- Text Input -->
        Name: <input type="text" name="fname"><br><br>

        <!-- Password Input -->
        Password: <input type="password" name="fpassword"><br><br>

        <!-- Email Input -->
        Email: <input type="email" name="femail"><br><br>

        <!-- Number Input -->
        Age: <input type="number" name="fage" min="1" max="100"><br><br>

        <!-- Radio Buttons -->
        Gender: 
        <input type="radio" name="fgender" value="Male"> Male
        <input type="radio" name="fgender" value="Female"> Female<br><br>

        <!-- Checkboxes -->
        Hobbies: 
        <input type="checkbox" name="fhobbies[]" value="Reading"> Reading
        <input type="checkbox" name="fhobbies[]" value="Traveling"> Traveling
        <input type="checkbox" name="fhobbies[]" value="Gaming"> Gaming<br><br>

        <!-- Select Dropdown -->
        Country:
        <select name="fcountry">
            <option value="USA">USA</option>
            <option value="UK">UK</option>
            <option value="Canada">Canada</option>
            <option value="Australia">Australia</option>
        </select><br><br>

        <!-- Date Input -->
        Birthdate: <input type="date" name="fbirthdate"><br><br>

        <!-- File Upload -->
        Profile Picture: <input type="file" name="fprofilepic"><br><br>

        <!-- Submit Button -->
        <input type="submit" value="Submit">
    </form>
</body>
</html>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Text Input
    $name = htmlspecialchars($_POST['fname']);
    echo empty($name) ? "Name is empty<br>" : "Name: $name<br>";

    // Password Input
    $password = htmlspecialchars($_POST['fpassword']);
    echo empty($password) ? "Password is empty<br>" : "Password: $password<br>";

    // Email Input
    $email = htmlspecialchars($_POST['femail']);
    echo empty($email) ? "Email is empty<br>" : "Email: $email<br>";

    // Number Input
    $age = htmlspecialchars($_POST['fage']);
    echo empty($age) ? "Age is empty<br>" : "Age: $age<br>";

    // Radio Buttons
    $gender = htmlspecialchars($_POST['fgender']);
    echo empty($gender) ? "Gender is not selected<br>" : "Gender: $gender<br>";

    // Checkboxes
    if (!empty($_POST['fhobbies'])) {
        $hobbies = $_POST['fhobbies'];
        echo "Hobbies: " . implode(", ", $hobbies) . "<br>";
    } else {
        echo "No hobbies selected<br>";
    }

    // Dropdown
    $country = htmlspecialchars($_POST['fcountry']);
    echo "Country: $country<br>";

    // Date Input
    $birthdate = htmlspecialchars($_POST['fbirthdate']);
    echo empty($birthdate) ? "Birthdate is empty<br>" : "Birthdate: $birthdate<br>";

    // File Upload
    if (isset($_FILES['fprofilepic']) && $_FILES['fprofilepic']['error'] == UPLOAD_ERR_OK) {
        echo "Profile Picture uploaded: " . htmlspecialchars($_FILES['fprofilepic']['name']) . "<br>";
    } else {
        echo "No profile picture uploaded<br>";
    }
}
?>
