
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the chosen coins equaling 452
   goal_sum = 452
   # Define the tax values for each coin
   tax_values = {37: 2, 38: 4, 30: 18, 39: 18, 14: 1, 18: 1, 4: 1, 10: 8, 21: 10, 6: 5, 42: 13, 32: 10, 25: 2, 17: 15, 13: 2, 9: 4, 22: 17, 7: 5, 3: 2, 54: 7, 19: 15, 8: 2, 36: 17, 28: 6, 5: 5, 41: 9, 57: 12}
   # Define the list of coins
   coins = [39, 3, 38, 10, 3, 5, 6, 14, 32, 7, 30, 28, 17, 9, 8, 13, 17, 41, 25, 6, 19, 36, 5, 36, 8, 38, 6, 19, 25, 3, 22, 18, 3, 21, 57, 37, 42, 30, 54, 13, 36, 6, 13, 17, 10, 4, 36]
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
           # Check if the new state would be valid, ie the coin is not already chosen and the total tax paid does not exceed the goal tax
           if coin not in state[0] and g + tax_values[coin] <= goal_sum:
               # Generate the new state
               new_state = (state[0].copy(), g + tax_values[coin])
               new_state[0].add(coin)
               # The cost so far is the total tax paid so far
               new_cost = g
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum, tax_values, prev_coin), new_cost, actions + [coin], new_state))
                   prev_coin = coin
   return None


def heuristic(state, goal_sum, tax_values, prev_coin):
   # An admissible and consistent heuristic for this problem is the sum of the tax values of the remaining coins to be chosen, plus the tax value of the last chosen coin
   # This heuristic relaxes the constraint that the tax value of a coin must be even if it is smaller than the previous coin chosen and odd otherwise
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the tax value of the coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax value of the coin) + h(n)
   remaining_coins = set(coins) - state[0]
   h = sum(tax_values[coin] for coin in remaining_coins)
   if prev_coin is not None:
       h += tax_values[prev_coin]
   return h


print(a_star())
