
import heapq


def initialize():
   # Define the adjacency matrix representing the connections between cities
   adjacency_matrix = [[0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                       [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
                       [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                       [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
                       [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
                       [1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0]]
   cities = ['R', 'L', 'F', 'E', 'D', 'Q', 'G', 'U', 'H', 'T', 'Z', 'A']
   start_city = 'F'
   target_cities = ['R', 'A']
   num_cities = len(cities)


   visited_costs = {}
   visited_costs[start_city] = 0


   queue = [(0, 0, [], start_city)]
  
   return adjacency_matrix, cities, start_city, target_cities, num_cities, visited_costs, queue
  
def a_star():
  
   adjacency_matrix, cities, start_city, target_cities, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, actions, current_city = heapq.heappop(queue)


       # If we have visited both target cities twice, return the path
       if all(actions.count(city) == 2 for city in target_cities):
           return actions + [current_city]


       # Generate all possible actions from the current city, which includes moving to any city connected by a one-way road
       current_city_index = cities.index(current_city)
       for i in range(num_cities):
           if adjacency_matrix[current_city_index][i] == 1 and cities[i] not in actions:
               new_cost = g + 1
               new_actions = actions + [current_city]
               # If the city is one of the target cities, append it to the actions list
               if cities[i] in target_cities:
                   new_actions.append(cities[i])
               heapq.heappush(queue, (new_cost, new_cost, new_actions, cities[i]))
   return None


print(a_star())
