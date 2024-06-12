
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the coins that need to be chosen
   goal_sum = 452
   # Define the tax values for each coin
   tax_values = {9: 6, 14: 9, 24: 8, 26: 12, 16: 6, 45: 14, 8: 3, 22: 8, 38: 9, 40: 14, 31: 9, 257: 11, 36: 2, 2: 1, 41: 6, 29: 6, 39: 4}
   # Define the list of coins
   coins = [38, 36, 40, 31, 39, 29, 36, 31, 16, 14, 16, 45, 40, 45, 257, 8, 39, 16, 2, 41, 9, 26, 22, 24]
   # Define the set of used coins
   used_coins = set()
   # Define the set of available coins
   available_coins = set(coins)
   # Define the dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in the list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the total sum of the chosen coins is equal to the goal sum
       if sum(state[0]) == goal_sum:
           return actions


       # Generate all possible actions from the current state, which includes choosing a coin from the available coins
       for coin in available_coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the tax for the coin is even if it is smaller than the previous chosen coin, and odd if it is larger or equal
           if coin not in used_coins and (not state[0] or (coin < max(state[0]) and tax_values[coin] % 2 == 0) or (coin >= max(state[0]) and tax_values[coin] % 2 == 1)):
               # Generate the new state
               new_state = (state[0] | {coin}, g + tax_values[coin])
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g + tax_values[coin]
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
                  
   return None


def heuristic(state, goal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the values of the remaining coins to be chosen, minus the goal sum
   # This heuristic relaxes the constraint that the coins must be chosen in increasing order, and the tax for the coin is even if it is smaller than the previous chosen coin, and odd if it is larger or equal
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the available coins to the chosen coins reduces the heuristic cost of the successor node by a max of the value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax for the moved coin) + h(n)
   return sum(coin for coin in state[0]) - goal_sum


print(a_star())
