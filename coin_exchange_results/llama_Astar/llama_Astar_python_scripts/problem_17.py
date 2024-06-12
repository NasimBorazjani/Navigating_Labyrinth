
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the coins that need to be chosen
   goal_sum = 233
   # Define the tax values for each coin
   tax_values = {21: 18, 1: 1, 13: 3, 20: 2, 19: 7, 5: 4, 18: 4, 4: 1, 15: 5, 12: 7, 17: 5, 22: 10, 8: 3, 7: 5, 23: 11, 9: 7, 10: 8, 3: 2, 14: 4, 6: 1, 2: 2, 11: 10}
   # Define the list of coins
   coins = [4, 2, 18, 5, 18, 13, 22, 15, 5, 14, 15, 21, 23, 13, 19, 22, 6, 12, 19, 8, 15, 8, 12, 15, 11, 17, 7, 19, 23, 9, 3, 4, 12, 10, 11, 2, 22, 19, 19, 11, 18, 6, 10, 23, 20, 1, 6, 23, 8, 6]
   # Define the dictionary of coins and their tax values
   coins_tax_values = {coin: tax_values[coin] for coin in coins}
   # Define the dictionary of coins and their indices in the coins list
   coins_indices = {coin: index for index, coin in enumerate(coins)}
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in a list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, chosen_coins, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie if the sum of the chosen coins equals the goal sum
       if sum(state[0]) == goal_sum:
           return chosen_coins


       # Generate all valid actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the coin can be chosen, ie if it is not already in the chosen set and if it satisfies the conditions about the previous chosen coin
           if coin not in state[0] and (not chosen_coins or (chosen_coins[-1] < coin and coins_tax_values[coin] % 2 == 0) or (chosen_coins[-1] >= coin and coins_tax_values[coin] % 2 == 1)):
               # Generate the new state
               new_state = (state[0] | {coin}, state[1] + coins_tax_values[coin])
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g + coins_tax_values[coin]
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum, coins_tax_values, coins_indices), new_cost, chosen_coins + [coin], new_state))
                  
   return None


def heuristic(state, goal_sum, coins_tax_values, coins_indices):
   # An admissible and consistent heuristic for this problem is the sum of the tax values of the remaining coins to be chosen, plus the difference between the goal sum and the sum of the chosen coins
   # This heuristic relaxes the constraint that the tax for coins of the same value is the same
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the tax value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax value of the moved coin) + h(n)
   remaining_coins = [coin for coin in coins if coin not in state[0]]
   h = sum(coins_tax_values[coin] for coin in remaining_coins) + abs(goal_sum - sum(state[0]))
   return h


print(a_star())
