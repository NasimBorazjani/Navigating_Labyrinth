
import heapq


def initialize():
   # Define the adjacency matrix as a dictionary of dictionaries, where the keys are the city names and the values are dictionaries representing the connections to other cities
   adjacency_matrix = {
       'A': {'M': 1, 'O': 1, 'E': 1},
       'N': {'Q': 1, 'P': 1},
       'B': {'M': 1, 'O': 1},
       'M': {'N': 1, 'O': 1},
       'Z': {'E': 1},
       'O': {'M': 1, 'E': 1, 'Q': 1},
       'E': {'A': 1, 'B': 1, 'O': 1, 'P': 1},
       'Q': {'M': 1},
       'G': {'N': 1},
       'L': {'N': 1, 'P': 1},
       'P': {'O': 1, 'L': 1}
   }
   start_city = 'B'
   target_cities = ['N', 'E']
   num_visits = 2


   visited_costs = {}
   visited_costs[start_city] = 0


   queue = [(0, 0, [], start_city)]
  
   return adjacency_matrix, start_city, target_cities, num_visits, visited_costs, queue
  
def a_star():
  
   adjacency_matrix, start_city, target_cities, num_visits, visited_costs, queue = initialize()


   while queue:
       _, g, actions, current_city = heapq.heappop(queue)


       # Check if we have visited each target city the required number of times
       if all(actions.count(city) == num_visits for city in target_cities):
           return actions + [current_city]


       # Generate all possible actions from the current city, which includes moving to any city connected by a one-way road
       for neighbor_city, cost in adjacency_matrix[current_city].items():
           # Check if the new state would be valid, ie the city has not been visited more than the required number of times
           if actions.count(neighbor_city) < num_visits:
               # Generate the new state
               new_cost = g + cost
               if neighbor_city not in visited_costs or new_cost < visited_costs[neighbor_city]:
                   visited_costs[neighbor_city] = new_cost
                   heapq.heappush(queue, (new_cost, new_cost, actions + [current_city], neighbor_city))
   return None


print(a_star())
