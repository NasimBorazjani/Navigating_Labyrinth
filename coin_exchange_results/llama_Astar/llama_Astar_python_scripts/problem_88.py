
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the coins that need to be chosen
   goal_sum = 465
   # Define the tax values for each coin
   tax_values = {13: 9, 106: 19, 28: 20, 44: 14, 9: 6, 35: 6, 22: 19, 46: 17, 11: 7, 40: 12, 17: 15, 10: 4, 12: 6, 30: 20, 2: 2, 23: 11, 42: 10, 16: 1, 107: 11, 21: 12, 5: 3, 31: 13, 29: 20}
   # Define the list of coins
   coins = [21, 31, 30, 31, 10, 17, 13, 35, 12, 2, 16, 40, 23, 10, 29, 13, 23, 2, 9, 5, 107, 46, 23, 11, 42, 9, 46, 28, 44, 22, 106, 10]
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
           # Check if the new state would be valid, ie the coin is not already chosen and the tax for the coin is less than or equal to the tax for the previous chosen coin
           if coin not in state[0] and (prev_coin is None or tax_values[coin] <= tax_values[prev_coin]):
               # Generate the new state
               new_state = (state[0] | {coin}, state[1] + tax_values[coin])
               # The additional cost of this state is the tax for the chosen coin
               new_cost = g + tax_values[coin]
              
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
                   prev_coin = coin
   return None


def heuristic(state, goal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the values of the remaining coins to be chosen, minus the sum of the taxes for the remaining coins
   # This heuristic relaxes the constraint that the tax for a coin must be less than or equal to the tax for the previous chosen coin
   # It is admissible because it never overestimates the cost to reach the goal, as the cost of choosing a coin is always the tax for that coin
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the tax for that coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax for the chosen coin) + h(n)
   remaining_coins = goal_sum - sum(state[0])
   remaining_taxes = sum(tax_values[coin] for coin in state[0])
   return remaining_coins - remaining_taxes


print(a_star())
