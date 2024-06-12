
import heapq


def a_star():
   # Define the adjacency matrix as a dictionary of dictionaries, where the keys are the city names and the values are dictionaries representing the connections to other cities
   adjacency_matrix = {
       'A': {'Q': 1, 'S': 1, 'O': 1, 'N': 1, 'V': 0, 'I': 0, 'X': 0, 'D': 0, 'B': 1, 'E': 0, 'Y': 0},
       'Q': {'A': 1, 'N': 1, 'B': 1},
       'S': {'A': 1, 'O': 1, 'N': 1, 'B': 1},
       'O': {'A': 1, 'S': 1, 'N': 1, 'D': 1, 'B': 1},
       'N': {'Q': 1, 'S': 1, 'O': 1, 'V': 1, 'I': 1, 'X': 1, 'D': 1, 'B': 0, 'E': 0, 'Y': 0},
       'V': {'A': 1, 'Q': 1, 'D': 1},
       'I': {'X': 1},
       'X': {'A': 1, 'Q': 1, 'S': 1, 'N': 1, 'O': 1, 'D': 1, 'B': 1, 'E': 1, 'Y': 1},
       'D': {'Q': 1, 'S': 1, 'O': 1, 'N': 1, 'B': 1},
       'B': {'O': 1, 'N': 1, 'V': 1, 'D': 1, 'E': 1, 'Y': 1},
       'E': {'A': 1, 'Q': 1, 'S': 1, 'N': 1, 'O': 1, 'D': 1, 'B': 1, 'Y': 1},
       'Y': {'A': 1, 'S': 1, 'N': 1, 'V': 1, 'D': 1, 'B': 1, 'E': 1}
   }
  
   # Define the initial state, which is the city 'I'
   initial_state = 'I'
   # Define the goal state, which is to visit cities 'A' and 'X' twice each
   goal_state = ['A', 'A', 'X', 'X']
  
   # Initialize a dictionary to store the cost of reaching each visited city
   visited_costs = {}
   visited_costs[initial_state] = 0
  
   # Initialize a priority queue of cities not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the goal
   queue = [(0, 0, [initial_state], initial_state)]
  
   # While there are un-visited cities
   while queue:
       _, g, path, current_city = heapq.heappop(queue)
      
       # If the current city is one of the goal cities and it has been visited twice, return the path
       if path.count(current_city) == 2 and current_city in goal_state:
           return path
      
       # Generate all possible actions from the current city, which includes moving to any city connected by a road
       for neighbor, cost in adjacency_matrix[current_city].items():
           # Check if the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of not-yet-visited cities
           if neighbor not in visited_costs or g + cost < visited_costs[neighbor]:
               visited_costs[neighbor] = g + cost
               heapq.heappush(queue, (g + cost + heuristic(neighbor, goal_state), g + cost, path + [neighbor], neighbor))
  
   return None


def heuristic(city, goal_state):
   # The heuristic function is the number of cities left to visit in the goal state, as we want to minimize the number of cities left to visit
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the number of cities left to visit is always less than or equal to the actual cost
   # The heuristic is consistent because the cost of moving to a neighboring city is always 1, which is exactly the decrease in the number of cities left to visit, if the city is moved towards the goal state, otherwise the estimated cost of the successor node is the same or higher
   return len([city for city in goal_state if city not in goal_state])


print(a_star())
