
import heapq


def a_star():
   # Define the initial state of the map, as a 2d tuple
   initial_state = (('K', 'N', 'W', 'X', 'P', 'J', 'E', 'L', 'M', 'I'),
                   ('N', '0', '0', '1', '0', '0', '1', '0', '1', '0'),
                   ('W', '1', '0', '0', '1', '1', '0', '0', '0', '0'),
                   ('X', '0', '1', '0', '1', '0', '1', '0', '0', '0'),
                   ('P', '1', '1', '0', '0', '1', '0', '0', '0', '0'),
                   ('J', '0', '0', '1', '0', '0', '1', '0', '0', '0'),
                   ('E', '1', '1', '0', '0', '0', '0', '0', '0', '0'),
                   ('L', '1', '0', '0', '0', '0', '0', '0', '0', '1'),
                   ('M', '1', '1', '0', '0', '0', '1', '0', '0', '0'),
                   ('I', '0', '0', '1', '0', '1', '0', '1', '1', '0'),
                   ('K', '0', '0', '0', '0', '0', '1', '0', '0', '1'),
                   ('Q', '1', '1', '0', '0', '0', '0', '1', '0', '1'))
  
   # Encoding other variables given in the problem statement
   num_cities = 11
   start_city = 'K'
   dest_cities = ['P', 'N']
   dest_count = 2


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when we have visited the destination cities exactly twice
       if all(state[0].count(city) == dest_count for city in dest_cities):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the other cities
       for city_ind in range(1, num_cities):
           city = state[0][city_ind]
           # Check if the new state would be valid, ie we have not visited the city before and it is not the start city
           if state[0].count(city) == 1 and city != start_city:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[0][0], new_state[0][city_ind] = new_state[0][city_ind], new_state[0][0]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to visit the destination cities
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, dest_cities, dest_count)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [city], new_state))
   return None


def heuristic(state, dest_cities, dest_count):
   # An admissible and consistent heuristic for this problem is the sum of the minimum number of moves to visit each destination city exactly twice, minus the number of moves already made
   # This heuristic relaxes the constraint that we can only visit each city once
   # It is admissible because it never overestimates the cost to reach the goal, as each city must be visited at least once
   # It's consistent because moving to a city reduces the heuristic cost of the successor node by a max of 1 (if the city is a destination city), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for city in dest_cities:
       h += min(state[0].count(city) - dest_count, state[0].count(city))
   return h


print(a_star())
