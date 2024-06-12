
import heapq

def a_star():
    # Define the adjacency matrix as a dictionary
    adjacency_matrix = {
        'R': {'R': 0, 'L': 0, 'F': 0, 'E': 1, 'D': 0, 'Q': 0, 'G': 1, 'U': 0, 'H': 0, 'T': 0, 'Z': 1, 'A': 0},
        'L': {'R': 0, 'L': 0, 'F': 0, 'E': 0, 'D': 0, 'Q': 0, 'G': 1, 'U': 0, 'H': 0, 'T': 0, 'Z': 0, 'A': 1},
        'F': {'R': 0, 'L': 0, 'F': 0, 'E': 0, 'D': 0, 'Q': 1, 'G': 0, 'U': 0, 'H': 0, 'T': 0, 'Z': 0, 'A': 0},
        'E': {'R': 0, 'L': 0, 'F': 0, 'E': 0, 'D': 0, 'Q': 1, 'G': 0, 'U': 1, 'H': 0, 'T': 0, 'Z': 0, 'A': 0},
        'D': {'R': 1, 'L': 0, 'F': 0, 'E': 1, 'D': 0, 'Q': 0, 'G': 0, 'U': 0, 'H': 1, 'T': 0, 'Z': 0, 'A': 1},
        'Q': {'R': 1, 'L': 1, 'F': 0, 'E': 0, 'D': 0, 'Q': 0, 'G': 0, 'U': 1, 'H': 1, 'T': 0, 'Z': 0, 'A': 0},
        'G': {'R': 0, 'L': 1, 'F': 1, 'E': 1, 'D': 1, 'Q': 0, 'G': 0, 'U': 1, 'H': 1, 'T': 0, 'Z': 0, 'A': 0},
        'U': {'R': 0, 'L': 0, 'F': 0, 'E': 0, 'D': 1, 'Q': 0, 'G': 0, 'U': 0, 'H': 1, 'T': 0, 'Z': 1, 'A': 0},
        'H': {'R': 1, 'L': 0, 'F': 1, 'E': 0, 'D': 0, 'Q': 0, 'G': 0, 'U': 0, 'H': 0, 'T': 0, 'Z': 0, 'A': 0},
        'T': {'R': 0, 'L': 1, 'F': 0, 'E': 0, 'D': 1, 'Q': 0, 'G': 0, 'U': 0, 'H': 1, 'T': 0, 'Z': 1, 'A': 0},
        'Z': {'R': 1, 'L': 0, 'F': 1, 'E': 0, 'D': 1, 'Q': 1, 'G': 0, 'U': 0, 'H': 1, 'T': 0, 'Z': 0, 'A': 0},
        'A': {'R': 0, 'L': 0, 'F': 0, 'E': 0, 'D': 1, 'Q': 1, 'G': 0, 'U': 0, 'H': 0, 'T': 1, 'Z': 0, 'A': 0}
    }

    # Define the initial state and goal state
    initial_state = 'F'
    goal_state = ['R', 'A']

    # Initialize a priority queue to store the states to be visited
    queue = []
    heapq.heappush(queue, (0, initial_state, []))

    # While there are states to visit
    while queue:
        _, current_state, path = heapq.heappop(queue)

        # If we have visited both destination cities twice, return the path
        if path.count('R') == 2 and path.count('A') == 2:
            return path + [current_state]

        # Add the current state to the path
        new_path = path + [current_state]

        # Generate all possible actions from the current state
        for next_state in adjacency_matrix[current_state]:
            # Check if the next state has not been visited before
            if next_state not in new_path:
                # Add the next state to the priority queue with the updated path
                heapq.heappush(queue, (len(new_path), next_state, new_path))

    return None

print(a_star())
