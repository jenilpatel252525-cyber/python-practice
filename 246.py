def generateParenthesis(n: int):
    res = []

    def backtrack(curr, open_count, close_count):
        # If the string is complete
        if len(curr) == 2 * n:
            res.append(curr)
            return

        # If we can still add "("
        if open_count < n:
            backtrack(curr + "(", open_count + 1, close_count)

        # If we can still add ")"
        if close_count < open_count:
            backtrack(curr + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return res