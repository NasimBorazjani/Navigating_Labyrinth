
import itertools

# Adjacency matrix
matrix = [
    [0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
]

# Names of the cities
cities = ['D', 'T', 'L', 'E', 'C', 'J', 'Q', 'O', 'K', 'X', 'F']

# Function to calculate the total travel time
def total_travel_time(route):
    total = 0
    for i in range(len(route) - 1):
        from_city = route[i]
        to_city = route[i + 1]
        total += matrix[cities.index(from_city)][cities.index(to_city)]
    return total

# List to store the final solution
solution = None

# Iterate over all possible routes
for route in itertools.permutations(cities[1:]):
    route = ['J'] + list(route) + ['J']
    # Visit city E and D exactly twice
    count_E = route.count('E')
    count_D = route.count('D')
    if count_E == 2 and count_D == 2:
        # Update the solution if this route is quicker
        if solution is None or total_travel_time(route) < total_travel_time(solution):
            solution = route

print(solution)
