
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the coins to be chosen, and the total tax paid
   goal_state = (None, 228)
   # Define the set of all coins and their tax values
   coins = [21, 20, 21, 11, 23, 16, 16, 16, 3, 20, 2, 19, 16, 21, 18, 7, 20, 3, 16, 18, 7, 22, 3, 22, 7, 21, 12, 22, 5, 6, 17, 16, 8, 8, 14, 4, 18, 9, 4, 20, 2]
   taxes = {6: 1, 7: 3, 9: 1, 18: 1, 2: 1, 11: 7, 5: 3, 12: 2, 3: 3, 22: 6, 14: 3, 20: 15, 4: 3, 17: 4, 16: 8, 23: 18, 21: 16, 19: 2, 8: 6}
   # Define the additional constraints on the chosen coins
   constraints = [(6, 1), (7, 3), (9, 1), (18, 1), (2, 1), (11, 7), (5, 3), (12, 2), (3, 3), (22, 6), (14, 3), (20, 15), (4, 3), (17, 4), (16, 8), (23, 18), (21, 16), (19, 2), (8, 6)]
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in each state in a list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]
  
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)
       # Check if the current state is the goal state
       if state[1] == goal_state[1]:
           return actions
       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the total tax paid does not exceed the goal tax
           if coin not in state[0] and g + taxes[coin] <= goal_state[1]:
               # Generate the new state
               new_state = (state[0] | {coin}, g + taxes[coin])
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state, constraints), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal, constraints):
   # An admissible and consistent heuristic for this problem is the sum of the differences between the goal tax and the current total tax, for each constraint
   # This heuristic relaxes the constraint that the coin chosen must be smaller than the previous one, or larger than or equal to the previous coin chosen
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched coin must be chosen at least once
   # It's consistent because moving a coin from one state to another reduces the heuristic cost of the successor node by a max of 1 (if the moved coin's tax matches the constraint but not in the old state), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for constraint in constraints:
       if constraint[0] not in state[0]:
           h += goal[1] - state[1] - constraint[1]
   return h


print(a_star())
