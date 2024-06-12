
import heapq


def initialize():
   # Define the adjacency matrix representing the connections between cities
   adjacency_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                       [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                       [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
                       [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                       [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]]
  
   # Encoding other variables given in the problem statement
   start_city = 'F'
   target_cities = ['I', 'N']
   num_cities = 11


   visited_costs = {}
   visited_costs[start_city] = 0


   queue = [(0, 0, [], start_city)]
  
   return adjacency_matrix, start_city, target_cities, num_cities, visited_costs, queue
  
def a_star():
  
   adjacency_matrix, start_city, target_cities, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, actions, current_city = heapq.heappop(queue)


       # If we have visited both target cities twice, return the actions taken
       if all(actions.count(city) == 2 for city in target_cities):
           return actions


       # Generate all possible actions from the current city, which includes moving to a city connected by a road
       for next_city in range(num_cities):
           if adjacency_matrix[current_city][next_city] == 1:
               # Generate the new state
               new_cost = g + 1
               if new_city not in visited_costs or new_cost < visited_costs[new_city]:
                   visited_costs[new_city] = new_cost
                   heapq.heappush(queue, (new_cost, new_cost, actions + [next_city], next_city))
   return None


print(a_star())
