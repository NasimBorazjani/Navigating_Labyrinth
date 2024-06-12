
import itertools

# The adjacency matrix
adj_matrix = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0]
]

# The list of cities
cities = ['O', 'T', 'I', 'F', 'A', 'M', 'X', 'Y', 'R', 'G']

# The start city
start = 'M'

# The target cities
targets = ['A', 'R']

# The number of times to visit each city
visits = {city: 2 if city in targets else 1 for city in cities}

# The total number of cities to visit
total_visits = sum(visits.values())

# The minimum total time
min_total_time = float('inf')

# The quickest route
quickest_route = None

# The function to calculate the total time of a route
def total_time(route):
    return sum(adj_matrix[cities.index(route[i-1])][cities.index(route[i])] for i in range(1, len(route)))

# The function to search for the quickest route
def search(route, remaining_visits):
    global min_total_time, quickest_route
    if len(route) == total_visits + 1:
        total_time_route = total_time(route)
        if total_time_route < min_total_time:
            min_total_time = total_time_route
            quickest_route = route
    else:
        for city in cities:
            if city not in route:
                new_route = route + [city]
                new_remaining_visits = remaining_visits.copy()
                for target in targets:
                    new_remaining_visits[target] -= city == target
                if all(visit >= 0 for visit in new_remaining_visits.values()):
                    search(new_route, new_remaining_visits)

# Search for the quickest route
search([start], visits)

# Print the quickest route
print(quickest_route)
