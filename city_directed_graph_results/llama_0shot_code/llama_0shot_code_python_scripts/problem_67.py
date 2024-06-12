
import heapq

# Define the adjacency matrix and the names of the cities
adjacency_matrix = [
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0]
]

city_names = ['A', 'K', 'G', 'U', 'Q', 'D', 'N', 'X', 'S', 'V', 'Y', 'R', 'Z']

# Define the starting city
start_city = 'S'

# Create a dictionary to store the shortest distances from the start city to all other cities
shortest_distances = {city: float('infinity') for city in city_names}
shortest_distances[start_city] = 0

# Create a dictionary to store the previous city in the shortest path from the start city to each city
previous_cities = {city: None for city in city_names}

# Define the destinations and the number of visits to each destination
destinations = {'N': 2, 'R': 2}

# Create a dictionary to store the number of visits to each city
visits = {city: 0 for city in city_names}

# Use a priority queue to select the next city to visit
next_city = [0, start_city]

while next_city:
    current_distance, current_city = heapq.heappop(next_city)
    
    # If we have visited the current city twice and it is a destination city, skip it
    if current_city in destinations and visits[current_city] == destinations[current_city]:
        continue
    
    # If we have visited the current city once and it is a destination city, increase the visit count
    if current_city in destinations:
        visits[current_city] += 1
    
    for i, distance in enumerate(adjacency_matrix[city_names.index(current_city)]):
        if distance == 1:
            city = city_names[i]
            
            # If we have visited the city twice and it is a destination city, skip it
            if city in destinations and visits[city] == destinations[city]:
                continue
            
            new_distance = current_distance + 1
            if new_distance < shortest_distances[city]:
                shortest_distances[city] = new_distance
                previous_cities[city] = current_city
                heapq.heappush(next_city, (new_distance, city))

# Construct the shortest path
path = []
city = 'N'
while city is not None:
    path.append(city)
    city = previous_cities[city]
path.reverse()

# Print the shortest path
print(path)
