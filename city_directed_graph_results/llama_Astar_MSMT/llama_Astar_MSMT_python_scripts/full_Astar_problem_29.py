
import heapq


def initialize():
   # Define the adjacency matrix of the graph
   adj_matrix = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
                 [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                 [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0],
                 [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
                 [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]]

   # Define the start city and the destination cities
   start_city = 'G'
   dest_cities = ['S', 'E']
   num_cities = 10


   visited_costs = {}
   visited_costs[(start_city, 0, 0)] = 0


   queue = [(0, 0, [], (start_city, 0, 0))]
  
   return adj_matrix, start_city, dest_cities, num_cities, visited_costs, queue
  
def a_star():
  
   adj_matrix, start_city, dest_cities, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If we have visited both destination cities exactly twice, return the path
       if state[1] == 2 and state[2] == 2:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for i in range(num_cities):
           if adj_matrix[state[0].index(ord(state[0])-ord('A')+1)][i] == 1:
               # Check if the new state is valid, ie we have not visited the city before, or we have visited both destination cities at least once
               if (chr(i+ord('A')) not in state[0] or (state[0].count(dest_cities[0]) >= 2 and state[0].count(dest_cities[1]) >= 2)):
                   # Generate the new state
                   new_state = (state[0] + chr(i+ord('A')), state[1] + (1 if chr(i+ord('A')) == dest_cities[0] else 0), state[2] + (1 if chr(i+ord('A')) == dest_cities[1] else 0))
                   # The cost of the new state is the travel time to get to the new city, plus the cost of the current state
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The city must be added to the path
                       heapq.heappush(queue, (new_cost + heuristic(new_state, dest_cities), new_cost, actions + [chr(i+ord('A'))], new_state))
   return None




def heuristic(state, dest_cities):
   # The heuristic function can be a simple count of the number of cities left to visit, including the destination cities
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent because the cost of reaching the goal state is always less than or equal to the sum of the costs to reach the goal cities and the heuristic estimate for the goal city, and the cost of reaching any other city is never greater than the cost of reaching the goal city
   h = 0
   for city in state[0]:
       if city not in dest_cities:
           h += 1
   return h


print(a_star())
