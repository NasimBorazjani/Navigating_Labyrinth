
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the empty list of chosen coin values
   initial_state = (set(), [])
   # Define the goal state, as the sum of the chosen coins equaling 485
   goal_state = 485
   # Define the tax values for each coin
   tax_values = {44: 6, 39: 15, 4: 2, 23: 11, 7: 2, 40: 10, 13: 10, 34: 8, 45: 9, 10: 3, 35: 18, 14: 2, 28: 5, 46: 12, 25: 3, 26: 18, 15: 11, 31: 2, 20: 15, 9: 7, 41: 13, 18: 16, 32: 11, 3: 3, 48: 20, 38: 4, 43: 6, 33: 9, 16: 13, 8: 4, 17: 1, 47: 17, 6: 5}
   # Define the list of coins
   coins = [40, 28, 46, 16, 13, 15, 38, 39, 3, 8, 40, 41, 18, 48, 16, 25, 39, 14, 47, 46, 31, 16, 41, 45, 9, 26, 33, 46, 17, 23, 6, 46, 7, 43, 10, 28, 47, 15, 35, 20, 32, 4, 32, 9, 48, 7, 34, 46, 10, 39, 44]
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in the list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, chosen_coins, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the sum of the chosen coins is equal to 485
       if sum(state[1]) == goal_state:
           return chosen_coins


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the sum of the chosen coins plus the new coin does not exceed the goal state
           if coin not in state[0] and sum(state[1]) + coin <= goal_state:
               # Generate the new state
               new_state = (state[0] | {coin}, state[1] + [coin])
               # The cost so far is the sum of the chosen coins, as we are trying to minimize the total tax paid
               new_cost = g + sum(state[1])
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state, tax_values), new_cost, chosen_coins + [coin], new_state))
   return None


def heuristic(state, goal, tax_values):
   # An admissible and consistent heuristic for this problem is the sum of the tax values of the chosen coins
   # This heuristic relaxes the constraint that the tax for coins of the same value is the same
   # It is admissible because it never overestimates the cost to reach the goal, as the tax for each coin is a non-negative integer
   # It's consistent because moving a coin from one state to another reduces the heuristic cost of the successor node by a max of the tax value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax value of the moved coin) + h(n)
   h = 0
   for coin in state[1]:
       h += tax_values[coin]
   return h


print(a_star())
