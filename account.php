<?php
session_start();

// Check if the user is logged in
if (!isset($_SESSION['email'])) {
    header("Location: index.php");
    exit();
}

$name = $_SESSION['name'];
$email = $_SESSION['email'];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="index.css">
    <title>Account Page</title>
</head>
<body>
    <div class="account-container">
        <h1>Welcome, <?php echo htmlspecialchars($name); ?>!</h1>
        <p>Your email: <?php echo htmlspecialchars($email); ?></p>
        
        <a href="logout.php"><button class="btn">Logout</button></a>
    </div>
</body>
</html>
