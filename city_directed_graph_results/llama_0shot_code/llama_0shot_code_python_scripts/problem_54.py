
def get_path(matrix, start):
    n = len(matrix)
    visited = [False] * n
    path = []

    def dfs(city):
        visited[city] = True
        path.append(city)

        for i in range(n):
            if matrix[city][i] == 1 and not visited[i]:
                dfs(i)

        path.pop()
        visited[city] = False

    dfs(start)
    return [chr(i + 65) for i in path]

matrix = [
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
]

print(get_path(matrix, 17))  # 'R', 'A', 'Y', 'K', 'U', 'T', 'G', 'D', 'E', 'I', 'S', 'P', 'M', 'R'
