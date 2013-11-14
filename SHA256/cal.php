<?php
echo $path = isset($_GET['path'])?$_GET['path']:'';
echo '<br/>';
echo exec('python cal.py '.$path);
?>
