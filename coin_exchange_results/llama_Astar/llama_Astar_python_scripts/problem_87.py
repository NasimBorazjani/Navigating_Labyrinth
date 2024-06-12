
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = ([], 0)
   # Define the goal state, as the total sum of the chosen coins equal to 449
   goal_sum = 449
   # Define the tax values for each coin
   tax_values = {21: 5, 26: 13, 36: 8, 28: 8, 34: 12, 3: 2, 6: 2, 23: 10, 2: 2, 9: 5, 41: 4, 29: 19, 7: 6, 18: 18, 43: 2, 8: 7, 181: 9, 25: 10, 33: 8, 14: 13, 13: 1, 22: 13, 40: 7, 37: 11, 19: 11}
   # Define the list of coins
   coins = [25, 41, 34, 19, 19, 36, 37, 13, 28, 26, 181, 7, 14, 6, 29, 36, 33, 7, 8, 43, 19, 9, 3, 2, 18, 40, 43, 22, 23, 21]
   # Define the dictionary of coin values and their tax values
   coin_values = {coin: tax for coin, tax in zip(coins, tax_values[coin] for coin in coins)}
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in the list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the sum of the chosen coins is equal to 449
       if sum(state[0]) == goal_sum:
           return actions


       # Generate all valid actions from the current state, which includes choosing a coin from the list
       for coin in coin_values:
           # Check if the new state would be valid, ie the coin is not already chosen and the sum of the chosen coins does not exceed 449
           if coin not in state[0] and sum(state[0]) + coin <= goal_sum:
               # Generate the new state
               new_state = ([coin] + state[0], state[1] + coin_values[coin])
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g + coin_values[coin]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
                  
   return None


def heuristic(state, goal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the values of the remaining coins to be chosen, to reach the goal sum
   # This heuristic relaxes the constraint that the coin chosen must be smaller than the previous one, if it is smaller, and larger than or equal to the previous one, if it is larger
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the value of the moved coin) + h(n)
   remaining_coins = goal_sum - sum(state[0])
   return remaining_coins


print(a_star())
