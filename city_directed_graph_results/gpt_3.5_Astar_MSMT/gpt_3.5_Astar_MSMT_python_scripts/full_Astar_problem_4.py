
import heapq


def initialize():
   # Define the adjacency matrix representing the connections between cities
   adjacency_matrix = [[0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
                       [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                       [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                       [0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                       [1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                       [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                       [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                       [0, 1, 0, 0, 0, 1, 1, 0, 0, 0]]
  
   # Encoding other variables given in the problem statement
   start_city = 'L'
   target_cities = ['D', 'N']
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


   while queue:
       _, g, actions, current_city = heapq.heappop(queue)


       # If we have visited both target cities twice, return the path taken
       if all(actions.count(city) == 2 for city in target_cities):
           return actions


       # Generate all possible actions from the current city, which includes moving to any city connected by a one-way road
       for next_city in range(num_cities):
           if adjacency_matrix[current_city][next_city] == 1:
               # Generate the new state
               new_cost = g + 1
               new_actions = actions + [next_city]
              
               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of un-visited cities
               if next_city not in visited_costs or new_cost < visited_costs[next_city]:
                   visited_costs[next_city] = new_cost
                   # The heuristic is the number of target cities not visited twice yet, as we want to minimize the number of moves to reach the goal state
                   h = len([city for city in target_cities if new_actions.count(city) < 2])
                   heapq.heappush(queue, (new_cost + h, new_cost, new_actions, next_city))
   return None


print(a_star())
