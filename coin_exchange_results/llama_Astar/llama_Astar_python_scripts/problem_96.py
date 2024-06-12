
import heapq


def a_star():
   # Define the initial state of the problem, as an empty list representing the chosen coins
   initial_state = []
   # Define the goal sum, as 463
   goal_sum = 463
   # Define the tax values for each coin
   tax_values = {18: 11, 17: 7, 7: 6, 43: 2, 22: 3, 24: 11, 9: 3, 36: 10, 46: 4, 10: 3, 39: 5, 5: 5, 35: 15, 28: 8, 15: 2, 34: 6, 27: 3, 38: 11, 30: 20, 23: 18, 25: 10, 12: 1, 4: 1, 49: 16, 37: 6, 48: 17, 2: 2, 8: 4, 3: 1, 6: 3, 19: 10, 32: 19}
   # Define the list of coins
   coins = [22, 25, 37, 5, 46, 10, 23, 23, 3, 6, 34, 32, 34, 2, 3, 8, 4, 28, 32, 24, 15, 38, 17, 35, 9, 12, 12, 22, 34, 48, 39, 30, 7, 18, 10, 46, 30, 36, 49, 27, 22, 19, 9, 24, 43, 15]
   # Sort the coins in descending order
   coins.sort(reverse=True)
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(initial_state)] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in the list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the sum of the chosen coins equals the goal sum
       if sum(state) == goal_sum:
           return actions


       # Generate all valid actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the sum of the chosen coins plus the new coin does not exceed the goal sum
           if sum(state) + coin <= goal_sum:
               # Generate the new state
               new_state = state + [coin]
               # The cost so far is the sum of the chosen coins, as our objective is to minimize the sum of the chosen coins
               new_cost = g + coin
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                   visited_costs[tuple(new_state)] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum, tax_values), new_cost, actions + [coin], new_state))
                  
   return None


def heuristic(state, goal_sum, tax_values):
   # An admissible and consistent heuristic for this problem is the sum of the tax values of the coins in the current state
   # This heuristic relaxes the constraint that the tax value of a coin must be equal to the tax value of the previous coin chosen
   # It is admissible because it never overestimates the cost to reach the goal, as the tax value of a coin must be less than or equal to the tax value of the previous coin chosen
   # It's consistent because moving a coin from one state to another reduces the heuristic cost of the successor node by a max of the tax value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax value of the moved coin) + h(n)
   h = 0
   for coin in state:
       h += tax_values[coin]
   return h


print(a_star())
