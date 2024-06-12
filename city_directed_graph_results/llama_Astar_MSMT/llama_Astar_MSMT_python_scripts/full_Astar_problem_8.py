
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [
       [0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
       [1, 0, 1, 0, 0, 1, 0, 0, 1, 1],
       [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 1, 0, 0, 1, 1],
       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 0, 0, 1, 0, 1, 0, 0, 0, 0]
   ]
   # Define the start city and the cities we need to visit exactly twice
   start_city = 'U'
   visit_twice = ['A', 'X']
   # Define the list of cities
   cities = ['Y', 'O', 'Q', 'X', 'K', 'R', 'A', 'U', 'M', 'L']
   # Define the index of the start city
   start_index = cities.index(start_city)
   # Define the indices of the cities we need to visit exactly twice
   visit_twice_indices = [cities.index(city) for city in visit_twice]
   # Define the number of cities
   num_cities = len(cities)


   visited_costs = {}
   visited_costs[(start_index, visit_twice_indices)] = 0


   queue = []
   # No actions taken in the initial state
   heapq.heappush(queue, (0, 0, [], (start_index, visit_twice_indices)))
  
   return adj_matrix, start_index, visit_twice_indices, cities, num_cities, visited_costs, queue
  
def a_star():
  
   adj_matrix, start_index, visit_twice_indices, cities, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If we have visited the cities we need to visit exactly twice twice, return the actions taken
       if all(state[1][i] == 2 for i in visit_twice_indices):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for i in range(num_cities):
           if adj_matrix[state[0]][i] == 1:
               # Check if the new state is valid, ie if we have visited the city before or if we have visited the city we need to visit exactly twice
               if i not in state[0] and i not in state[1]:
                   # Generate the new state
                   new_state = (state[0] + [i], state[1] + [i if i in visit_twice_indices else 0])
                   # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to visit the cities
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, visit_twice_indices)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [cities[i]], new_state))
   return None




def heuristic(state, visit_twice_indices):
   # The heuristic function can be a simulation of visiting the cities greedily, visiting the cities we need to visit exactly twice first
   # This heuristic is admissible because it is greedy, always opting for the action that visits the cities we need to visit exactly twice first, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if we visit a city we do not need to visit exactly twice, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of actions that can be saved by visiting the cities we need to visit exactly twice first is at most 1
   h = 0
   # Sort the cities by whether they are in the visit_twice_indices
   cities = sorted(range(len(state[0])), key=lambda i: i in visit_twice_indices)
   # Iterate through the cities
   for i in cities:
       # If we have not visited the city, increment the estimated cost to the goal by 1 actions
       if state[1][i] < 2:
           h += 1
   return h


print(a_star())
