
import heapq


def initialize():
   # Define the adjacency matrix representing the connections between cities
   adjacency_matrix = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                       [0, 0, 0, 1, 1, 0, 0, 1, 1, 1],
                       [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                       [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                       [0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
                       [0, 1, 0, 1, 0, 0, 1, 1, 0, 1],
                       [1, 1, 1, 0, 0, 1, 0, 0, 0, 0]]
  
   # Encoding other variables given in the problem statement
   start_city = 'Q'
   target_cities = ['P', 'E']
   num_cities = 10


   # Initialize a dictionary to store the cost of reaching each visited city
   visited_costs = {}
   visited_costs[start_city] = 0


   # Initialize a priority queue of cities not yet visited, with the start city as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the target cities
   # Record the path taken to reach each city in a list; no path taken to reach the start city
   queue = [(0, 0, [start_city], start_city)]
  
   return adjacency_matrix, start_city, target_cities, num_cities, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the adjacency matrix, start city, target cities, and number of cities)
   adjacency_matrix, start_city, target_cities, num_cities, visited_costs, queue = initialize()


   # While there are un-visited cities
   while queue:
       # Pop the city with the lowest sum of the cost so far and estimated cost to the target cities from the queue
       _, g, path, current_city = heapq.heappop(queue)


       # If the current city is one of the target cities and has been visited twice, return the path taken
       if current_city in target_cities and path.count(current_city) == 2:
           return path


       # Generate all possible actions from the current city, which includes moving to any city directly connected by a road
       for next_city in range(num_cities):
           if adjacency_matrix[num_cities.index(current_city)][next_city] == 1:
               # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited to reach the target cities
               new_cost = g + 1
               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of not-yet-visited cities
               if num_cities[next_city] not in visited_costs or new_cost < visited_costs[num_cities[next_city]]:
                   visited_costs[num_cities[next_city]] = new_cost
                   # Calculate the heuristic cost to reach the target cities from the new city
                   h = heuristic(num_cities[next_city], target_cities)
                   heapq.heappush(queue, (new_cost + h, new_cost, path + [num_cities[next_city]], num_cities[next_city]))
                  
   return None


def heuristic(city, target_cities):
   # An admissible and consistent heuristic is the minimum distance to the nearest target city from the current city
   # This heuristic relaxes the constraint that we need to visit each target city twice, as it only considers the distance to the nearest target city
   # It is admissible because it never overestimates the cost to reach the target cities, as the actual cost can only be equal or less than the distance to the nearest target city
   # It is consistent because the cost of moving from one city to another is always 1, which is exactly the decrease in the heuristic estimate if the new city is closer to the target city, otherwise the estimated cost of the successor node is the same or higher
   distances = {city: float('inf') for city in target_cities}
   distances[city] = 0
   for target_city in target_cities:
       if city != target_city:
           # Calculate the distance to the target city based on the index of the cities in the adjacency matrix
           distance = abs(target_cities.index(city) - target_cities.index(target_city))
           distances[target_city] = min(distances[target_city], distance)
   return min(distances.values())


print(a_star())
