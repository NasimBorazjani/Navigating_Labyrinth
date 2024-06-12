
import heapq


def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries of connected cities
    adjacency_matrix = {
        'B': {'J': 1, 'T': 1, 'N': 1},
        'A': {'B': 1},
        'M': {'G': 1},
        'G': {'C': 1, 'J': 1, 'N': 1},
        'V': {'A': 1, 'B': 1, 'G': 1, 'N': 1},
        'J': {'T': 1, 'W': 1},
        'T': {'A': 1, 'N': 1},
        'N': {'G': 1, 'H': 1, 'W': 1},
        'W': {'G': 1, 'H': 1, 'X': 1},
        'X': {'A': 1, 'T': 1, 'N': 1, 'Y': 1},
        'K': {'V': 1},
        'Y': {'M': 1, 'N': 1, 'W': 1},
        'H': {'M': 1, 'W': 1},
        'C': {'V': 1, 'Y': 1}
    }
    
    # Define the start city, the two destination cities, and the current city
    start_city = 'A'
    destination_cities = ['H', 'W']
    current_city = start_city
    
    # Initialize a list to store the path taken
    path = [current_city]
    
    # While both destination cities have not been visited twice
    while destination_cities[0] not in path or destination_cities[1] not in path or path.count(destination_cities[0]) < 2 or path.count(destination_cities[1]) < 2:
        # Get the connected cities from the current city
        connected_cities = adjacency_matrix[current_city]
        
        # Choose the next city to visit based on the connected cities
        next_city = None
        for city in connected_cities:
            if city not in path:
                next_city = city
                break
        
        # If there are no unvisited connected cities, backtrack to the previous city
        if next_city is None:
            path.pop()
            current_city = path[-1]
        else:
            path.append(next_city)
            current_city = next_city
    
    return path


print(a_star())
