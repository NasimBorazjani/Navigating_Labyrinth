
import heapq


def initialize():
   # Define the adjacency matrix representing the connections between the cities
   adjacency_matrix = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
                       [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                       [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0],
                       [1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
                       [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                       [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0]]
   cities = ['R', 'S', 'W', 'B', 'P', 'G', 'Q', 'E', 'N', 'D', 'J']
   start_city = 'G'
   target_cities = ['S', 'E']
   num_visits = 2


   visited_costs = {}
   visited_costs[start_city] = 0


   queue = [(0, 0, [], start_city)]
  
   return adjacency_matrix, cities, start_city, target_cities, num_visits, visited_costs, queue
  
def a_star():
  
   adjacency_matrix, cities, start_city, target_cities, num_visits, visited_costs, queue = initialize()


   while queue:
       _, g, actions, current_city = heapq.heappop(queue)


       # Check if we have visited the target cities the required number of times
       if all(actions.count(target) == num_visits for target in target_cities):
           return actions


       # Generate all possible actions from the current city, which includes moving to any city that is directly connected and has not been visited yet
       for i, connected in enumerate(adjacency_matrix[cities.index(current_city)]):
           if connected == 1 and cities[i] not in actions:
               new_city = cities[i]
               new_cost = g + 1
              
               if new_city not in visited_costs or new_cost < visited_costs[new_city]:
                   visited_costs[new_city] = new_cost
                   # The heuristic is the number of target cities that have not been visited the required number of times
                   h = sum(actions.count(target) < num_visits for target in target_cities)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_city], new_city))
   return None


print(a_star())
