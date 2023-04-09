const s = "{(({[]))[]}";
function queue(s) {
  const stack = [];
  for (let i = 0; i < s.length; i++) {
    if (s == "(") {
      stack.append(")");
    } else if (s == "{") {
      stack.append("}");
    } else if (s == "[") {
      stack.append("]");
    } else if (stack == null || stack.pop() != s) {
      return false;
    } else if (stack == null) {
      return true;
    }
  }
}

queue(s);
