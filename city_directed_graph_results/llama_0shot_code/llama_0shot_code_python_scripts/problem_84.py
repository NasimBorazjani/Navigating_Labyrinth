
# Adjacency matrix
matrix = [
    "000110001000000",
    "000010100100100",
    "100001100011100",
    "000110001000000",
    "000000100100100",
    "000010100100000",
    "000110000100111",
    "100001001110000",
    "000000010011100",
    "110000001001110",
    "000110001000010",
    "100001000010010",
    "000010100100100",
    "100001000100010"
]

# Create a dictionary from the adjacency matrix
graph = {city: [] for city in 'FOLPYRQBTVAKS'}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == '1':
            graph[chr(i+65)].append(chr(j+65))

# DFS function
def dfs(city, path):
    path.append(city)
    if city not in ('H', 'K'):
        for neighbor in graph[city]:
            if neighbor not in path:
                dfs(neighbor, path)
    path.append(city)

# Start the DFS from 'T'
path = []
dfs('T', path)

# Visit 'H' and 'K' twice
path.extend(['H', 'K'])

print(path)
