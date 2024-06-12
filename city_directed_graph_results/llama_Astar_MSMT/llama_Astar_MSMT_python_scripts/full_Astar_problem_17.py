
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [
       [0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
       [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
       [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
       [0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 1, 1, 0]
   ]
   # Define the start city and the destination cities
   start_city = 'V'
   dest_cities = ['Y', 'I']
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
       if state[0] in dest_cities and state[1] == 2:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for i in range(num_cities):
           if adj_matrix[state[2][i]] == 1:
               # Check if the new state is valid, ie if we have visited the city before
               if state[2][i] != state[2][i - 1]:
                   # Generate the new state
                   new_state = (chr(i + 65), state[1] + 1, list(state[2]))
                   new_state[2][i] = 1
                   # The cost so far is the number of cities visited, as the task is to minimize the number of cities visited to reach the goal state
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, dest_cities)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state[0]], new_state))
   return None




def heuristic(state, dest_cities):
   # The heuristic function can be a simulation of visiting the destination cities greedily, visiting the nearest city first
   # This heuristic is admissible because it is greedy, always opting for the action that visits the destination cities the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if we visit a city that is not a destination city, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of cities that can be visited in the heuristic is by visiting the nearest destination city, which is exactly the city used to visit in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Sort the cities by their distance to the current city
   cities = sorted(range(len(state[2])), key=lambda i: abs(ord(state[0]) - 65 - i))
   # Iterate through the cities
   for i in cities:
       if state[2][i] == 0:
           # Visit the city and increment the estimated cost to the goal by 1 actions
           state[2][i] = 1
           h += 1
   return h


print(a_star())
