
import heapq


def a_star():
   # Define the adjacency matrix as a dictionary with city names as keys and a list of connected cities as values
   adjacency_matrix = {
       'G': ['R', 'K'],
       'J': ['G', 'Y', 'K'],
       'Y': ['G', 'R', 'F'],
       'Q': ['F', 'K'],
       'C': ['G', 'J', 'K'],
       'D': ['G', 'K', 'H'],
       'R': ['J', 'Y', 'F', 'H'],
       'F': ['K', 'H'],
       'K': ['G', 'Y', 'F', 'H', 'N'],
       'H': ['J', 'R', 'N'],
       'N': ['J', 'R', 'C']
   }
   start_city = 'Q'
   goal_cities = ['K', 'Y']
  
   # Initialize a dictionary to store the cost of reaching each visited city
   visited_costs = {}
   visited_costs[start_city] = 0

   # Initialize a priority queue of cities not yet visited, with the start city as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the goal
   # Record the path taken to reach each city in a list; no path taken to reach the start city
   queue = [(0, 0, [start_city], start_city)]

   # While there are un-visited cities
   while queue:
       _, g, path, current_city = heapq.heappop(queue)

       # Check if the current city is one of the goal cities
       if current_city in goal_cities:
           # If we have visited both goal cities twice, return the path taken
           if path.count('K') == 2 and path.count('Y') == 2:
               return path

       # Generate all valid actions from the current city, which includes moving to any connected city
       for next_city in adjacency_matrix[current_city]:
           # Calculate the cost to reach the next city
           new_cost = g + 1
           # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of not-yet-visited cities
           if next_city not in visited_costs or new_cost < visited_costs[next_city]:
               visited_costs[next_city] = new_cost
               # Calculate the heuristic cost as the number of goal cities not visited twice
               h = 2 - path.count('K') + 2 - path.count('Y')
               heapq.heappush(queue, (new_cost + h, new_cost, path + [next_city], next_city))
              
   return None


print(a_star())
