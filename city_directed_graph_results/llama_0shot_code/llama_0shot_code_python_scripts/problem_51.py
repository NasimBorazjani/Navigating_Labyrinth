
import sys

# Adjacency matrix
matrix = [
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
]

# List of city names
cities = ['O', 'C', 'F', 'W', 'I', 'P', 'U', 'B', 'H', 'Q', 'G', 'S']

# Function to perform DFS
def dfs(city, path, counts):
    # Add current city to the path
    path.append(city)
    
    # If we have visited both 'U' and 'F' twice, we stop
    if counts['U'] == 2 and counts['F'] == 2:
        return path
    
    # Visit each neighbor
    for i, val in enumerate(matrix[city]):
        if val == 1:
            # If it's a destination city, we check the count
            if i in ['F', 'U']:
                counts[i] += 1
                if counts[i] == 2:
                    continue
            # If we have not visited the city before, we continue
            if i not in path:
                result = dfs(i, path, counts)
                # If we found a solution, we return it
                if result:
                    return result
            # If we have visited the city but it's not a destination city, we continue
            elif i not in ['F', 'U']:
                result = dfs(i, path, counts)
                # If we found a solution, we return it
                if result:
                    return result
    
    # If we didn't find a solution, we backtrack
    path.pop()
    return None

# Start from city 'G'
result = dfs(6, [], {'U': 0, 'F': 0})

# Print the result
print(result)
