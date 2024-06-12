
import heapq

def initialize():
   # Define the adjacency matrix representing the connections between cities
   adjacency_matrix = [[0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
                       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
                       [0, 0, 1, 0, 1, 1, 0, 0, 1, 1],
                       [1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
                       [0, 0, 0, 0, 1, 0, 1, 0, 0, 0]]
   cities = ['G', 'X', 'R', 'L', 'Y', 'E', 'V', 'T', 'B', 'H']
   start_city = 'H'
   target_cities = ['E', 'X']
   num_target_visits = 2

   visited_costs = {}
   visited_costs[start_city] = 0

   queue = [(0, 0, [], start_city)]

   return adjacency_matrix, cities, start_city, target_cities, num_target_visits, visited_costs, queue

def a_star():
  
   adjacency_matrix, cities, start_city, target_cities, num_target_visits, visited_costs, queue = initialize()

   while queue:
       _, g, actions, current_city = heapq.heappop(queue)

       # Check if the current city is one of the target cities
       if current_city in target_cities:
           # If we have visited the target city the required number of times, return the actions taken
           if actions.count(current_city) == num_target_visits:
               return actions

       # Generate all possible actions from the current city, which includes moving to any city connected by a road
       city_index = cities.index(current_city)
       for i in range(len(cities)):
           if adjacency_matrix[city_index][i] == 1 and cities[i] not in actions:
               new_city = cities[i]
               new_cost = g + 1

               if new_city not in visited_costs or new_cost < visited_costs[new_city]:
                   visited_costs[new_city] = new_cost
                   heapq.heappush(queue, (new_cost, new_cost, actions + [new_city], new_city))
  
   return None

print(a_star())
