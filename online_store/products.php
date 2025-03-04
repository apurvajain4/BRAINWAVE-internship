<?php
include("dbconfig.php");

$sql = "SELECT * FROM products";
$result = $conn->query($sql);

while ($row = $result->fetch_assoc()) {
    echo "<h2>".$row["productName"]."</h2>";
    echo "<p>".$row["productDescription"]."</p>";
    echo "<p>Price: ".$row["productPrice"]."</p>";
    echo "<hr>";
}
?>
