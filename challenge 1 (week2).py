def count_climbing_ways(n):
    if n < 1 or n > 45:
        return 0

    ways = {}

    # base cases
    ways[1] = 1
    if n >= 2:
        ways[2] = 2

    # build answers
    for step in range(3, n + 1):
        ways[step] = ways[step - 1] + ways[step - 2]

    return ways[n]
print(count_climbing_ways(6))