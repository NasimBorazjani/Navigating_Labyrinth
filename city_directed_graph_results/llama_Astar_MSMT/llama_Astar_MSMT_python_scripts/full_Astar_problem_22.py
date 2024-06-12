
import heapq


def initialize():
   # Define the adjacency matrix of the directed graph
   adj_matrix = [
       [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
       [0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
       [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],
       [1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0],
       [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
       [0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
   ]
   # Define the start city and the goal cities
   start = 'X'
   goals = ['E', 'T']
   num_cities = len(adj_matrix)


   visited_costs = {}
   visited_costs[(start, 0, 0)] = 0


   queue = [(0, 0, [], (start, 0, 0))]
  
   return adj_matrix, start, goals, num_cities, visited_costs, queue
  
def a_star():
  
   adj_matrix, start, goals, num_cities, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If we have visited each goal city exactly twice, return the path
       if state[1] == 2 and state[2] == 2:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for i in range(num_cities):
           if adj_matrix[state[0]][i] == 1:
               # Generate the new state
               new_state = (chr(i + 65), state[1] + (1 if chr(i + 65) == 'E' else 0), state[2] + (1 if chr(i + 65) == 'T' else 0))
               # The cost of the new state is the travel time to get to the new city
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The new city must be added to the path
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goals), new_cost, actions + [new_state[0]], new_state))
   return None




def heuristic(state, goals):
   # The heuristic function can be a simple count of the number of cities left to visit
   # This heuristic is admissible because it is an underestimate of the cost to reach the goal state
   # The heuristic is consistent because the cost of reaching the goal state is always 0, as we have visited all the goal cities exactly twice
   h = 0
   for goal in goals:
       if state[0] != goal and state[1] < 2:
           h += 1
   return h


print(a_star())
