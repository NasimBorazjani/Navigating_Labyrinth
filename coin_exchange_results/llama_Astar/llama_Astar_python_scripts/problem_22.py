
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the chosen coins equaling 268
   goal_sum = 268
   # Define the tax values for each coin
   tax_values = {66: 17, 9: 3, 15: 10, 7: 6, 3: 3, 13: 7, 11: 10, 25: 14, 22: 18, 24: 17, 12: 6, 23: 18, 2: 2, 10: 5, 19: 10, 20: 19, 5: 4, 16: 1, 21: 20, 69: 14, 4: 4}
   # Define the list of coins
   coins = [10, 2, 5, 22, 15, 3, 4, 66, 3, 11, 21, 16, 69, 2, 19, 20, 9, 24, 24, 20, 12, 13, 21, 7, 7, 23, 25, 10]
   # Define the dictionary of coin values and their tax values
   coin_tax_values = {coin: tax_values[coin] for coin in coins}
   # Define the dictionary of coin values and their indices in the coins list
   coin_indices = {coin: index for index, coin in enumerate(coins)}
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in a list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, chosen_coins, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the sum of the chosen coins equals the goal sum
       if sum(state[0]) == goal_sum:
           return chosen_coins


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the sum of the chosen coins does not exceed the goal sum
           if coin not in state[0] and sum(state[0]) + coin <= goal_sum:
               # Generate the new state
               new_state = (state[0] | {coin}, state[1] + coin_tax_values[coin])
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g + coin_tax_values[coin]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum, coin_indices), new_cost, chosen_coins + [coin], new_state))
   return None


def heuristic(state, goal_sum, coin_indices):
   # An admissible and consistent heuristic for this problem is the sum of the remaining coins to be chosen, plus the difference between the goal sum and the sum of the chosen coins
   # This heuristic relaxes the constraint that the coins must be chosen in increasing order of their values
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the value of the moved coin) + h(n)
   remaining_coins = [coin for coin in coin_indices if coin not in state[0]]
   remaining_coins.sort(key=lambda coin: coin_indices[coin])
   return sum(remaining_coins) + abs(goal_sum - sum(state[0]))


print(a_star())
