
import heapq

def initialize():
   # Define the adjacency matrix representing the connections between cities
   adjacency_matrix = [[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
                       [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                       [1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                       [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
                       [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
                       [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                       [1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0]]
  
   # Encoding other variables given in the problem statement
   num_cities = 11
   start_city = 'D'
   target_cities = ['G', 'Q']
   target_count = 2


   visited_costs = {}
   visited_costs[start_city] = 0


   queue = []
   # No actions taken in the initial state
   heapq.heappush(queue, (0, 0, [], start_city))
  
   return adjacency_matrix, num_cities, start_city, target_cities, target_count, visited_costs, queue
  
def a_star():
  
   adjacency_matrix, num_cities, start_city, target_cities, target_count, visited_costs, queue = initialize()


   while queue:
       _, g, actions, current_city = heapq.heappop(queue)


       # Check if the current city is one of the target cities
       if current_city in target_cities:
           # Decrease the target count
           target_count -= 1
           # If we have visited both target cities twice, return the actions taken
           if target_count == 0:
               return actions


       # Generate all possible actions from the current city, which includes moving to any city connected by a one-way road
       for next_city in range(num_cities):
           if adjacency_matrix[current_city][next_city] == 1:
               # Generate the new state
               new_cost = g + 1
               # If the new city is unvisited or we found a new path with a lower cost to reach this city, add it to the queue of unvisited cities
               if next_city not in visited_costs or new_cost < visited_costs[next_city]:
                   visited_costs[next_city] = new_cost
                   heapq.heappush(queue, (new_cost, new_cost, actions + [next_city], next_city))
   return None


print(a_star())
