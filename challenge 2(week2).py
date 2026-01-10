def find_longest_mirror_length(s):
    n = len(s)

    # Step 1: Create DP table
    dp = [[0] * n for _ in range(n)]

    # Step 2: Single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Step 3: Build the table for substrings of length 2 to n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            # If characters match
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                # Take the maximum by skipping one character
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # Step 4: Result is stored at dp[0][n-1]
    return dp[0][n - 1]

s = "bbabcbcab"
print(find_longest_mirror_length(s))


