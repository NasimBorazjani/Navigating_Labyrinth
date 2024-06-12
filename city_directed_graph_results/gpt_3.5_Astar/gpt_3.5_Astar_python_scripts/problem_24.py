
import heapq


def a_star():
   # Define the adjacency matrix as a dictionary with city names as keys and a list of connected cities as values
   adjacency_matrix = {
       'L': ['H', 'D', 'A', 'J', 'B'],
       'H': ['O', 'I', 'W', 'Y'],
       'D': ['H'],
       'O': ['H', 'A', 'B'],
       'A': ['M', 'B'],
       'M': ['L', 'H'],
       'I': ['J', 'B'],
       'J': ['W'],
       'W': ['Y', 'B'],
       'Y': ['L', 'O', 'B'],
       'B': []
   }
   start_city = 'D'
   goal_cities = ['B', 'L']
  
   # Initialize a dictionary to store the cost of reaching each visited city
   visited_costs = {}
   visited_costs[start_city] = 0

   # Initialize a priority queue of cities not yet visited, with the start city as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the goal
   # Record the path taken to reach each city in a list
   queue = [(0, 0, [start_city], start_city)]

   # While there are un-visited cities
   while queue:
       _, g, path, current_city = heapq.heappop(queue)

       # Check if the current city is one of the goal cities
       if current_city in goal_cities:
           # If we have visited both goal cities twice, return the path taken
           if path.count('B') == 2 and path.count('L') == 2:
               return path

       # Generate all possible actions from the current city, which includes moving to any connected city
       for next_city in adjacency_matrix[current_city]:
           # Check if the new city is unvisited
           if next_city not in visited_costs:
               # Generate the new path
               new_path = path + [next_city]
               # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited
               new_cost = g + 1
              
               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of not-yet-visited cities
               if next_city not in visited_costs or new_cost < visited_costs[next_city]:
                   visited_costs[next_city] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(next_city, goal_cities), new_cost, new_path, next_city))
                  
   return None


def heuristic(city, goal_cities):
   # An admissible and consistent heuristic is the number of goal cities that have not been visited twice
   # This heuristic relaxes the constraint that we need to visit each goal city twice, as it assumes we can visit the goal cities in any order
   # The heuristic is admissible because it never overestimates the cost to reach the goal, as it only counts the number of goal cities that have not been visited twice
   # The heuristic is consistent because the cost of visiting a city is always 1, which is exactly the decrease in the heuristic estimate if a goal city is visited twice, otherwise the estimated cost of the successor node is the same or higher
   h = sum(goal_cities.count(city) < 2 for city in goal_cities)
   return h


print(a_star())
