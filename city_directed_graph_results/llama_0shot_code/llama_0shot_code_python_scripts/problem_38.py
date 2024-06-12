
# Adjacency matrix
matrix = [[0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
          [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
          [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
          [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
          [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
          [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0],
          [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
          [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
          [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
          [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]]

# List of cities
cities = ['S', 'X', 'Y', 'Q', 'O', 'R', 'D', 'V', 'H', 'J', 'F', 'C']

# Function to perform depth-first search
def dfs(city, visited, path):
    # Mark the current city as visited
    visited[city] = True
    # Add the current city to the path
    path.append(cities[city])

    # If the current city is 'F' or 'V', and we have visited it twice,
    # then we have found a solution
    if (cities[city] == 'F' and path.count('F') == 2) or (cities[city] == 'V' and path.count('V') == 2):
        return path

    # Try to find a solution by visiting the next city
    for next_city in range(len(matrix)):
        if matrix[city][next_city] == 1 and not visited[next_city]:
            result = dfs(next_city, visited, path)
            if result:
                return result

    # Backtrack: remove the current city from the path and unmark it
    path.pop()
    visited[city] = False

    return None

# Start the search from city 'Q'
start_city = cities.index('Q')
visited = [False] * len(matrix)
path = []
result = dfs(start_city, visited, path)
print(result)
