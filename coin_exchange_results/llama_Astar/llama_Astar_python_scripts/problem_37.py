
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the coins that need to be chosen
   goal_sum = 303
   # Define the tax values for each coin
   tax_values = {15: 2, 18: 17, 22: 16, 29: 7, 28: 5, 23: 1, 20: 17, 14: 3, 13: 2, 4: 2, 5: 3, 27: 10, 16: 6, 3: 2, 6: 3, 19: 8, 2: 1, 25: 6, 24: 19, 26: 18, 21: 10, 11: 1, 30: 4}
   # Define the list of coins
   coins = [22, 15, 4, 23, 19, 3, 5, 28, 22, 27, 13, 18, 14, 11, 22, 20, 27, 24, 21, 13, 25, 11, 6, 2, 30, 29, 4, 16, 3, 13, 3, 28, 28, 20, 15, 27, 4, 18, 20, 5, 16, 21, 25, 24, 23, 15, 22, 26]
   # Define the dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in a list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the total sum of the chosen coins equals the goal sum
       if sum(state[0]) == goal_sum:
           return actions


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the total sum of the chosen coins does not exceed the goal sum
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
   # This heuristic relaxes the constraint that the coins must be chosen in increasing or decreasing order, and the tax values must be paid
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax value of the moved coin) + h(n)
   remaining_coins = goal_sum - sum(state[0])
   return remaining_coins


print(a_star())
