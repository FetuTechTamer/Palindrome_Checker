<?php

function isPalindrome($string) {
    // Convert the string to lowercase and remove non-alphanumeric characters
    $cleanedString = preg_replace("/[^A-Za-z0-9]/", '', strtolower($string));

    // Check if the cleaned string is the same as its reverse
    return $cleanedString === strrev($cleanedString);
}

// Example usage
$inputString = "A man, a plan, a canal, Panama";
if (isPalindrome($inputString)) {
    echo "'$inputString' is a palindrome.";
} else {
    echo "'$inputString' is not a palindrome.";
}

?>
