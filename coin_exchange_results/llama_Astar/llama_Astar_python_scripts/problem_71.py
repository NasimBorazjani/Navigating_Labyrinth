
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the chosen coins equal to 400
   goal_sum = 400
   # Define the tax values for each coin
   tax_values = {29: 9, 40: 8, 30: 5, 17: 16, 3: 3, 5: 3, 2: 2, 22: 17, 11: 1, 14: 4, 8: 5, 18: 11, 26: 8, 39: 15, 7: 1, 31: 2, 24: 17, 189: 5, 12: 4, 25: 10, 35: 18, 10: 1, 4: 3, 34: 16}
   # Define the list of coins
   coins = [18, 11, 14, 3, 7, 18, 40, 3, 35, 30, 24, 29, 34, 11, 17, 14, 14, 10, 5, 40, 4, 31, 25, 14, 39, 12, 26, 24, 3, 8, 34, 2, 22, 189, 40]
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in the list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the total sum of the chosen coins is equal to 400
       if sum(state[0]) == goal_sum:
           return actions


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the total sum of the chosen coins does not exceed 400
           if coin not in state[0] and sum(state[0]) + coin <= goal_sum:
               # Generate the new state
               new_state = (state[0] | {coin}, state[1] + tax_values[coin])
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g + tax_values[coin]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the values of the remaining coins to be chosen, to reach the goal sum
   # This heuristic relaxes the constraint that the tax for coins of the same value is the same
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax of the moved coin) + h(n)
   remaining_coins = goal_sum - sum(state[0])
   return remaining_coins


print(a_star())
