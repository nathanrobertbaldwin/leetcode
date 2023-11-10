function isValid(s) {
  if (s.length % 2 === 1) return false;

  let stack = [];

  for (let i = 0; i < s.length; i++) {
    let char = s[i];

    // Only push an opening brace's partner.
    if (char == "(") stack.push(")");
    if (char == "{") stack.push("}");
    if (char == "[") stack.push("]");

    // If stack is empty, we have a closing brace without the correct opening brace.
    if (stack.length === 0) return false;

    // If the element we remove from the stack isn't the correct closing brace...
    let testChar = stack.pop();
    if (char !== testChar) return false;
  }

  return stack.length === 0;
}
