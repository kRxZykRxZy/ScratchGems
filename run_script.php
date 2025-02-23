<?php
// Path to your shell script
$scriptPath = './Terminal.sh';

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Execute the shell script without displaying the output
    shell_exec($scriptPath);
    
    // Redirect back to the original page after running the script
    header('Location: index.html');
    exit;
}
?>
