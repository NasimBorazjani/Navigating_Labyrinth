
import heapq


def a_star():
   # Define the initial state of the map, as a 2d tuple
   initial_state = (('L', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '1', '1'),
                   ('0', 'R', '0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '0', '0', '1'),
                   ('0', '1', 'P', '0', '0', '1', '0', '1', '1', '1', '1', '0', '0', '0', '0'),
                   ('0', '0', '0', 'U', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0'),
                   ('1', '0', '0', '0', 'H', '0', '1', '0', '1', '1', '0', '1', '1', '1', '0'),
                   ('1', '1', '0', '1', '1', 'T', '0', '0', '0', '0', '1', '0', '0', '0', '0'),
                   ('0', '0', '0', '0', '0', 'E', '0', '0', '0', '0', '1', '0', '0', '0', '1'),
                   ('1', '0', '1', '0', '1', '0', 'W', '0', '0', '0', '0', '0', '1', '0', '1'),
                   ('0', '0', '1', '1', '1', '0', '0', 'F', '0', '1', '0', '0', '0', '0', '0'),
                   ('0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0'),
                   ('0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0'),
                   ('1', '0', '0', '0', '0', '1', '0', '1', '1', '0', '0', '0', '0', '0', '1'),
                   ('0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0'),
                   ('0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0'))
  
   # Encoding other variables given in the problem statement
   num_cities = 15
   start_city = 'L'
   destinations = {'W': 2, 'P': 2}


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
       if all(state.count(city) == 2 for city in destinations):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the directly connected cities
       for city_ind in range(num_cities):
           city = state[city_ind]
           if city != '0' and state.count(city) < 2:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               # Move to the new city
               new_state[city_ind] = '0'
               new_state[0] = city
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal state
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, destinations), new_cost, actions + [city], new_state))
   return None


def heuristic(state, destinations):
   # An admissible and consistent heuristic for this problem is the sum of the minimum number of moves to visit each destination city exactly twice
   # This heuristic relaxes the constraint that we can only visit each city once on our path
   # It is admissible because it never overestimates the cost to reach the goal, as each move to a city is costlier
   # It's consistent because moving to a city is costlier than moving to another city, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for city, count in destinations.items():
       h += min(state.count(city), count)
   return h


print(a_star())
