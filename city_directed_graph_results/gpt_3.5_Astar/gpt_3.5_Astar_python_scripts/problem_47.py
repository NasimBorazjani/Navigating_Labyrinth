
import heapq


def a_star():
   # Define the adjacency matrix as a dictionary of dictionaries, where the keys are the city names and the values are dictionaries representing the connections to other cities
   adjacency_matrix = {
       'Z': {'K': 1, 'S': 1},
       'O': {'F': 1},
       'F': {'O': 1, 'K': 1, 'B': 1, 'U': 1, 'D': 1},
       'M': {'Z': 1, 'F': 1, 'B': 1},
       'C': {'F': 1, 'U': 1, 'R': 1, 'J': 1},
       'K': {'O': 1, 'M': 1, 'U': 1},
       'B': {'F': 1, 'C': 1, 'D': 1},
       'U': {'M': 1, 'C': 1, 'D': 1, 'R': 1, 'J': 1},
       'D': {'K': 1, 'M': 1, 'U': 1},
       'R': {'F': 1, 'C': 1, 'S': 1},
       'S': {'C': 1, 'R': 1, 'J': 1},
       'J': {'F': 1, 'C': 1, 'S': 1}
   }
  
   # Define the initial state, which is the starting city 'Z'
   initial_state = 'Z'
   # Define the goal state, which is to visit cities 'C' and 'D' twice each
   goal_state = ['C', 'C', 'D', 'D']
  
   # Initialize a dictionary to store the cost of reaching each visited city
   visited_costs = {}
   visited_costs[initial_state] = 0
  
   # Initialize a priority queue of cities not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the goal
   queue = [(0, 0, [initial_state], initial_state)]
  
   # While there are un-visited cities
   while queue:
       _, g, path, current_city = heapq.heappop(queue)
      
       # If the current city is one of the goal cities, remove it from the goal list
       if current_city in goal_state:
           goal_state.remove(current_city)
          
           # If all goal cities have been visited twice, return the path
           if not goal_state:
               return path
          
       # Generate all possible actions from the current city, which includes moving to any city connected by a one-way road
       for neighbor, cost in adjacency_matrix[current_city].items():
           # Calculate the new cost to reach the neighbor city
           new_cost = g + cost
          
           # If the neighbor city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
           if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
               visited_costs[neighbor] = new_cost
               # Calculate the heuristic cost, which is the number of goal cities remaining to be visited
               h = len(goal_state)
               heapq.heappush(queue, (new_cost + h, new_cost, path + [neighbor], neighbor))
  
   return None


print(a_star())
