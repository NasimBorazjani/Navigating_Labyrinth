
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the chosen coins equaling 384
   goal_sum = 384
   # Define the tax values for each coin
   tax_values = {13: 1, 4: 1, 61: 2, 30: 19, 12: 4, 20: 16, 29: 10, 2: 2, 35: 17, 31: 17, 19: 15, 25: 11, 21: 8, 27: 16, 17: 17, 11: 7, 58: 12, 26: 4, 15: 14, 28: 10, 8: 5, 16: 5, 9: 8, 33: 13}
   # Define the list of coins
   coins = [8, 13, 16, 4, 35, 2, 19, 2, 21, 26, 28, 12, 58, 28, 12, 35, 33, 4, 19, 27, 61, 30, 17, 20, 27, 25, 30, 31, 9, 15, 4, 13, 11, 29]
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
           if coin not in state[0] and state[1] + tax_values[coin] <= goal_sum:
               # Relax the constraints on the coin values and taxes to generate the new state
               new_state = (state[0] | {coin}, state[1] + tax_values[coin])
               new_cost = g + tax_values[coin]
              
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum, tax_values), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_sum, tax_values):
   # An admissible and consistent heuristic for this problem is the sum of the remaining coins to be chosen, minus the remaining tax to be paid
   # This heuristic relaxes the constraints that the tax for coins of the same value is the same, and the coin chosen must be smaller than the previous one if it is smaller, and larger or equal to the previous one if it is larger or equal
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining set to the chosen set reduces the heuristic cost of the successor node by a max of the tax value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax value of the moved coin) + h(n)
   remaining_coins = goal_sum - sum(state[0])
   remaining_tax = goal_sum - state[1]
   return remaining_coins - remaining_tax


print(a_star())
