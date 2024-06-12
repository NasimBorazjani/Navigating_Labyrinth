
import numpy as np

# Adjacency matrix
matrix = np.array([[0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                   [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
                   [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
                   [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
                   [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
                   [0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                   [0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0]])

# Find the nearest city from the given city
def nearest_city(city, visited):
    unvisited = [i for i in range(len(matrix)) if i != city and i not in visited]
    distances = matrix[city, unvisited]
    return unvisited[np.argmin(distances)]

# Route plan
route = []
visited = []
current_city = 0  # Start from city 'K'

for i in range(22):  # 22 = (13 cities * 2 visits)
    if i % 2 == 0:
        route.append(current_city)
    else:
        visited.append(current_city)
    current_city = nearest_city(current_city, visited)

route.append(current_city)  # Return to city 'K'
route = [chr(65 + i) for i in route]  # Convert city indices to letters

print(route)
