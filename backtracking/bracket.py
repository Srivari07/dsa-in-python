
def generateParenthesis(n):
    res = []

    def helper(res, s, open, close, n):

        if len(s) == n*2:
            res.append(s)
            return

        if open < n:
            helper(res, s+"(", open+1, close, n)
        if close < open:
            helper(res, s+")", open, close+1, n)

    helper(res, "", 0, 0, n)
    return res


print(generateParenthesis(3))
