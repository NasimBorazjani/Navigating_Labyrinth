
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are lists of connected cities
    adjacency_matrix = {
        'H': ['T'],
        'F': ['R', 'I', 'L', 'D'],
        'C': ['L'],
        'E': ['C', 'T'],
        'T': ['H', 'V', 'D'],
        'V': ['F', 'R', 'I'],
        'R': ['I', 'M', 'D'],
        'I': ['V', 'R', 'M'],
        'M': ['H', 'Z'],
        'Z': ['F', 'L'],
        'L': ['C', 'Z', 'D'],
        'D': ['T', 'F', 'R', 'I', 'M', 'Z']
    }
    
    # Define the initial state with the starting city 'E'
    initial_state = 'E'
    
    # Define the goal state with the cities 'D' and 'T' visited twice
    goal_state = ['D', 'T', 'D', 'T']
    
    # Initialize a priority queue to store the paths to be explored, with the initial state as the first element
    queue = [(0, [initial_state])]
    
    # While there are paths to explore
    while queue:
        # Pop the path with the lowest cost from the queue
        _, path = heapq.heappop(queue)
        
        # Get the current city from the end of the path
        current_city = path[-1]
        
        # Check if the path reaches the goal state
        if path == goal_state:
            return path
        
        # Explore all possible next cities to visit from the current city
        for next_city in adjacency_matrix[current_city]:
            # Check if the next city has not been visited before in the path
            if next_city not in path:
                # Calculate the cost of the path by counting the number of cities visited
                cost = len(path)
                # Create a new path by extending the current path with the next city
                new_path = path + [next_city]
                # Add the new path to the queue with the cost as the priority
                heapq.heappush(queue, (cost, new_path))
    
    return None

print(a_star())
