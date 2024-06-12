
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [
       [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
       [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
       [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0],
       [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0]
   ]
   # Define the start city and the destination cities
   start_city = 'Y'
   dest_cities = ['I', 'Q']
   num_cities = len(adj_matrix)


   visited_costs = {}
   visited_costs[(start_city, 0, 0)] = 0


   queue = []
   # No actions taken in the initial state
   heapq.heappush(queue, (0, 0, [], (start_city, 0, 0)))
  
   return adj_matrix, start_city, dest_cities, num_cities, visited_costs, queue
  
def a_star():
  
   adj_matrix, start_city, dest_cities, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current city is a destination city and we have visited it twice, return the actions taken
       if state[0] in dest_cities and state[1] == 2 and state[2] == 2:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for i in range(num_cities):
           if adj_matrix[state[0]][i] == 1:
               # Check if the new state is valid, ie if we have visited the city before
               if state[0] != dest_cities[0] or state[1] < 2:
                   new_state = (chr(i + 65), state[1] + (1 if state[0] == dest_cities[0] else 0), state[2] + (1 if state[0] == dest_cities[1] else 0))
                   # The cost of the new state is the travel time to get to the new city
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic is the straight-line distance between the current city and the destination cities, as the task is to minimize the total travel time
                       h = heuristic(new_state, dest_cities)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state[0]], new_state))
   return None




def heuristic(state, dest_cities):
   # The heuristic is the straight-line distance between the current city and the destination cities, as the task is to minimize the total travel time
   # This heuristic is admissible because it is an underestimate of the cost to reach the goal state
   # The heuristic is consistent because the estimated cost of the next node is higher if we move to a city that is further from the destination cities, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum distance that can be added to the heuristic is by moving to a city that is closer to the destination cities
   h = 0
   for dest_city in dest_cities:
       h += abs(ord(state[0]) - ord(dest_city))
   return h


print(a_star())
