
import heapq


def initialize():
   # Define the adjacency matrix representing the connections between cities
   adjacency_matrix = [[0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                       [1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
                       [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                       [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                       [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
                       [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
                       [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                       [0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0]]
  
   # Encoding other variables given in the problem statement
   start_city = 'Q'
   target_cities = ['K', 'Y']
   num_cities = 11


   # Initialize a dictionary to store the cost of reaching each visited city
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
       _, g, actions, current_city = heapq.heappop(queue)


       # If the current city is one of the target cities, check if we have visited both target cities twice and return the path taken
       if current_city in target_cities:
           if actions.count(target_cities[0]) == 2 and actions.count(target_cities[1]) == 2:
               return actions


       # Generate all valid actions from the current city, which includes moving to any city directly connected by a road
       for next_city in range(num_cities):
           if adjacency_matrix[current_city][next_city] == 1:
               # The actions is valid, generate the new state
               new_cost = g + 1
               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of not-yet-visited cities
               if next_city not in visited_costs or new_cost < visited_costs[next_city]:
                   visited_costs[next_city] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(next_city, target_cities), new_cost, actions + [next_city], next_city))
                  
   return None


def heuristic(city, target_cities):
   # An admissible and consistent heuristic is the sum of the distances from the current city to the target cities, as we aim to minimize the total distance traveled
   # The heuristic is admissible because it never overestimates the cost to reach the target cities, as the sum of the distances is always less than or equal to the actual cost
   # The heuristic is consistent because the cost of moving from one city to another is always 1, which is exactly the decrease in the heuristic estimate if the next city is closer to the target cities
   h = sum(abs(city - target) for target in target_cities)
   return h


print(a_star())
