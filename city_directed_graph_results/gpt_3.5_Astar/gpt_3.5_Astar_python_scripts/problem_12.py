
import heapq


def a_star():
   # Define the adjacency matrix as a dictionary with city names as keys and a list of connected cities as values
   adjacency_matrix = {
       'S': ['T', 'B', 'N'],
       'T': ['V'],
       'R': ['S', 'T', 'I', 'N'],
       'A': ['S', 'R', 'V', 'N'],
       'L': ['A', 'V', 'P', 'N'],
       'B': ['S', 'V'],
       'V': ['S', 'T', 'R', 'A', 'I', 'P', 'N'],
       'I': ['L'],
       'P': ['L'],
       'N': ['L', 'I']
   }
   start_city = 'B'
   goal_cities = ['V', 'L']
  
   # Initialize a dictionary to store the cost of reaching each visited city
   visited_costs = {}
   visited_costs[start_city] = 0

   # Initialize a priority queue of cities not yet visited, with the start city as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the goal
   # Record the path taken to reach each city in a list; no path taken to reach the start city
   queue = [(0, 0, [start_city], start_city)]

   # While there are un-visited cities
   while queue:
       _, g, path, current_city = heapq.heappop(queue)

       # If the current city is one of the goal cities and we have visited both goal cities twice, return the path taken
       if current_city in goal_cities and path.count(current_city) == 2:
           return path

       # Generate all possible actions from the current city, which includes moving to any of the connected cities
       for neighbor in adjacency_matrix[current_city]:
           # Check if the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of not-yet-visited cities
           new_cost = g + 1
           if neighbor not in visited_costs or new_cost < visited_costs[neighbor]:
               visited_costs[neighbor] = new_cost
               # The heuristic is the number of goal cities not yet visited twice
               h = len([city for city in goal_cities if path.count(city) < 2])
               heapq.heappush(queue, (new_cost + h, new_cost, path + [neighbor], neighbor))
                  
   return None


print(a_star())
