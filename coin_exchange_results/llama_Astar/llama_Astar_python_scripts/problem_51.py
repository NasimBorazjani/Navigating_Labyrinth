
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the set of all coins and the total tax paid, which is 0 as we have chosen all coins
   goal_state = (set(range(1, 33)), 0)
   # Define the set of coins and their tax values
   coins = [31, 83, 19, 4, 13, 27, 13, 18, 21, 24, 9, 3, 2, 30, 16, 14, 31, 29, 27, 23, 18, 8, 32, 3, 3, 25, 17, 8, 32, 5, 2, 28, 30, 26, 25, 12, 12]
   tax_values = {32: 1, 19: 12, 3: 1, 27: 14, 5: 3, 9: 5, 13: 11, 14: 10, 28: 6, 31: 15, 8: 8, 18: 18, 17: 7, 2: 2, 12: 9, 24: 16, 83: 6, 23: 9, 16: 15, 29: 4, 25: 5, 26: 18, 4: 1, 21: 10, 30: 10}
   # Define the total sum of the coins to be chosen
   total_sum = 335
   # Define the previous chosen coin
   prev_coin = None


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the total sum of the chosen coins does not exceed the target sum
           if coin not in state[0] and sum(state[0]) + coin <= total_sum:
               # Check the tax constraint
               if prev_coin is None or coin < prev_coin and tax_values[coin] % 2 == 0 or coin >= prev_coin and tax_values[coin] % 2 == 1:
                   # Generate the new state
                   new_state = (state[0].copy(), state[1] + tax_values[coin])
                   new_state[0].add(coin)
                   # The cost so far is the total tax paid so far, as we are trying to minimize the total tax paid
                   new_cost = g + tax_values[coin]
                  
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [coin], new_state))
                       prev_coin = coin
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the remaining coins to be chosen, as we are trying to minimize the total tax paid
   # This heuristic relaxes the constraint that the coins must be chosen in a specific order, as it only considers the remaining coins to be chosen
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining set to the chosen set reduces the heuristic cost of the successor node by a max of the tax value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax value of the moved coin) + h(n)
   remaining_coins = goal[0] - state[0]
   return sum(remaining_coins)


print(a_star())
