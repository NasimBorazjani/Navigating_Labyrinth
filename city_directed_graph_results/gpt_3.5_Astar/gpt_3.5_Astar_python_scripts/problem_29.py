
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary of dictionaries
    adjacency_matrix = {
        'R': {'R': 0, 'S': 0, 'W': 0, 'B': 0, 'P': 0, 'G': 0, 'Q': 0, 'E': 1, 'N': 0, 'D': 1, 'J': 1},
        'S': {'R': 0, 'S': 0, 'W': 1, 'B': 0, 'P': 0, 'G': 1, 'Q': 0, 'E': 0, 'N': 1, 'D': 0, 'J': 1},
        'W': {'R': 1, 'S': 0, 'W': 0, 'B': 0, 'P': 0, 'G': 0, 'Q': 0, 'E': 0, 'N': 0, 'D': 0, 'J': 0},
        'B': {'R': 0, 'S': 0, 'W': 0, 'B': 0, 'P': 1, 'G': 0, 'Q': 0, 'E': 0, 'N': 0, 'D': 0, 'J': 1},
        'P': {'R': 0, 'S': 1, 'W': 0, 'B': 0, 'P': 0, 'G': 0, 'Q': 0, 'E': 0, 'N': 0, 'D': 1, 'J': 0},
        'G': {'R': 0, 'S': 0, 'W': 0, 'B': 1, 'P': 0, 'G': 0, 'Q': 0, 'E': 0, 'N': 0, 'D': 0, 'J': 0},
        'Q': {'R': 0, 'S': 0, 'W': 1, 'B': 1, 'P': 1, 'G': 0, 'Q': 0, 'E': 0, 'N': 1, 'D': 1, 'J': 0},
        'E': {'R': 1, 'S': 1, 'W': 0, 'B': 0, 'P': 1, 'G': 1, 'Q': 1, 'E': 0, 'N': 0, 'D': 0, 'J': 0},
        'N': {'R': 0, 'S': 0, 'W': 0, 'B': 0, 'P': 1, 'G': 1, 'Q': 0, 'E': 0, 'N': 0, 'D': 1, 'J': 0},
        'D': {'R': 0, 'S': 0, 'W': 1, 'B': 0, 'P': 0, 'G': 0, 'Q': 0, 'E': 1, 'N': 0, 'D': 0, 'J': 0},
        'J': {'R': 0, 'S': 1, 'W': 0, 'B': 0, 'P': 1, 'G': 0, 'Q': 1, 'E': 0, 'N': 0, 'D': 0, 'J': 0}
    }
    
    # Define the start city
    start_city = 'G'
    # Define the destination cities
    destinations = ['S', 'E']
    
    # Initialize a priority queue to store the states to be visited
    queue = []
    # Record the visited cities and their costs
    visited = {}
    # Record the path taken to reach each city
    path = {}
    
    # Initialize the start state
    start_state = (start_city, 0, 0, [])
    # Push the start state to the priority queue
    heapq.heappush(queue, start_state)
    
    while queue:
        # Pop the state with the lowest cost so far
        current_city, s_count, e_count, current_path = heapq.heappop(queue)
        
        # Check if we have visited both destination cities twice
        if s_count == 2 and e_count == 2:
            return current_path + [current_city]
        
        # Update the visited dictionary
        visited[current_city] = (s_count, e_count)
        
        # Iterate over the neighbors of the current city
        for neighbor, connected in adjacency_matrix[current_city].items():
            # Check if the neighbor is not the current city, is connected, and has not been visited twice
            if neighbor != current_city and connected == 1 and (neighbor not in visited or visited[neighbor] != (2, 2)):
                # Update the counts for S and E destinations
                new_s_count = s_count + (1 if neighbor == 'S' else 0)
                new_e_count = e_count + (1 if neighbor == 'E' else 0)
                # Calculate the new cost
                new_cost = len(current_path) + 1
                # Update the path
                new_path = current_path + [current_city]
                
                # Push the new state to the priority queue
                heapq.heappush(queue, (neighbor, new_s_count, new_e_count, new_path))
    
    return None

print(a_star())
