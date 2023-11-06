function isPalindrome(s) {
  s = s.toLowerCase();
  let cleaned = "";
  for (let i = 0; i < s.length; i++) {
    if ((s[i] >= "a" && s[i] <= "z") || (s[i] >= "0" && s[i] <= "9"))
      cleaned += s[i];
  }

  let palindrome = true;

  for (let i = 0; i < Math.floor(cleaned.length / 2); i++) {
    if (cleaned[i] !== cleaned[cleaned.length - 1 - i]) palindrome = false;
  }
  return palindrome;
}

console.log(isPalindrome("0P"));

// Can also use: s.toLowerCase().replace(/[^a-z0-9]/g, "")
// 1. [^] negates a range of characters.
// 2. g is the global flag 
// 3. i is case insensitive. I like the toLowerCase() first.