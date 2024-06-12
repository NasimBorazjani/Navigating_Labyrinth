
import heapq


def initialize():
   # Define the adjacency matrix representing the directed graph
   adjacency_matrix = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
                      [0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
                      [0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                      [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
                      [0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0],
                      [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0]]
   # Define the cities and their corresponding indices in the adjacency matrix
   cities = {0: 'H', 1: 'F', 2: 'C', 3: 'E', 4: 'T', 5: 'V', 6: 'R', 7: 'I', 8: 'M', 9: 'Z', 10: 'L', 11: 'D'}
   start = 'E'
   destinations = ['D', 'T']
   num_cities = 12


   # Initialize the visited_costs dictionary and the priority queue
   visited_costs = {}
   visited_costs[(start, 0, 0)] = 0
   queue = []
   heapq.heappush(queue, (0, 0, [], (start, 0, 0)))
  
   return adjacency_matrix, cities, start, destinations, num_cities, visited_costs, queue
  
def a_star():
  
   adjacency_matrix, cities, start, destinations, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, path, state = heapq.heappop(queue)


       # Unpack the information encoded in each state
       current_city, d_visits, t_visits = state


       # If we have visited both destinations exactly twice, return the path
       if d_visits == 2 and t_visits == 2:
           return path


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       city_index = list(cities.values()).index(current_city)
       for i in range(num_cities):
           if adjacency_matrix[city_index][i] == 1:
               next_city = cities[i]
               # Update the destination city visit counts
               d_visits_new, t_visits_new = d_visits, t_visits
               if next_city == 'D':
                   d_visits_new += 1
               elif next_city == 'T':
                   t_visits_new += 1
               # Generate the new state
               new_state = (next_city, d_visits_new, t_visits_new)
               # Cost of the new state is the travel time to get to the new city, which is the same for all directly connected cities
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The new city must be added to the path
                   heapq.heappush(queue, (new_cost + heuristic(new_state, destinations), new_cost, path + [next_city], new_state))
   return None




def heuristic(state, destinations):
   # The heuristic is the sum of the minimum number of travels required to reach the destinations from the current city
   # This heuristic is admissible because it is an upper bound on the cost to reach the goal state
   # The heuristic is consistent because the cost of reaching any city from the current city is always the same, regardless of the destinations
   current_city, d_visits, t_visits = state
   h = 0
   if 'D' not in destinations:
       d_visits = 2
   if 'T' not in destinations:
       t_visits = 2
   h = min(d_visits, t_visits)
   return h


print(a_star())
