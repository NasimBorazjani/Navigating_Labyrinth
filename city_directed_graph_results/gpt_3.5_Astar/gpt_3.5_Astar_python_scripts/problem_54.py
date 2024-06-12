
import heapq


def a_star():
   # Define the adjacency matrix as a dictionary of dictionaries, where the keys are the city names and the values are dictionaries representing the connections to other cities
   adjacency_matrix = {
       'G': {'T': 1, 'K': 1, 'Y': 1, 'A': 1},
       'T': {'D': 1},
       'M': {'G': 1, 'T': 1},
       'U': {'G': 1, 'K': 1},
       'K': {'T': 1, 'Y': 1, 'D': 1, 'P': 1, 'S': 1},
       'Y': {'M': 1, 'U': 1, 'K': 1, 'D': 1},
       'D': {'Y': 1, 'A': 1, 'S': 1, 'I': 1},
       'A': {'G': 1, 'K': 1, 'Y': 1, 'P': 1},
       'P': {'M': 1, 'S': 1, 'I': 1},
       'R': {'A': 1, 'E': 1},
       'E': {'K': 1, 'P': 1},
       'S': {'T': 1, 'Y': 1, 'P': 1},
       'I': {'D': 1, 'K': 1}
   }
  
   # Define the initial state, which is the starting city 'R'
   initial_state = 'R'
   # Define the goal state, which is to visit cities 'A' and 'Y' twice each
   goal_state = ['A', 'A', 'Y', 'Y']
  
   # Initialize a dictionary to store the cost of reaching each visited city
   visited_costs = {}
   visited_costs[initial_state] = 0
  
   # Initialize a priority queue of cities not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the goal
   queue = [(0, 0, [initial_state], initial_state)]
  
   # While there are un-visited cities
   while queue:
       _, g, path, current_city = heapq.heappop(queue)
      
       # If the current city is one of the goal cities and it has been visited twice, remove it from the goal state list
       if current_city in goal_state:
           goal_state.remove(current_city)
           if not goal_state:
               return path
          
       # Generate all possible actions from the current city, which includes moving to any city connected by a one-way road
       for neighbor, cost in adjacency_matrix[current_city].items():
           new_cost = g + cost
           new_path = path + [neighbor]
          
           # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of not-yet-visited cities
           if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
               visited_costs[neighbor] = new_cost
               # The heuristic is the number of cities left to visit in the goal state list
               h = len(goal_state)
               heapq.heappush(queue, (new_cost + h, new_cost, new_path, neighbor))
              
   return None


print(a_star())
