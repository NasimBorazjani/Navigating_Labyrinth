
import heapq


def a_star():
   # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries representing the connections to other cities
   adjacency_matrix = {
       'Q': {'Z': 1},
       'T': {'Q': 1, 'A': 1, 'X': 1},
       'A': {'M': 1},
       'X': {'M': 1, 'Z': 1, 'B': 1},
       'M': {'Q': 1, 'B': 1},
       'Y': {'T': 1, 'A': 1},
       'Z': {'M': 1, 'B': 1},
       'B': {'Q': 1, 'T': 1, 'A': 1},
       'S': {'T': 1, 'Y': 1, 'E': 1},
       'E': {'X': 1, 'Z': 1, 'B': 1}
   }
   start_city = 'Q'
   goal_cities = ['T', 'E']
  
   # Initialize a dictionary to store the cost of reaching each visited city
   visited_costs = {}
   visited_costs[start_city] = 0

   # Initialize a priority queue of cities not yet visited, with the start city as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the goal
   # Record the path taken to reach each city in a list
   queue = [(0, 0, [start_city], start_city)]

   # While there are un-visited cities
   while queue:
       _, g, path, current_city = heapq.heappop(queue)

       # If we have visited both destination cities twice, return the path
       if path.count('T') == 2 and path.count('E') == 2:
           return path

       # Generate all possible actions from the current city, which includes moving to any city connected by a road
       for neighbor in adjacency_matrix[current_city]:
           # Check if the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of not-yet-visited cities
           new_cost = g + 1
           if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
               visited_costs[neighbor] = new_cost
               # The heuristic is the number of steps to reach the nearest destination city from the current city
               h = min(path.count('T'), path.count('E'))
               heapq.heappush(queue, (new_cost + h, new_cost, path + [neighbor], neighbor))
              
   return None


print(a_star())
