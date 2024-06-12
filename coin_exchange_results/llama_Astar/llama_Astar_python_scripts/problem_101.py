
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the empty list of chosen coin values
   initial_state = (set(), [])
   # Define the goal state, as the sum of the chosen coins equaling 477
   goal_state = 477
   # Define the tax values for each coin
   tax_values = {41: 15, 22: 3, 9: 4, 34: 9, 32: 11, 36: 5, 18: 5, 40: 9, 46: 11, 45: 17, 33: 3, 14: 9, 12: 12, 7: 2, 43: 14, 25: 18, 31: 9, 51: 8, 24: 18, 17: 3, 16: 5, 19: 10, 6: 6, 27: 15, 42: 7, 23: 2, 29: 2, 21: 13, 30: 7, 44: 4, 5: 2, 20: 11, 26: 12, 15: 8}
   # Define the list of coins
   coins = [29, 25, 15, 12, 40, 23, 36, 22, 16, 24, 51, 34, 46, 29, 20, 14, 21, 27, 15, 31, 15, 17, 9, 42, 30, 45, 14, 14, 30, 16, 44, 32, 6, 15, 5, 41, 18, 43, 36, 31, 27, 26, 6, 44, 33, 23, 7, 19]
   # Define the set of unique coin values
   unique_coins = set(coins)
   # Define the dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in the list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the sum of the chosen coins is equal to 477
       if sum(state[1]) == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes choosing a coin from the list of coins
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the sum of the chosen coins does not exceed the goal state
           if coin not in state[0] and sum(state[1]) + coin <= goal_state:
               # Generate the new state
               new_state = (state[0] | {coin}, state[1] + [coin])
               # The cost so far is the sum of the chosen coins, as we are trying to minimize the sum of the chosen coins
               new_cost = g + coin
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state, tax_values), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal, tax_values):
   # An admissible and consistent heuristic for this problem is the sum of the tax values of the chosen coins
   # This heuristic relaxes the constraint that the tax for coins of the same value is the same
   # It is admissible because it never overestimates the cost to reach the goal, as each coin must be taxed at least once
   # It's consistent because moving a coin from one state to another reduces the heuristic cost of the successor node by a max of the tax value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax value of the moved coin) + h(n)
   h = 0
   for coin in state[1]:
       h += tax_values[coin]
   return h


print(a_star())
