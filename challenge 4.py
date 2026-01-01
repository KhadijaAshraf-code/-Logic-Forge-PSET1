import heapq

def kthSmallest(matrix, k):
    import heapq

    n = len(matrix)
    heap = []

    for r in range(n):
        heapq.heappush(heap, (matrix[r][0], r, 0))

    for i in range(k):
        value, r, c = heapq.heappop(heap)
        if c + 1 < n:
            heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))

    return value

matrix = [[1,3,9],[8,11,13],[12,13,16]]
k = 6
print(kthSmallest(matrix, k))
