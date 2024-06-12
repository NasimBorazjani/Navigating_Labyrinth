
import heapq


def initialize():
   # Define the adjacency matrix as a dictionary of dictionaries, where the keys are the city names and the values are dictionaries representing the connections to other cities
   adjacency_matrix = {
       'Y': {'O': 1, 'R': 1, 'A': 1, 'U': 1, 'M': 1},
       'O': {'Q': 1},
       'Q': {'Y': 1, 'K': 1, 'M': 1},
       'X': {'Y': 1, 'Q': 1, 'R': 1, 'M': 1, 'A': 1},
       'K': {'O': 1, 'Q': 1},
       'R': {'K': 1},
       'A': {'Q': 1, 'X': 1, 'M': 1},
       'U': {'L': 1},
       'M': {'Q': 1, 'X': 1},
       'L': {'Y': 1}
   }
   start_city = 'U'
   goal_cities = ['A', 'X']
   num_visits = 2


   visited_costs = {}
   visited_costs[start_city] = 0


   queue = [(0, 0, [], start_city)]
  
   return adjacency_matrix, start_city, goal_cities, num_visits, visited_costs, queue
  
def a_star():
  
   adjacency_matrix, start_city, goal_cities, num_visits, visited_costs, queue = initialize()


   while queue:
       _, g, actions, current_city = heapq.heappop(queue)


       # If we have visited both destination cities twice, return the path
       if all(actions.count(city) == num_visits for city in goal_cities):
           return actions + [current_city]


       # Generate all possible actions from the current city, which includes moving to any city connected by a one-way road
       for neighbor_city, cost in adjacency_matrix[current_city].items():
           # Check if visiting the neighbor city is valid, ie we have not visited the city before
           if actions.count(neighbor_city) < num_visits:
               # Generate the new state
               new_actions = actions + [current_city]
               new_cost = g + cost
              
               if neighbor_city not in visited_costs or new_cost < visited_costs[neighbor_city]:
                   visited_costs[neighbor_city] = new_cost
                   heapq.heappush(queue, (new_cost, new_cost, new_actions, neighbor_city))
   return None


print(a_star())
