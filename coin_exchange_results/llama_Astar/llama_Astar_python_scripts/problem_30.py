
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the empty list of chosen coin values
   initial_state = (set(), [])
   # Define the goal state, as the sum of the chosen coins equaling 294
   goal_state = 294
   # Define the tax values for each coin
   tax_values = {21: 14, 19: 16, 4: 3, 23: 10, 10: 3, 18: 7, 9: 3, 27: 13, 20: 12, 13: 9, 26: 17, 3: 3, 6: 6, 49: 16, 2: 2, 15: 7, 28: 13, 46: 10, 8: 3, 7: 6, 22: 20, 14: 5, 16: 8}
   # Define the list of coins
   coins = [46, 10, 4, 8, 2, 22, 26, 49, 4, 19, 2, 9, 23, 28, 6, 21, 9, 14, 15, 21, 22, 3, 14, 2, 28, 13, 20, 2, 28, 7, 16, 27, 22, 18, 28, 10, 14, 14, 4, 20, 18]
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in the list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, chosen_coins, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the sum of the chosen coins is equal to 294
       if sum(state[1]) == goal_state:
           return chosen_coins


       # Generate all valid actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the sum of the chosen coins does not exceed 294
           if coin not in state[0] and sum(state[1]) + coin <= goal_state:
               # Generate the new state
               new_state = (state[0] | {coin}, state[1] + [coin])
               # The cost so far is the sum of the chosen coins, as we are trying to minimize the total tax paid
               new_cost = g + sum(state[1])
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state, tax_values), new_cost, chosen_coins + [coin], new_state))
                  
   return None


def heuristic(state, goal, tax_values):
   # An admissible and consistent heuristic for this problem is the sum of the tax values of the chosen coins
   # This heuristic relaxes the constraint that the tax for coins of the same value is the same
   # It is admissible because it never overestimates the cost to reach the goal, as each coin must be chosen at least once
   # It's consistent because moving a coin from one state to another reduces the heuristic cost of the successor node by a max of the tax value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax value of the moved coin) + h(n)
   h = 0
   for coin in state[1]:
       h += tax_values[coin]
   return h


print(a_star())
