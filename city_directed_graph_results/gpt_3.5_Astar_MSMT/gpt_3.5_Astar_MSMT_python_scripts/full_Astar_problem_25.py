
import heapq

def initialize():
   # Define the adjacency matrix representing the connections between cities
   adjacency_matrix = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
                       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                       [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                       [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
                       [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
                       [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                       [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0]]

   # Define the cities and their indices
   cities = ['O', 'M', 'Y', 'J', 'Z', 'V', 'K', 'F', 'X', 'L', 'R']
   start_city = 'M'
   end_cities = ['X', 'Y']

   # Initialize a dictionary to store the cost of reaching each visited city
   visited_costs = {}
   visited_costs[start_city] = 0

   # Initialize a priority queue of cities not yet visited, with the start city as the first element
   # Record the path taken to reach each city in a list; no path taken to reach the start city
   queue = [(0, 0, [start_city], start_city)]

   return adjacency_matrix, cities, start_city, end_cities, visited_costs, queue

def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the adjacency matrix, cities, start city, and end cities)
   adjacency_matrix, cities, start_city, end_cities, visited_costs, queue = initialize()

   while queue:
       _, g, path, current_city = heapq.heappop(queue)

       # Check if the current city is one of the end cities and we have visited both of them twice
       if current_city in end_cities and path.count(current_city) == 2:
           return path

       # Generate all possible actions from the current city, which includes moving to any connected city that has not been visited yet
       for i, connected in enumerate(adjacency_matrix[cities.index(current_city)]):
           if connected == 1 and cities[i] not in path:
               new_path = path + [cities[i]]
               new_cost = g + 1

               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of not-yet-visited cities
               if cities[i] not in visited_costs or new_cost < visited_costs[cities[i]]:
                   visited_costs[cities[i]] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(cities[i], end_cities), new_cost, new_path, cities[i]))

   return None

def heuristic(city, end_cities):
   # An admissible heuristic is the minimum distance from the current city to the nearest end city that has not been visited twice
   # This heuristic assumes that the path to the goal state will go through the nearest end city that has not been visited twice
   # It is admissible because it never overestimates the cost to reach the goal, as the actual cost to reach the goal is at least as much as the heuristic estimate
   # The heuristic is consistent because the cost of moving from one city to a neighboring city is always 1, which is exactly the decrease in the heuristic estimate if the neighboring city is closer to the nearest end city
   distances = {city: {'X': 3, 'Y': 2, 'M': 1, 'O': 2, 'J': 3, 'Z': 2, 'V': 1, 'K': 1, 'F': 2, 'L': 2, 'R': 3}}
   return min([distances[city][end_city] for end_city in end_cities if end_city not in path])

print(a_star())
