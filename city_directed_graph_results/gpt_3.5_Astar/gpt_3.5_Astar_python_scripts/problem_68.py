
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
    adjacency_matrix = {
        'P': {'J': 1, 'R': 1},
        'G': {'D': 1, 'M': 1},
        'W': {'L': 1, 'M': 1, 'B': 1},
        'V': {'L': 1, 'B': 1, 'R': 1},
        'L': {'G': 1, 'W': 1, 'V': 1, 'B': 1, 'H': 1},
        'M': {'W': 1, 'G': 1, 'H': 1},
        'B': {'P': 1, 'W': 1, 'H': 1},
        'S': {'H': 1, 'R': 1},
        'J': {'P': 1, 'H': 1, 'D': 1},
        'H': {'L': 1, 'M': 1, 'B': 1, 'S': 1, 'J': 1, 'D': 1},
        'D': {'G': 1, 'J': 1, 'H': 1},
        'N': {'H': 1, 'R': 1},
        'R': {'P': 1, 'V': 1, 'N': 1}
    }
    
    # Define the initial state, goal state, and other variables
    initial_state = 'P'
    goal_cities = ['G', 'J']
    goal_count = {city: 2 for city in goal_cities}
    visited_states = {initial_state: {city: 0 for city in goal_cities}}
    
    # Initialize the priority queue with the initial state
    queue = [(0, initial_state, [])]
    
    while queue:
        _, current_city, path = heapq.heappop(queue)
        
        # Check if we have visited both goal cities twice
        if all(visited_states[current_city][city] == count for city, count in goal_count.items()):
            return path + [current_city]
        
        # Explore all possible connections from the current city
        for neighbor, _ in adjacency_matrix[current_city].items():
            new_path = path + [current_city]
            new_visited_states = {city: count for city, count in visited_states[current_city].items()}
            if neighbor in goal_cities:
                new_visited_states[neighbor] += 1
            new_cost = len(new_path)
            
            # Add the new state to the queue if it has not been visited or we found a shorter path
            if neighbor not in visited_states or new_cost < visited_states[neighbor]:
                visited_states[neighbor] = new_visited_states
                heapq.heappush(queue, (new_cost, neighbor, new_path))
    
    return None

print(a_star())
