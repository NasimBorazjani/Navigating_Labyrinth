
import itertools

# Adjacency matrix
matrix = [
    "010000000001000",
    "100000000000000",
    "100000010000000",
    "000000000111000",
    "100000110100010",
    "001000010001000",
    "000000000110000",
    "000100100000101",
    "000001100000000",
    "000000000100000",
    "111110000000000",
    "010101000000000",
    "000000000011001",
    "000110000010010",
    "000000000000100",
]

# Convert the adjacency matrix into a dictionary of lists
graph = {city: [] for city in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if col == "1":
            graph[chr(i + 65)].append(chr(j + 65))

# Function to perform depth-first search
def find_routes(city, g_count, o_count, route):
    if g_count == o_count == 2:
        routes.append(route)
    for next_city in graph[city]:
        if next_city not in route:
            find_routes(next_city, g_count + (next_city == 'G'), o_count + (next_city == 'O'), route + next_city)

# Perform depth-first search from city 'A'
routes = []
find_routes('A', 0, 0, 'A')

# Sort the routes by total travel time
routes.sort(key=len)

# Return the shortest route
print(routes[0])
