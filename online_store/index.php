<?php
include("dbconfig.php");
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Online Store</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <h1>Welcome to Online Store</h1>
    <h2>Products</h2>
    
    <?php
    $sql = "SELECT * FROM products";
    $result = $conn->query($sql);
    while ($row = $result->fetch_assoc()) {
        echo "<div>";
        echo "<h3>".$row["productName"]."</h3>";
        echo "<p>".$row["productDescription"]."</p>";
        echo "<p>Price: ".$row["productPrice"]."</p>";
        echo '<a href="cart.php?id='.$row["id"].'">Add to Cart</a>';
        echo "</div>";
    }
    ?>
</body>
</html>
