def password_recovery_window(log, pattern):
    if not log or not pattern:
        return ""

    from collections import Counter

    # Frequency of required characters
    need = Counter(pattern)
    window = {}

    required = len(need)  # number of unique chars needed
    formed = 0  # number of chars meeting required count

    left = 0
    min_len = float("inf")
    min_window = ""

    # Expand window
    for right in range(len(log)):
        char = log[right]
        window[char] = window.get(char, 0) + 1

        if char in need and window[char] == need[char]:
            formed += 1

        # Try to shrink window
        while formed == required:
            window_size = right - left + 1
            if window_size < min_len:
                min_len = window_size
                min_window = log[left:right + 1]

            left_char = log[left]
            window[left_char] -= 1

            if left_char in need and window[left_char] < need[left_char]:
                formed -= 1

            left += 1

    return min_window
print(password_recovery_window("CODE", "CDS"))
print(password_recovery_window("a", "a"))
print(password_recovery_window("a", "aa"))