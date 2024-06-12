
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the coins that need to be chosen
   goal_sum = 462
   # Define the tax values of the coins
   tax_values = {33: 16, 21: 14, 4: 1, 13: 9, 23: 8, 2: 2, 12: 2, 41: 15, 46: 6, 45: 2, 34: 16, 24: 15, 19: 4, 5: 4, 35: 14, 6: 6, 37: 13, 26: 16, 43: 20, 15: 13, 111: 2, 38: 1, 10: 7, 32: 13, 20: 14, 27: 15, 36: 14, 25: 8, 14: 2, 28: 10, 8: 4}
   # Define the list of coins
   coins = [35, 14, 15, 111, 8, 4, 6, 37, 14, 33, 45, 32, 46, 41, 38, 19, 34, 14, 2, 4, 24, 36, 46, 33, 12, 2, 14, 28, 12, 21, 34, 26, 28, 27, 25, 4, 23, 43, 43, 20, 10, 13, 5, 36, 27, 36]
   # Define the dictionary of coins and their tax values
   coins_dict = {coin: tax for coin, tax in zip(coins, tax_values[coin] for coin in coins)}
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in a list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
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
               new_state = (state[0].copy(), state[1])
               new_state[0].add(coin)
               new_state[1] += coins_dict[coin]
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g + coins_dict[coin]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum, coins_dict), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_sum, coins_dict):
   # An admissible and consistent heuristic for this problem is the sum of the values of the remaining coins to be chosen, plus the tax value of the largest coin that can be chosen
   # This heuristic relaxes the constraint that the coins must be chosen in increasing order of their values
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the tax value of the largest coin that can be chosen, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax value of the largest coin that can be chosen) + h(n)
   remaining_coins = [coin for coin in coins_dict if coin not in state[0]]
   h = sum(coins_dict[coin] for coin in remaining_coins)
   if remaining_coins:
       h += max(coins_dict[coin] for coin in remaining_coins)
   return h


print(a_star())
