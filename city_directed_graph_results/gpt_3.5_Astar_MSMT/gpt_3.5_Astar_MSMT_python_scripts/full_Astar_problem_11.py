
import heapq


def initialize():
   # Define the adjacency matrix representing the connections between cities
   adjacency_matrix = [[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                       [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
                       [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                       [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
                       [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                       [0, 0, 1, 1, 1, 0, 0, 1, 1, 0]]
   cities = ['Q', 'T', 'A', 'X', 'M', 'Y', 'Z', 'B', 'S', 'E']
   start_city = 'Q'
   end_cities = ['T', 'E']
   num_cities = len(cities)


   visited_costs = {}
   visited_costs[start_city] = 0


   queue = [(0, 0, [], start_city)]
  
   return adjacency_matrix, cities, start_city, end_cities, num_cities, visited_costs, queue
  
def a_star():
  
   adjacency_matrix, cities, start_city, end_cities, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, actions, current_city = heapq.heappop(queue)


       # If we have visited both destination cities twice, return the path
       if all(actions.count(city) == 2 for city in end_cities):
           return actions + [current_city]


       # Generate all possible actions from the current city, which includes moving to any city connected by a one-way road
       for i in range(num_cities):
           if adjacency_matrix[cities.index(current_city)][i] == 1:
               # Check if the new city is not already visited
               if actions.count(cities[i]) < 1:
                   new_cost = g + 1
                   new_actions = actions + [current_city]
                   # If we have visited both destination cities once, mark them as visited
                   if cities[i] in end_cities:
                       if actions.count(cities[i]) == 1:
                           new_actions.append(cities[i])
                   # Add the new city to the queue with the updated cost and actions
                   heapq.heappush(queue, (new_cost, new_cost, new_actions, cities[i]))
   return None


print(a_star())
