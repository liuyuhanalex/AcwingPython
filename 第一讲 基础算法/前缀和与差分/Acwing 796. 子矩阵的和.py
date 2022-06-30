if __name__ == '__main__':
    n, m, q = [int(i) for i in input().split(' ')]
    matrix = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1, n+1):
        matrix[i][1: m+1] = [int(j) for j in input().split(' ')]
    for i in range(1, n+1):
        for j in range(1, m+1):
            matrix[i][j] += matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]
    for i in range(q):
        x1, y1, x2, y2 = [int(j) for j in input().split()]
        print(matrix[x2][y2] - matrix[x1-1][y2] - matrix[x2][y1-1] + matrix[x1-1][y1-1])
