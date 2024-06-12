
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [
       [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
       [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
       [0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [1, 1, 1, 1, 0, 1, 0, 0, 1, 1],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
   ]
   # Define the start city and the destination cities
   start = 'B'
   destinations = ['V', 'L']
   num_cities = len(adj_matrix)


   visited_costs = {}
   visited_costs[(start, 0, 0)] = 0


   queue = [(0, 0, [], (start, 0, 0))]
  
   return adj_matrix, start, destinations, num_cities, visited_costs, queue
  
def a_star():
  
   adj_matrix, start, destinations, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current city is a destination city and we have visited it twice, return the path
       if state[0] in destinations and state[1] == 2 and state[2] == 2:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for i in range(num_cities):
           if adj_matrix[state[0]][i] == 1:
               # Generate the new state
               new_state = (chr(i + 65), state[1] + (1 if state[0] == 'V' else 0), state[2] + (1 if state[0] == 'L' else 0))
               # The cost of the new state is the travel time to get to the new city
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The new city must be added to the path
                   heapq.heappush(queue, (new_cost + heuristic(new_state, destinations), new_cost, actions + [new_state[0]], new_state))
   return None




def heuristic(state, destinations):
   # The heuristic function can be a simulation of moving to the destination cities greedily, using the next nearest city as the next city to visit
   # This heuristic is admissible because it is greedy, always opting for the action that moves us closer to the destination cities, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if we move to a city that is not a destination city, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum distance to the nearest destination city that we have not visited twice is exactly the city used to fill the bucket in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   # Calculate the remaining number of times we need to visit each destination city
   remaining_destinations = [2 - state[1], 2 - state[2]]
   # Iterate through the remaining number of times we need to visit each destination city
   for i in range(len(remaining_destinations)):
       if remaining_destinations[i] > 0:
           # Find the nearest city that has not been visited twice yet
           for j in range(num_cities):
               if adj_matrix[state[0]][j] == 1:
                   h += 1
                   break
   return h


print(a_star())
