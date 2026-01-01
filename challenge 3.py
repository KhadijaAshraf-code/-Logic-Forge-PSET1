def findMedianSortedArrays(scoresA, scoresB):
    m, n = len(scoresA), len(scoresB)
    total = m + n

    i = j = 0
    count = 0

    prev = curr = 0

    # Traverse until we reach the median position
    while count <= total // 2:
        prev = curr

        if i < m and (j >= n or scoresA[i] <= scoresB[j]):
            curr = scoresA[i]
            i += 1
        else:
            curr = scoresB[j]
            j += 1

        count += 1

    # If total elements are odd
    if total % 2 == 1:
        return float(curr)

    # If total elements are even
    return (prev + curr) / 2.0
print(findMedianSortedArrays([1,2,3,4], [6,7,8,9]))