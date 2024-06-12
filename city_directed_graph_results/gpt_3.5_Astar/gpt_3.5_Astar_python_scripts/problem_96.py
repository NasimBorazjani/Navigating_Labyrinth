
import heapq


def a_star():
   # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
   adjacency_matrix = {
       'R': {'L': 1, 'T': 1, 'A': 1},
       'J': {'R': 1, 'Y': 1, 'K': 1},
       'E': {'R': 1, 'A': 1, 'L': 1, 'T': 1},
       'Y': {'N': 1},
       'A': {'R': 1, 'L': 1, 'T': 1, 'B': 1, 'C': 1},
       'L': {'R': 1, 'E': 1, 'A': 1},
       'T': {'R': 1, 'E': 1, 'A': 1},
       'K': {'Z': 1, 'X': 1},
       'C': {'L': 1},
       'N': {'Y': 1, 'E': 1, 'A': 1},
       'B': {'R': 1},
       'S': {'Y': 1, 'Z': 1},
       'Z': {'R': 1, 'J': 1, 'A': 1, 'L': 1, 'T': 1},
       'X': {'R': 1, 'J': 1, 'A': 1},
       'O': {'A': 1, 'L': 1, 'T': 1, 'Z': 1, 'X': 1}
   }
  
   # Define the initial state, which is the starting city 'O'
   initial_state = 'O'
   # Define the goal state, which is to visit cities J and K twice each
   goal_state = ['J', 'J', 'K', 'K']
  
   # Initialize a priority queue to store the states to be visited, with the initial state as the first element
   queue = [(0, [initial_state])]
  
   # While there are states to visit
   while queue:
       _, path = heapq.heappop(queue)
       current_city = path[-1]
      
       # If the current path satisfies the goal state, return the path
       if path.count('J') == 2 and path.count('K') == 2:
           return path
      
       # Generate all possible actions from the current state, which are the cities connected to the current city
       for neighbor, _ in adjacency_matrix[current_city].items():
           # Check if the neighbor city has not been visited before in the current path
           if neighbor not in path:
               # Create a new path by adding the neighbor city to the current path
               new_path = path + [neighbor]
               # Calculate the cost of the new path, which is the length of the path
               new_cost = len(new_path)
               # Add the new path to the priority queue
               heapq.heappush(queue, (new_cost, new_path))
  
   return None


print(a_star())
