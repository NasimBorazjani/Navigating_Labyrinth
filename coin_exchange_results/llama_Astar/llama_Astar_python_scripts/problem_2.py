
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the coins that need to be chosen
   goal_sum = 203
   # Define the tax values for each coin
   tax_values = {15: 5, 36: 15, 39: 9, 9: 8, 13: 3, 2: 2, 18: 10, 12: 12, 3: 3, 8: 8, 11: 6, 10: 4, 4: 4, 14: 10, 7: 3, 16: 16, 20: 18, 19: 17}
   # Define the list of coins
   coins = [13, 10, 12, 10, 16, 7, 9, 14, 13, 18, 36, 11, 7, 14, 7, 8, 19, 7, 39, 13, 3, 18, 20, 4, 3, 18, 15, 2, 19, 16]
   # Define the dictionary of coin values and their tax values
   coin_values = {coin: tax for coin, tax in zip(coins, tax_values[coin] for coin in coins)}
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
           # Check if the new state would be valid, ie the coin is not already chosen and the total tax paid does not exceed the goal tax
           if coin not in state[0] and state[1] + coin_values[coin] <= goal_sum:
               # Generate the new state
               new_state = (state[0].copy(), state[1] + coin_values[coin])
               new_state[0].add(coin)
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g + coin_values[coin]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum, coin_values), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_sum, coin_values):
   # An admissible and consistent heuristic for this problem is the sum of the values of the coins not chosen yet, plus the tax value of the largest coin not chosen yet
   # This heuristic relaxes the constraint that the coins must be chosen in increasing order of their values
   # It is admissible because it never overestimates the cost to reach the goal, as each coin not chosen must be chosen at least once
   # It's consistent because moving a coin from the not chosen set to the chosen set reduces the heuristic cost of the successor node by a max of the tax value of the largest coin not chosen yet, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax value of the largest coin not chosen yet) + h(n)
   not_chosen_coins = [coin for coin in coin_values if coin not in state[0]]
   if not_chosen_coins:
       return sum(coin_values[coin] for coin in not_chosen_coins) + max(coin_values[coin] for coin in not_chosen_coins)
   else:
       return 0


print(a_star())
