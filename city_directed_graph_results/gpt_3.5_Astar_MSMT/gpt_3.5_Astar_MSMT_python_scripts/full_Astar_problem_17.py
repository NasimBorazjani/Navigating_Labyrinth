
import heapq


def initialize():
   # Define the adjacency matrix representing the connections between cities
   adjacency_matrix = [[0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                       [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                       [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
                       [0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 1, 1, 0]]
  
   # Encoding other variables given in the problem statement
   start_city = 'V'
   target_cities = ['Y', 'I']
   num_cities = len(adjacency_matrix)
   visited_costs = {}
   visited_costs[start_city] = 0


   # Initialize a priority queue of cities not yet visited, with the start city as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the target cities
   # Record the path taken to get to each city in a list; no path taken to reach the start city
   queue = [(0, 0, [], start_city)]
  
   return adjacency_matrix, start_city, target_cities, num_cities, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the adjacency matrix, start city, target cities, and number of cities)
   adjacency_matrix, start_city, target_cities, num_cities, visited_costs, queue = initialize()


   # While there are un-visited cities
   while queue:
       # Pop the city with the lowest sum of the cost so far and estimated cost to the target cities from the queue
       _, g, path, current_city = heapq.heappop(queue)


       # If the current city is one of the target cities, check if we have visited both target cities twice
       if current_city in target_cities:
           if path.count(target_cities[0]) == 2 and path.count(target_cities[1]) == 2:
               return path


       # Generate all possible actions from the current city, which includes moving to any city directly connected by a road
       for next_city in range(num_cities):
           if adjacency_matrix[current_city][next_city] == 1:
               # Generate the new path
               new_path = path + [next_city]
               # The cost so far is the number of cities visited, as our objective is to minimize the number of cities visited
               new_cost = g + 1
              
               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of not-yet-visited cities
               if next_city not in visited_costs or new_cost < visited_costs[next_city]:
                   visited_costs[next_city] = new_cost
                   # Calculate the heuristic cost to reach the target cities by counting the number of target cities not visited twice
                   h = len([city for city in target_cities if path.count(city) < 2])
                   heapq.heappush(queue, (new_cost + h, new_cost, new_path, next_city))
                  
   return None


print(a_star())
