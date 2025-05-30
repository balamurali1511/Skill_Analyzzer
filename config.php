<?php
  $servername = "localhost";
  $username = "root";
  $password = "";
  $dbname = "log";

  $conn = new mysqli($servername,$username,$password,$dbname);

  if($conn->connect_error)
  {
       die("connection faild".$conn->connect_error);
  }
    echo "";
  
?>