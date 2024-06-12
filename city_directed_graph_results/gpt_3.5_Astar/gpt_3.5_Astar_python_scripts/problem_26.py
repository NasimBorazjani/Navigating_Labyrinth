
import heapq


def a_star():
   # Define the adjacency matrix as a dictionary of dictionaries, where the keys are the city names and the values are dictionaries representing the connections to other cities
   adjacency_matrix = {
       'L': {'Z': 1, 'R': 1, 'K': 1},
       'T': {'P': 1, 'H': 1, 'I': 1, 'X': 1},
       'W': {'C': 1, 'K': 1},
       'P': {'L': 1, 'C': 1},
       'Z': {'L': 1, 'T': 1, 'R': 1},
       'H': {'L': 1, 'T': 1, 'K': 1},
       'I': {'T': 1, 'Z': 1, 'C': 1},
       'X': {'W': 1},
       'R': {'T': 1, 'H': 1, 'C': 1},
       'C': {'L': 1, 'T': 1, 'P': 1, 'R': 1},
       'K': {'Z': 1, 'H': 1, 'R': 1}
   }
  
   # Define the initial state, which is the starting city 'I'
   initial_state = 'I'
   # Define the goal state, which is to visit cities 'W' and 'L' twice each
   goal_state = ['W', 'W', 'L', 'L']
  
   # Initialize a priority queue to store the states to be visited, with the initial state as the first element
   queue = [(0, [initial_state])]
  
   # While there are states to visit
   while queue:
       _, path = heapq.heappop(queue)
       current_city = path[-1]
      
       # If the current path satisfies the goal state, return the path
       if path.count('W') == 2 and path.count('L') == 2:
           return path
      
       # Generate all possible actions from the current state, which are the cities connected to the current city
       for neighbor in adjacency_matrix[current_city]:
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
