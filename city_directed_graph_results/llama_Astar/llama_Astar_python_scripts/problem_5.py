
import heapq


def a_star():
   # Define the initial state of the map, as a 2d tuple
   initial_state = (('H', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'),
                   ('0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '1'),
                   ('0', '0', '0', '1', '0', '1', '1', '0', '0', '1', '0'),
                   ('0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0'),
                   ('0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0'),
                   ('0', '0', '1', '1', '0', '0', '1', '0', '1', '0', '0'),
                   ('0', '1', '0', '1', '1', '0', '0', '0', '0', '0', '0'),
                   ('1', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0'),
                   ('0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0'),
                   ('0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0'),
                   ('0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0'))
  
   # Encoding other variables given in the problem statement
   num_cities = 10
   start_city = 'H'
   dest_cities = ['K', 'Z']
   num_visits = 2


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
       if all(state[i][0] in dest_cities and state[i].count('1') == 2 for i in range(1, num_cities + 1)):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the other cities
       for city_ind in range(1, num_cities + 1):
           # Check if the new state would be valid, ie the city must not be the start city or a destination city, and we must not have visited the city twice
           if state[city_ind][0] != start_city and state[city_ind].count('1') < num_visits:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[city_ind][0] = '1'
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to visit the destination cities
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, dest_cities, num_visits), new_cost, actions + [state[city_ind][0]], new_state))
   return None


def heuristic(state, dest_cities, num_visits):
   # An admissible and consistent heuristic for this problem is the sum of the minimum number of moves to visit each destination city the remaining number of times
   # This heuristic relaxes the constraint that we can only visit each city once on our path
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining visit to a destination city must be made at least once
   # It's consistent because moving to a city results in a decrease in the heuristic cost of the successor node by a max of 1 (if the moved city is a destination city), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for city_ind in range(1, len(state)):
       if state[city_ind][0] in dest_cities:
           h += min(num_visits - state[city_ind].count('1'), state[city_ind].count('0'))
   return h


print(a_star())
