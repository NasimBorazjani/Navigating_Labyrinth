
import heapq


def a_star():
   # Define the initial state of the map, as a 2d tuple
   initial_state = (('L', 'A', 'J', 'U', 'E', 'P', 'Q', 'Y', 'H', 'R', 'K', 'M', 'F'),
                   ('0', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0'),
                   ('1', '0', '1', '0', '0', '0', '0', '0', '1', '0', '1', '0', '1'),
                   ('0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'),
                   ('0', '0', '1', '0', '0', '0', '0', '0', '1', '1', '1', '0', '1'),
                   ('0', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '1', '0'),
                   ('1', '0', '1', '1', '0', '1', '0', '0', '1', '1', '0', '0', '1'),
                   ('1', '1', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0'),
                   ('0', '1', '1', '1', '0', '1', '0', '1', '0', '1', '0', '0', '1'),
                   ('0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0'),
                   ('0', '1', '0', '0', '1', '1', '0', '0', '1', '0', '0', '0', '0'),
                   ('0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0'),
                   ('0', '1', '0', '0', '1', '1', '0', '1', '0', '0', '0', '1', '0'))
  
   # Encoding other variables given in the problem statement
   num_cities = 13
   start_city = 'L'
   dest_cities = ['J', 'K']
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
       if all(state[0].count(city) == dest_count for city in dest_cities):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the other cities
       for city_ind in range(num_cities):
           city = state[0][city_ind]
           # Check if the new state would be valid, ie we have not visited the city before and it is not the start city
           if city != start_city and state[0].count(city) < dest_count:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[0][city_ind] = start_city
               new_state[1][city_ind] = '0'
               new_state[city_ind + 1][0] = city
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, dest_cities)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [city], new_state))
   return None


def heuristic(state, dest_cities):
   # An admissible and consistent heuristic for this problem is the sum of the distances from the current city to the destination cities
   # This heuristic relaxes the constraint that we can only visit each city once on our path
   # It is admissible because it never overestimates the cost to reach the goal, as each move made is a valid move
   # It's consistent because moving to a city is always a valid move, and the heuristic cost of the successor node is higher or equal to the cost of reaching the successor node
   h = 0
   for city in dest_cities:
       # The distance is the number of moves made to reach the city, as the cost of moving to a city is 1
       h += state[0].count(city)
   return h


print(a_star())
