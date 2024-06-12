
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the chosen coins equaling 423
   goal_sum = 423
   # Define the tax values for each coin
   tax_values = {40: 1, 41: 13, 8: 5, 28: 2, 21: 18, 15: 7, 5: 4, 14: 13, 37: 12, 22: 12, 29: 3, 30: 15, 35: 4, 26: 19, 39: 7, 31: 14, 11: 7, 20: 3, 6: 2, 12: 8, 27: 13, 19: 19, 34: 5, 18: 9, 38: 16, 24: 17}
   # Define the list of coins
   coins = [28, 11, 40, 15, 21, 6, 20, 6, 12, 22, 8, 18, 34, 24, 22, 30, 35, 41, 6, 39, 5, 15, 19, 8, 26, 38, 11, 29, 31, 14, 37, 28, 8, 11, 28, 27, 38]
   # Define the additional constraints on the coins
   constraints = {'prev_coin': None, 'even_odd': None}


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
           # Check if the new state would be valid, ie the coin is not already chosen and the tax for the coin is less than the tax for the previous coin chosen
           if coin not in state[0] and (constraints['prev_coin'] is None or tax_values[coin] <= tax_values[constraints['prev_coin']]):
               # Update the constraints
               constraints['prev_coin'] = coin
               if coin < constraints['prev_coin']:
                   constraints['even_odd'] = 'even'
               else:
                   constraints['even_odd'] = 'odd'
               # Generate the new state
               new_state = (state[0] | {coin}, state[1] + tax_values[coin])
               # The cost so far is the tax paid so far, as the task is to minimize the total tax paid
               new_cost = g + tax_values[coin]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum, tax_values, constraints), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_sum, tax_values, constraints):
   # An admissible and consistent heuristic for this problem is the sum of the remaining coins to be chosen, minus the tax for the next coin to be chosen
   # This heuristic relaxes the constraint that the tax for the next coin to be chosen must be less than the tax for the previous coin chosen
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the tax for the next coin to be chosen, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax for the next coin to be chosen) + h(n)
   remaining_coins = set(coins) - state[0]
   if not remaining_coins:
       return 0
   else:
       next_coin = min(remaining_coins, key=lambda coin: (tax_values[coin], coin))
       return sum(coin for coin in remaining_coins if coin != next_coin) - tax_values[next_coin]


print(a_star())
