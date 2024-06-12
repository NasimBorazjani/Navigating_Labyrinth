
import heapq


def a_star():
   # Define the initial state of the map, as a 2d tuple
   initial_state = (('T', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'),
                   ('0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0'),
                   ('0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0'),
                   ('0', '1', '0', '0', '1', '0', '0', '0', '0', '1', '1'),
                   ('0', '0', '1', '1', '0', '0', '0', '1', '0', '0', '0'),
                   ('0', '0', '0', '1', '1', '0', '0', '0', '0', '1', '1'),
                   ('0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0'),
                   ('0', '0', '0', '0', '0', '1', '0', '0', '1', '0', '1'),
                   ('1', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0'),
                   ('0', '0', '1', '0', '0', '1', '1', '0', '0', '0', '0'),
                   ('1', '0', '0', '0', '1', '1', '0', '0', '0', '1', '0'))
   num_cities = 11
   start_city = 'T'
   goal_cities = ['N', 'W']
   goal_count = 2


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when we have visited the goal cities exactly twice
       if all(state[i][j] in goal_cities and state[i][j] not in actions for i in range(num_cities) for j in range(num_cities) if state[i][j] in goal_cities):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the other cities
       for i in range(num_cities):
           for j in range(num_cities):
               if state[i][j] != '0':
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   city_to_move = new_state[i][j]
                   new_state[i][j] = '0'
                   new_state[j][i] = city_to_move
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of moves made, as the task is to minimize the number of moves required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, goal_cities, goal_count)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [city_to_move], new_state))
   return None


def heuristic(state, goal_cities, goal_count):
   # An admissible and consistent heuristic for this problem is the sum of the minimum number of moves to visit each goal city exactly twice
   # This heuristic relaxes the constraint that we can only visit each city once
   # It is admissible because it never overestimates the cost to reach the goal, as each city must be visited at least once
   # It's consistent because moving a city from one state to another results in a decrease in the heuristic cost of the successor node by a max of 1 (if the moved city is a goal city), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for city in goal_cities:
       # Calculate the minimum number of moves to visit the city exactly twice
       h += min(state[i][j] == city and state[j][i] == '0' for i in range(len(state)) for j in range(len(state[i])) if state[i][j] == city)
   return h


print(a_star())
