
import heapq


def initialize():
   # Define the adjacency matrix representing the connections between cities
   adjacency_matrix = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                       [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
                       [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                       [1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                       [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
                       [1, 1, 0, 0, 0, 0, 1, 0, 1, 1],
                       [1, 1, 0, 1, 0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 1, 1, 0, 0, 0, 1, 0]]
   cities = ['O', 'T', 'I', 'F', 'A', 'M', 'X', 'Y', 'R', 'G']
   start_city = 'M'
   goal_cities = ['A', 'R']
   num_cities = len(cities)


   visited_costs = {}
   visited_costs[start_city] = 0


   queue = []
   # No actions taken in the initial state
   heapq.heappush(queue, (0, 0, [], start_city))
  
   return adjacency_matrix, cities, start_city, goal_cities, num_cities, visited_costs, queue
  
def a_star():
  
   adjacency_matrix, cities, start_city, goal_cities, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, actions, current_city = heapq.heappop(queue)


       # If we have visited both destination cities twice, return the path
       if all(actions.count(city) == 2 for city in goal_cities):
           return actions + [current_city]


       # Generate all possible actions from the current city, which includes moving to any city connected by a road
       for i in range(num_cities):
           if adjacency_matrix[cities.index(current_city)][i] == 1:
               new_city = cities[i]
               # Check if the new city has not been visited before
               if new_city not in actions:
                   # Generate the new state
                   new_actions = actions + [current_city]
                   new_cost = g + 1
                  
                   if new_city not in visited_costs or new_cost < visited_costs[new_city]:
                       visited_costs[new_city] = new_cost
                       heapq.heappush(queue, (new_cost, new_cost, new_actions, new_city))
   return None


print(a_star())
