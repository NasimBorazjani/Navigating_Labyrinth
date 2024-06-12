
import heapq


def a_star():
   # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
   adjacency_matrix = {
       'C': {'K': 0, 'U': 1, 'F': 1, 'Q': 0, 'B': 1, 'N': 0, 'W': 0, 'H': 0, 'J': 0, 'T': 1, 'X': 1, 'R': 0, 'L': 1},
       'K': {'C': 1, 'U': 0, 'F': 0, 'Q': 1, 'B': 0, 'N': 1, 'W': 1, 'H': 0, 'J': 1, 'T': 0, 'X': 0, 'R': 0, 'L': 0},
       'U': {'C': 0, 'K': 0, 'F': 0, 'Q': 1, 'B': 0, 'N': 0, 'W': 0, 'H': 0, 'J': 1, 'T': 0, 'X': 0, 'R': 0, 'L': 1},
       'F': {'C': 0, 'K': 1, 'U': 0, 'Q': 0, 'B': 1, 'N': 0, 'W': 0, 'H': 0, 'J': 0, 'T': 1, 'X': 0, 'R': 1, 'L': 0},
       'Q': {'C': 0, 'K': 1, 'U': 1, 'F': 1, 'B': 0, 'N': 0, 'W': 0, 'H': 0, 'J': 0, 'T': 1, 'X': 0, 'R': 1, 'L': 1},
       'B': {'C': 1, 'K': 0, 'U': 0, 'F': 0, 'Q': 1, 'N': 0, 'W': 0, 'H': 0, 'J': 0, 'T': 0, 'X': 1, 'R': 0, 'L': 0},
       'N': {'C': 1, 'K': 0, 'U': 0, 'F': 1, 'Q': 0, 'B': 0, 'W': 1, 'H': 1, 'J': 0, 'T': 0, 'X': 0, 'R': 0, 'L': 0},
       'W': {'C': 0, 'K': 0, 'U': 1, 'F': 0, 'Q': 0, 'B': 0, 'N': 0, 'H': 0, 'J': 0, 'T': 0, 'X': 0, 'R': 0, 'L': 1},
       'H': {'C': 0, 'K': 0, 'U': 0, 'F': 0, 'Q': 1, 'B': 0, 'N': 0, 'W': 0, 'J': 0, 'T': 1, 'X': 1, 'R': 0, 'L': 0},
       'J': {'C': 1, 'K': 1, 'U': 0, 'F': 0, 'Q': 1, 'B': 1, 'N': 0, 'W': 0, 'H': 0, 'T': 0, 'X': 0, 'R': 0, 'L': 0},
       'T': {'C': 0, 'K': 0, 'U': 0, 'F': 1, 'Q': 0, 'B': 0, 'N': 1, 'W': 0, 'H': 0, 'J': 0, 'X': 1, 'R': 0, 'L': 0},
       'X': {'C': 0, 'K': 1, 'U': 0, 'F': 1, 'Q': 1, 'B': 0, 'N': 0, 'W': 0, 'H': 1, 'J': 0, 'T': 0, 'R': 0, 'L': 0},
       'R': {'C': 0, 'K': 0, 'U': 1, 'F': 0, 'Q': 0, 'B': 1, 'N': 0, 'W': 0, 'H': 1, 'J': 0, 'T': 1, 'X': 0, 'L': 0},
       'L': {'C': 0, 'K': 0, 'U': 1, 'F': 0, 'Q': 0, 'B': 0, 'N': 1, 'W': 1, 'H': 1, 'J': 0, 'T': 0, 'X': 0, 'R': 0}
   }
  
   # Define the initial state as the starting city
   initial_state = 'J'
   # Define the goal state as visiting city F and L twice
   goal_state = ['F', 'F', 'L', 'L']
  
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   queue = [(0, 0, [initial_state], initial_state)]
  
   while queue:
       _, g, path, current_city = heapq.heappop(queue)
      
       # If the current city is one of the goal cities, remove it from the goal list
       if current_city in goal_state:
           goal_state.remove(current_city)
          
       # If we have visited all the goal cities twice, return the path
       if not goal_state:
           return path
          
       # Generate all possible actions from the current state, which includes moving to any city connected to the current city
       for city, connected in adjacency_matrix[current_city].items():
           if connected == 1 and city not in path:
               new_path = path + [city]
               new_cost = g + 1
               # Calculate the heuristic cost as the number of remaining goal cities to visit
               h = len(goal_state)
               heapq.heappush(queue, (new_cost + h, new_cost, new_path, city))
  
   return None


print(a_star())
