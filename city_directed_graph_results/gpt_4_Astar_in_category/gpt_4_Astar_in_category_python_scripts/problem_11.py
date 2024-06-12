
import heapq


def a_star():
   # Define the adjacency matrix of the cities
   adjacency_matrix = [[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                       [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
                       [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                       [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
                       [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                       [0, 0, 1, 1, 1, 0, 0, 1, 1, 0]]
   # Define the names of the cities
   cities = ['Q', 'T', 'A', 'X', 'M', 'Y', 'Z', 'B', 'S', 'E']
   # Define the initial state and the goal state
   initial_state = (0, False, False, False, False, False, False, False, False, False, False, False)
   goal_state = (0, True, True, False, False, False, False, False, False, False, True, True)
   num_cities = 10


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [cities[0]], initial_state))


   while queue:
       _, g, path, state = heappop(queue)


       # If the current state is the goal state, return the path
       if state == goal_state:
           return path


       # Generate all possible actions from the current state, which includes moving to any of the cities directly connected to the current city
       for city_ind in range(num_cities):
           # Check if the new state would be valid, ie if there is a direct road from the current city to the new city
           if adjacency_matrix[state[0]][city_ind] == 1:
               # Generate the new state
               # The new state must maintain the information on the cities visited so far, and the number of times the destination cities have been visited
               # If the new city is a destination city, increment the count of the number of times it has been visited
               # If the new city is not a destination city, mark it as visited
               new_state = list(state[:])
               new_state[0] = city_ind
               if cities[city_ind] == 'T':
                   new_state[1] = True
                   new_state[2] = True if new_state[2] else False
               elif cities[city_ind] == 'E':
                   new_state[3] = True
                   new_state[4] = True if new_state[4] else False
               else:
                   new_state[city_ind + 5] = True
               new_state = tuple(new_state)
               # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to visit the destination cities twice
               new_cost = g + 1


               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The name of the new city must be added to the path
                   heappush(queue, (new_cost + heuristic(state[0], city_ind), new_cost, path + [cities[city_ind]], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the number of destination cities that have not been visited twice
   # The heuristic relaxes the constraints that we can only move to cities that are directly connected to the current city, and that we can only visit each non-destination city once; ie It presumes we can move directly to any given city
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one city to an adjacent city is 1, which is equal to the decrease in the heuristic cost if the successor node is a destination city that has not been visited twice
   return 2 - state[1] - state[2] + 2 - state[3] - state[4]


print(a_star())
