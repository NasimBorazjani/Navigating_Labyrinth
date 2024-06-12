
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries of connected cities
    adjacency_matrix = {
        'R': {'F': 1, 'P': 1, 'W': 1},
        'P': {'E': 1, 'F': 1, 'G': 1, 'H': 1, 'W': 1},
        'Z': {'H': 1, 'M': 1, 'W': 1},
        'U': {'P': 1, 'T': 1},
        'H': {'R': 1, 'U': 1, 'W': 1, 'Y': 1, 'Z': 1},
        'T': {'P': 1, 'W': 1},
        'E': {'F': 1, 'M': 1, 'W': 1},
        'W': {'E': 1, 'H': 1, 'R': 1, 'Y': 1, 'Z': 1},
        'F': {'C': 1, 'G': 1, 'H': 1, 'M': 1, 'P': 1},
        'M': {'C': 1, 'F': 1},
        'D': {'P': 1, 'Y': 1},
        'L': {'H': 1},
        'Y': {'E': 1, 'G': 1, 'H': 1, 'P': 1},
        'C': {'F': 1, 'G': 1, 'M': 1},
        'G': {'C': 1, 'F': 1, 'Y': 1}
    }
    
    # Define the start city
    start_city = 'L'
    
    # Define the goal cities
    goal_cities = ['P', 'W']
    
    # Initialize a priority queue to store the path with the lowest cost
    queue = []
    
    # Initialize the starting state with the start city and the number of times each goal city has been visited
    start_state = (start_city, {city: 0 for city in goal_cities})
    
    # Push the starting state to the priority queue
    heapq.heappush(queue, (0, start_state, [start_city]))
    
    while queue:
        _, (current_city, visited_goals), path = heapq.heappop(queue)
        
        # Check if all goal cities have been visited twice
        if all(visited_goals[city] == 2 for city in goal_cities):
            return path
        
        # Explore all possible next cities to visit
        for next_city in adjacency_matrix[current_city]:
            # Check if the next city is a goal city
            if next_city in goal_cities:
                # If the goal city has not been visited twice yet, update the visited goals
                if visited_goals[next_city] < 2:
                    new_visited_goals = visited_goals.copy()
                    new_visited_goals[next_city] += 1
                    new_state = (next_city, new_visited_goals)
                    new_path = path + [next_city]
                    # Calculate the cost of the new path (number of cities visited)
                    new_cost = len(new_path)
                    heapq.heappush(queue, (new_cost, new_state, new_path))
            else:
                # If the next city is not a goal city, continue exploring
                new_state = (next_city, visited_goals)
                new_path = path + [next_city]
                # Calculate the cost of the new path (number of cities visited)
                new_cost = len(new_path)
                heapq.heappush(queue, (new_cost, new_state, new_path))
    
    return None

print(a_star())
