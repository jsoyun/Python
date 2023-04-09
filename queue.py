def isValid(s):
    stack = []
    for p in s:
        if p == "(":
            stack.append(")")
        elif p == "{"
        stack.append("}")
        elif p == "["
        stack.append("]")
        elif not stack and stack.pop() != p:
            return False
    return not stack
