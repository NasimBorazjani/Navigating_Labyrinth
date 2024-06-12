
import heapq


def a_star():
   # Define the initial state of the map, as a 2d tuple
   initial_state = (('E', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '1'),
                   ('0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0'),
                   ('1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0'),
                   ('0', '1', '1', '0', '1', '0', '0', '1', '1', '0', '0', '0'),
                   ('0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'),
                   ('1', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0'),
                   ('0', '1', '0', '0', '1', '1', '0', '1', '1', '1', '0', '1'),
                   ('1', '1', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0'),
                   ('0', '1', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0'),
                   ('0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0'),
                   ('0', '0', '0', '1', '0', '1', '0', '0', '1', '0', '0', '0'),
                   ('0', '1', '0', '1', '0', '0', '0', '1', '1', '1', '0', '0'))
  
   # Encoding other variables given in the problem statement
   num_cities = 12
   start_city = 'E'
   dest_cities = ['R', 'D']
   dest_count = 2


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the path taken to reach each state in a list; no path performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when we have visited the destination cities exactly twice
       if all(state[i][i] == str(dest_count) for i in range(num_cities) if state[i][i] != '0' and state[i][i] != '1'):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for city_ind in range(num_cities):
           if state[city_ind][city_ind] != '0' and state[city_ind][city_ind] != '1':
               # Check if the new state would be valid, ie the city must not be visited more than twice
               if int(state[city_ind][city_ind]) < dest_count:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[city_ind][city_ind] = str(int(state[city_ind][city_ind]) + 1)
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of moves made, as the task is to minimize the number of moves required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [state[city_ind][city_ind]], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the distances from the current state to the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as each move made is either to or from a destination city
   # It is consistent because moving a city closer to its goal state reduces the heuristic cost of the successor node by a max of 1 (if the moved city is not a destination city), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state)):
       if state[i][i] != '0' and state[i][i] != '1':
           h += abs(int(state[i][i]) - dest_count)
   return h


print(a_star())
