
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the remaining coins
   initial_state = (set(), set(range(1, 48)))
   # Define the goal state, as the sum of the chosen coins equal to 477
   goal_state = 477
   # Define the tax values for each coin
   tax_values = {12: 8, 18: 6, 42: 8, 11: 9, 38: 13, 9: 9, 24: 15, 34: 1, 20: 5, 2: 2, 23: 2, 33: 12, 27: 8, 39: 11, 16: 1, 28: 12, 26: 11, 21: 7, 35: 7, 22: 19, 47: 9, 29: 12, 46: 3, 45: 9, 5: 1, 13: 13, 43: 8, 36: 11, 41: 4, 8: 8}
   # Define the list of coins
   coins = [26, 8, 34, 12, 20, 21, 35, 13, 28, 5, 16, 11, 24, 42, 16, 12, 34, 21, 27, 27, 20, 47, 9, 12, 38, 23, 43, 33, 26, 22, 38, 42, 20, 41, 47, 41, 24, 46, 35, 42, 9, 35, 13, 45, 24, 29, 45, 2, 41, 39, 24, 38, 39, 18, 5, 8, 36]
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in a list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, chosen_coins, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the sum of the chosen coins is equal to 477
       if sum(chosen_coins) == goal_state:
           return chosen_coins


       # Generate all possible actions from the current state, which includes choosing a coin from the remaining coins
       for coin in state[1]:
           # Check if the new state would be valid, ie the chosen coin must be smaller than the previous chosen coin if it is smaller, and larger or equal to the previous coin if it is larger
           if not chosen_coins or (coin < chosen_coins[-1] and coin % 2 == 0) or (coin >= chosen_coins[-1] and coin % 2 == 1):
               # Generate the new state
               new_state = (chosen_coins | {coin}, state[1] - {coin})
               # The cost so far is the sum of the chosen coins, as we are trying to minimize the sum of the chosen coins
               new_cost = g + coin
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state, tax_values), new_cost, chosen_coins + [coin], new_state))
   return None


def heuristic(state, goal, tax_values):
   # An admissible and consistent heuristic for this problem is the sum of the tax values of the chosen coins
   # This heuristic relaxes the constraint that the chosen coins must be smaller than the previous chosen coin if it is smaller, and larger or equal to the previous coin if it is larger
   # It is admissible because it never overestimates the cost to reach the goal, as each coin must be chosen at least once
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the tax value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax value of the moved coin) + h(n)
   h = 0
   for coin in state[0]:
       h += tax_values[coin]
   return h


print(a_star())
