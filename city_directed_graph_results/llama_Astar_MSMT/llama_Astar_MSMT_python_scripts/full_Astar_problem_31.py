
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adjacency_matrix = [
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
       [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
       [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
       [0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
       [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
       [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
       [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
   ]
   start = 'J'
   destinations = ['U', 'E']
   city_names = ['S', 'A', 'J', 'U', 'E', 'B', 'N', 'P', 'L', 'X', 'F']
   num_cities = len(city_names)


   visited_costs = {}
   visited_costs[(start, 0, 0)] = 0


   queue = [(0, 0, [], (start, 0, 0))]
  
   return adjacency_matrix, start, destinations, city_names, num_cities, visited_costs, queue
  
def a_star():
  
   adjacency_matrix, start, destinations, city_names, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If we have visited all the destinations twice, return the path
       if all(state[city_names.index(city) + 1] == 2 for city in destinations):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for new_city_index in range(num_cities):
           if adjacency_matrix[city_names.index(state[0])][new_city_index] == 1:
               new_city = city_names[new_city_index]
               # If the new city is a destination, we must have visited it once already
               if new_city in destinations and state[city_names.index(new_city) + 1] == 0:
                   continue
               # Generate the new state
               new_state = list(state)
               new_state[0] = new_city
               new_state[city_names.index(new_city) + 1] += 1
               new_state = tuple(new_state)
               # The cost of the new state is the travel time to get to the new city, plus the current cost
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the sum of the travel times from the new city to the remaining unvisited destinations
                   h = heuristic(new_state, destinations, city_names)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_city], new_state))
   return None


def heuristic(state, destinations, city_names):
   # The heuristic is the sum of the travel times from the new city to the remaining unvisited destinations
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent because it never overestimates the cost to reach the goal state
   h = 0
   for destination in destinations:
       if state[city_names.index(destination) + 1] == 0:
           h += 1
   return h


print(a_star())
