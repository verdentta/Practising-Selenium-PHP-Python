<!DOCTYPE html>
<html>
<head>
    <title>PHP Form Submission</title>
</head>
<body>

<?php

//set the database connection variables
$servername ="localhost";
$username ="root";
$password ="user";
$dbname ="selenium";

//create connection
$conn = new mysqli($servername, $username, $password, $dbname);

if($conn->connect_error)
{
    die("Connection failed: " . $conn->connect_error);
}

// Check if the form has been submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get form data
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $phone = htmlspecialchars($_POST['phone']);
    $age = htmlspecialchars($_POST['age']);

    //insert the data into the database
    $sql = "INSERT INTO form_data(name, email, phone, age) VALUES ('$name', '$email', '$phone', '$age')";

    if ($conn->query($sql) === TRUE)
    {
        echo "New record created succesfully";
    } else 
    {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    
    // Display the submitted data
    echo "<h3>Form Submitted:</h3>";
    echo "Name: " . $name . "<br>";
    echo "Email: " . $email . "<br>";
    echo "Phone: " . $phone . "<br>";
    echo "Age: " . $age . "<br>";
    
}

$conn->close();
?>

<!-- HTML Form -->
<form method="POST" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
    <label for="name">Name:</label><br>
    <input type="text" id="name" name="name" required><br><br>
    
    <label for="email">Email:</label><br>
    <input type="email" id="email" name="email" required><br><br>

    <label for="phone">Phone Number:</label><br>
    <input type="number" id="phone" name="phone" required><br><br>

    <label for="age">Age:</label><br>
    <input type="number" id="age" name="age" required><br><br>
    
    <input type="submit" value="Submit">
</form>

</body>
</html>