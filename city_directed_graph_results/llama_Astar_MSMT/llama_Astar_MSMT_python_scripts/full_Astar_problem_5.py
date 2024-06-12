
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [
       [0, 0, 1, 1, 0, 0, 1, 1, 0, 1],
       [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
       [0, 1, 0, 1, 0, 1, 1, 0, 0, 1],
       [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
       [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
       [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
   ]
   # Define the start city and the destination cities
   start_city = 'H'
   dest_cities = ['Z', 'K']
   num_cities = len(adj_matrix)


   visited_costs = {}
   visited_costs[(start_city, 0, 0)] = 0


   queue = [(0, 0, [], (start_city, 0, 0))]
  
   return adj_matrix, start_city, dest_cities, num_cities, visited_costs, queue
  
def a_star():
  
   adj_matrix, start_city, dest_cities, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If we have visited all destination cities twice, return the path
       if state[1] == 2 and state[2] == 2:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for dest_city in dest_cities:
           dest_index = ord(dest_city) - ord('A')
           for i in range(num_cities):
               if adj_matrix[i][dest_index] == 1:
                   # Check if the new state is valid, ie if we have visited the city before
                   if i != ord(start_city) - ord('A'):
                       new_state = (chr(i + ord('A')), state[1] + (1 if state[0] == dest_city else 0), state[2] + (1 if state[0] == 'K' else 0))
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, dest_cities), new_cost, actions + [new_state[0]], new_state))
   return None




def heuristic(state, dest_cities):
   # The heuristic function can be a simple count of the number of cities left to visit
   # This heuristic is admissible because it is a lower bound on the cost to reach the goal state
   # The heuristic is consistent because the cost of reaching the goal state is always 0, as we have visited all destination cities twice
   return sum(1 for city in dest_cities if state[0] != city)


print(a_star())
