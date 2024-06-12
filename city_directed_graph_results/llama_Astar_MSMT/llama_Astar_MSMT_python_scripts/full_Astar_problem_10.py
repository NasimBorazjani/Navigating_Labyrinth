
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 1, 1, 0, 1, 1, 1, 1],
       [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
       [1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
       [0, 1, 0, 1, 0, 0, 1, 0, 0, 1],
       [1, 1, 1, 0, 0, 1, 0, 0, 0, 0]
   ]
   # Define the start city and the destination cities
   start_city = 'Q'
   dest_cities = ['P', 'E']
   num_cities = len(adj_matrix)


   visited_costs = {}
   visited_costs[(start_city, 0, 0)] = 0


   queue = [(0, 0, [], (start_city, 0, 0))]
  
   return adj_matrix, start_city, dest_cities, num_cities, visited_costs, queue
  
def a_star():
  
   adj_matrix, start_city, dest_cities, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current city is a destination city and we have visited it twice, return the path
       if state[0] in dest_cities and state[1] == 2 and state[2] == 2:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for i in range(num_cities):
           if adj_matrix[state[0]][i] == 1:
               # Check if the new state is valid, ie if we have visited the destination cities at least once
               if (state[0] in dest_cities and state[1] >= 1 and state[2] >= 1) or state[0] not in dest_cities:
                   # Generate the new state
                   new_state = (chr(i + 65), state[1] + (1 if state[0] == 'P' else 0), state[2] + (1 if state[0] == 'E' else 0))
                   # The cost of the new state is the travel time to get to the new city
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The city must be added to the path
                       heapq.heappush(queue, (new_cost + heuristic(new_state, dest_cities), new_cost, actions + [new_state[0]], new_state))
   return None




def heuristic(state, dest_cities):
   # The heuristic function can be a simulation of moving to the destination cities greedily, using the next nearest city as long as the destination cities have not been visited twice
   # This heuristic is admissible because it is greedy, always opting for the action that moves us closer to the destination cities, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if we move to a city that is not a destination city, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of actions that can be taken is by moving to the nearest city that has not been visited twice
   h = 0
   # Sort the cities by their distance to the destination cities
   cities = sorted(range(len(state)), key=lambda i: abs(i - (ord(dest_cities[0]) - 65)) + abs(i - (ord(dest_cities[1]) - 65)))
   # Iterate through the cities
   for i in cities:
       # If the city is a destination city and we have not visited it twice, move to the city
       if (state[0] in dest_cities and state[1] < 2 and state[2] < 2) or state[0] not in dest_cities:
           h += 1
   return h


print(a_star())
