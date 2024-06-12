
import heapq


def a_star():
   # Define the adjacency matrix as a dictionary where the keys are the cities and the values are dictionaries of connected cities
   adjacency_matrix = {
       'Z': {'P': 1, 'B': 1, 'Y': 1, 'C': 1},
       'H': {'P': 1, 'L': 1, 'Q': 1, 'Y': 1, 'V': 1, 'C': 1},
       'M': {'B': 1, 'Q': 1},
       'P': {'B': 1, 'I': 1, 'C': 1},
       'B': {'I': 1},
       'I': {'P': 1, 'L': 1, 'Q': 1, 'C': 1},
       'E': {'Z': 1, 'H': 1, 'L': 1},
       'L': {'Z': 1, 'H': 1, 'I': 1, 'Q': 1},
       'Q': {'H': 1, 'P': 1, 'L': 1},
       'Y': {'L': 1, 'V': 1},
       'V': {'M': 1},
       'C': {'B': 1, 'Y': 1}
   }
   start_city = 'C'
   goal_cities = ['M', 'Q']
  
   # Initialize a dictionary to store the cost of reaching each visited city
   visited_costs = {}
   visited_costs[start_city] = 0

   # Initialize a priority queue of cities not yet visited, with the start city as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the goal
   # Record the path taken to reach each city in a list; no path taken to reach the start city
   queue = [(0, 0, [start_city], start_city)]

   # While there are un-visited cities
   while queue:
       _, g, path, current_city = heapq.heappop(queue)

       # If we have visited both destination cities twice, return the path taken
       if path.count('M') == 2 and path.count('Q') == 2:
           return path

       # Generate all possible actions from the current city, which includes moving to any connected city
       for neighbor in adjacency_matrix[current_city]:
           # Calculate the new cost to reach the neighbor city
           new_cost = g + 1
           # Calculate the heuristic cost, which is the number of destination cities not yet visited twice
           h = 4 - path.count('M') - path.count('Q')
           # If the neighbor city is not visited or we found a new path with a lower cost to reach this city, add it to the queue of not-yet-visited cities
           if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
               visited_costs[neighbor] = new_cost
               heapq.heappush(queue, (new_cost + h, new_cost, path + [neighbor], neighbor))
              
   return None


print(a_star())
