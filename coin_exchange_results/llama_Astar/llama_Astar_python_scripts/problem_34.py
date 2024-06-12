
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the coins to be chosen
   goal_sum = 293
   # Define the tax values for each coin
   tax_values = {2: 2, 14: 13, 29: 2, 13: 3, 25: 20, 28: 18, 11: 7, 9: 1, 3: 2, 15: 3, 8: 2, 7: 1, 12: 6, 26: 9, 19: 11, 24: 1, 22: 9, 27: 17, 6: 4, 18: 14, 21: 12, 4: 3, 37: 6, 20: 16, 5: 5, 10: 6}
   # Define the list of coins
   coins = [22, 14, 13, 18, 2, 5, 14, 26, 28, 9, 20, 26, 11, 29, 2, 15, 13, 11, 28, 12, 14, 6, 3, 25, 12, 24, 4, 28, 27, 10, 20, 6, 8, 7, 37, 18, 3, 10, 27, 20, 21, 8, 11, 13, 5, 19, 4, 2]
   # Define the previous chosen coin
   prev_coin = None


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if sum(state[0]) == goal_sum:
           return actions


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the tax value of the coin is even if it is smaller than the previous coin chosen and odd if it is larger or equal
           if coin not in state[0] and (prev_coin is None or (coin < prev_coin and tax_values[coin] % 2 == 0) or (coin >= prev_coin and tax_values[coin] % 2 == 1)):
               # Generate the new state
               new_state = (state[0].copy(), state[1] + tax_values[coin])
               new_state[0].add(coin)
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g + tax_values[coin]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum, tax_values), new_cost, actions + [coin], new_state))
                   prev_coin = coin
   return None


def heuristic(state, goal_sum, tax_values):
   # An admissible and consistent heuristic for this problem is the sum of the remaining coins to be chosen, plus the tax value of the next coin to be chosen
   # This heuristic relaxes the constraint that the tax value of the next coin to be chosen must be even if it is smaller than the previous coin chosen and odd if it is larger or equal
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the tax value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax value of the moved coin) + h(n)
   remaining_coins = goal_sum - sum(state[0])
   next_coin = min(coin for coin in tax_values if coin not in state[0])
   return remaining_coins + tax_values[next_coin]


print(a_star())
