
import heapq


def initialize():
   # Define the adjacency matrix representing the connections between cities
   adjacency_matrix = [[0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                       [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
                       [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                       [1, 0, 0, 1, 0, 0, 1, 0, 0, 0]]
  
   # Encoding other variables given in the problem statement
   start_city = 'Z'
   target_cities = ['B', 'H']
   num_cities = len(adjacency_matrix)


   # Initialize a dictionary to store the cost of reaching each visited city
   visited_costs = {}
   visited_costs[start_city] = 0


   # Initialize a priority queue of cities not yet visited, with the start city as the first element. The priority of each element is the cost to reach that city (g) + the estimate remaining cost (h) to reach the target cities
   # Record the path taken to reach each city in a list; no path taken to reach the start city
   queue = [(0, 0, [], start_city)]
  
   return adjacency_matrix, start_city, target_cities, num_cities, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the adjacency matrix, start city, target cities, and number of cities)
   adjacency_matrix, start_city, target_cities, num_cities, visited_costs, queue = initialize()


   # While there are un-visited cities
   while queue:
       # Pop the city with the lowest sum of the cost so far and estimated cost to the target cities from the queue
       _, g, path, current_city = heapq.heappop(queue)


       # If the current city is one of the target cities and it has been visited twice, return the path taken
       if current_city in target_cities and path.count(current_city) == 2:
           return path


       # Generate all possible actions from the current city, which includes moving to any city directly connected by a road
       for next_city in range(num_cities):
           if adjacency_matrix[current_city][next_city] == 1:
               # The cost to move to the next city is 1, as all roads have the same travel time
               new_cost = g + 1
               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of not-yet-visited cities
               if next_city not in visited_costs or new_cost < visited_costs[next_city]:
                   visited_costs[next_city] = new_cost
                   # The heuristic is the number of target cities not yet visited twice, as we want to minimize the number of moves to reach the target cities
                   h = len([city for city in target_cities if path.count(city) < 2])
                   heapq.heappush(queue, (new_cost + h, new_cost, path + [current_city], next_city))
                  
   return None


print(a_star())
