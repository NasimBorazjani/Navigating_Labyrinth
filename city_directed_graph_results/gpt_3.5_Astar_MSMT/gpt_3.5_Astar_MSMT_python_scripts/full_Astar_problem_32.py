
import heapq

def initialize():
   # Define the adjacency matrix representing the connections between cities
   adjacency_matrix = [[0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
                       [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
                       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
                       [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
                       [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0]]
  
   # Encoding other variables given in the problem statement
   start_city = 'J'
   end_cities = ['D', 'E']
   num_cities = 11

   # Initialize a dictionary to store the cost of reaching each visited city
   visited_costs = {}
   visited_costs[start_city] = 0

   # Initialize a priority queue of cities not yet visited, with the start city as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the end cities
   # Record the path taken to reach each city in a list; no path taken to reach the start city
   queue = [(0, 0, [start_city], start_city)]
  
   return adjacency_matrix, start_city, end_cities, num_cities, visited_costs, queue
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the adjacency matrix, start city, end cities, and number of cities)
   adjacency_matrix, start_city, end_cities, num_cities, visited_costs, queue = initialize()

   while queue:
       _, g, path, city = heapq.heappop(queue)

       # If the current city is one of the end cities and it has been visited twice, return the path taken
       if city in end_cities and path.count(city) == 2:
           return path

       # Generate all possible actions from the current city, which includes moving to any city connected by a one-way road and not yet visited
       for next_city in range(num_cities):
           if adjacency_matrix[num_cities.index(city)][next_city] == 1 and num_cities[next_city] not in path:
               # Calculate the new cost to reach the next city
               new_cost = g + 1
               # Estimate the remaining cost to reach the end cities by counting the number of end cities not visited twice
               remaining_end_cities = [city for city in end_cities if path.count(city) < 2]
               h = len(remaining_end_cities)
               # If the new city is not in the visited cities or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
               if num_cities[next_city] not in visited_costs or new_cost < visited_costs[num_cities[next_city]]:
                   visited_costs[num_cities[next_city]] = new_cost
                   heapq.heappush(queue, (new_cost + h, new_cost, path + [num_cities[next_city]], num_cities[next_city]))
   return None

print(a_star())
