
import heapq


def initialize():
   # Define the adjacency matrix representing the connections between cities
   adjacency_matrix = [[0, 0, 1, 1, 0, 0, 1, 1, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                       [0, 1, 0, 1, 0, 1, 1, 0, 0, 1],
                       [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
                       [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
   cities = ['K', 'B', 'Z', 'S', 'X', 'H', 'O', 'E', 'U', 'V']
   start_city = 'H'
   target_cities = ['K', 'Z']
   num_targets = 2


   visited_costs = {}
   visited_costs[start_city] = 0


   queue = [(0, 0, [], start_city)]
  
   return adjacency_matrix, cities, start_city, target_cities, num_targets, visited_costs, queue
  
def a_star():
  
   adjacency_matrix, cities, start_city, target_cities, num_targets, visited_costs, queue = initialize()


   while queue:
       _, g, actions, current_city = heapq.heappop(queue)


       # If we have visited both target cities twice, return the actions taken
       if all(actions.count(target) == 2 for target in target_cities):
           return actions


       # Generate all possible actions from the current city, which includes moving to any city connected by a road
       for i, connected in enumerate(adjacency_matrix[cities.index(current_city)]):
           if connected == 1 and cities[i] != start_city and (actions.count(cities[i]) < 1 or (actions.count(cities[i]) == 1 and cities[i] in target_cities)):
               # Generate the new state
               new_city = cities[i]
               new_cost = g + 1
              
               if new_city not in visited_costs or new_cost < visited_costs[new_city]:
                   visited_costs[new_city] = new_cost
                   heapq.heappush(queue, (new_cost, new_cost, actions + [new_city], new_city))
   return None


print(a_star())
