def removeInvalidParentheses(expr):
    result = set()

    # STEP 1: count removals needed
    left_remove = right_remove = 0
    for ch in expr:
        if ch == '(':
            left_remove += 1
        elif ch == ')':
            if left_remove == 0:
                right_remove += 1
            else:
                left_remove -= 1

    # STEP 2: DFS
    def dfs(index, left_count, right_count, left_remove, right_remove, path):
        # If end of string
        if index == len(expr):
            if left_remove == 0 and right_remove == 0:
                result.add(path)
            return

        ch = expr[index]

        # OPTION 1: Remove character (if possible)
        if ch == '(' and left_remove > 0:
            dfs(index + 1, left_count, right_count,
                left_remove - 1, right_remove, path)

        if ch == ')' and right_remove > 0:
            dfs(index + 1, left_count, right_count,
                left_remove, right_remove - 1, path)

        # OPTION 2: Keep character
        if ch not in "()":
            dfs(index + 1, left_count, right_count,
                left_remove, right_remove, path + ch)

        elif ch == '(':
            dfs(index + 1, left_count + 1, right_count,
                left_remove, right_remove, path + ch)

        elif ch == ')' and right_count < left_count:
            dfs(index + 1, left_count, right_count + 1,
                left_remove, right_remove, path + ch)

    dfs(0, 0, 0, left_remove, right_remove, "")
    return list(result)
print(removeInvalidParentheses("()"))

print(removeInvalidParentheses("(a)"))

print(removeInvalidParentheses("abc"))
