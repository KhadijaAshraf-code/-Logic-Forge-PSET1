def find_longest_mirror_length(s):
    n = len(s)

    # create table filled with 0
    dp = [[0] * n for _ in range(n)]

    # every single letter is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # check substrings of increasing length
    for length in range(2, n + 1):
        for i in range(n - length + 1):

            #This calculates the ending index.
            j = i + length - 1

            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]
print(find_longest_mirror_length("bbab"))



