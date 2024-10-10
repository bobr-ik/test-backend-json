<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    $data = $_GET['data']
    ?>

    <script>
        console.log(<?= $data ?>)
    </script>
</body>
</html>