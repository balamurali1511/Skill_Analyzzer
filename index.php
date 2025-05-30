<?php
include("config.php");

if (isset($_POST['Submit'])) {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $pass = $_POST['pass'];

    $verify_query = mysqli_query($conn, "SELECT Email FROM ind WHERE Email='$email'");
    if (mysqli_num_rows($verify_query) != 0) {
        echo "<div class='message'>
                <p>This email is already in use, try another one!</p>
            </div> <br>";
        echo "<a href='javascript:self.history.back()'><button class='btn'>Go Back</button>";
    } else {
        mysqli_query($conn, "INSERT INTO ind(Name, Email, Password) VALUES('$name','$email','$pass')") or die("Error Occurred");
        echo "<div class='message'>
                <p>Registration Successful!</p>
            </div> <br>";
        echo "<a href='index.php'><button class='btn'>Login Now</button>";
    }
} elseif (isset($_POST['submit'])) {
    $email = $_POST['email'];
    $password = $_POST['password'];

    $result = mysqli_query($conn, "SELECT * FROM ind WHERE Email='$email' AND Password='$password'");
    if (mysqli_num_rows($result) == 1) {
        echo "<script>window.location.href = 'home.html';</script>";
    } else {
        echo "<div class='message'>
                <p>Invalid email or password!</p>
            </div> <br>";
        echo "<a href='javascript:self.history.back()'><button class='btn'>Go Back</button>";
    }
} else {
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://pro.fontawesome.com/releases/v5.10.0/css/all.css" />
    <script src="https://kit.fontawesome.com/c4254e24a8.js" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="index1.css">
    <title>singup</title>
</head>
<body>
<div class="container" id="container">
    <div class="form-container sign-up-container">
        <form action="index.php" method="POST">
            <h1>Create Account</h1>
            <div class="social-container">
                <a href="#" class="social"><i class="fab fa-facebook"></i></a>
                <a href="#" class="social"><i class="fab fa-google"></i></a>
                <a href="#" class="social"><i class="fab fa-linkedin"></i></a>
            </div>
            <span>or use your email for registration</span>
            <input type="text" name="name" id="name" placeholder="Name" required />
            <input type="email" name="email" id="email" placeholder="Email" required />
            <input type="password" name="pass" id="pass" placeholder="Password" required />
            <button type="submit" name="Submit" id="Submit">Sign Up</button>
        </form>
    </div>
    <div class="form-container sign-in-container">
        <form action="index.php" method="POST">
            <h1>Sign in</h1>
            <div class="social-container">
                <a href="#" class="social"><i class="fab fa-facebook"></i></a>
                <a href="#" class="social"><i class="fab fa-google"></i></a>
                <a href="#" class="social"><i class="fab fa-linkedin"></i></a>
            </div>
            <span>or use your account</span>
            <input type="email" name="email" id="email2" placeholder="Email" required />
            <input type="password" name="password" id="password" placeholder="Password" required />
            <a href="#">Forgot your password?</a>
            <button type="submit" name="submit" id="submit">Sign In</button>
        </form>
    </div>
    <div class="overlay-container">
        <div class="overlay">
            <div class="overlay-panel overlay-left">
                <h1>Welcome Back!</h1>
                <p>To keep connected with us please login with your personal info</p>
                <button class="ghost" id="signIn">Sign In</button>
            </div>
            <div class="overlay-panel overlay-right">
                <h1>Hello, Friend!</h1>
                <p>Enter your personal details and start journey with us</p>
                <button class="ghost" id="signUp">Sign Up</button>
            </div>
        </div>
    </div>
</div>

<script>
const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
    container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
    container.classList.remove("right-panel-active");
});
</script>
</body>
</html>

<?php } ?>
