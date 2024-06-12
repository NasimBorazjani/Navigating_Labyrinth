
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total value of the coins that must be equal to 355
   goal_value = 355
   # Define the tax values for each coin
   tax_values = {6: 5, 17: 7, 12: 10, 34: 9, 5: 1, 11: 7, 10: 8, 21: 19, 15: 3, 33: 6, 3: 2, 16: 12, 58: 19, 8: 7, 14: 5, 20: 8, 2: 2, 19: 19, 59: 14, 18: 15, 29: 8, 23: 6, 32: 5}
   # Define the list of coins
   coins = [19, 21, 16, 6, 34, 23, 8, 10, 14, 10, 59, 15, 17, 32, 11, 15, 8, 29, 58, 12, 3, 5, 11, 34, 2, 12, 20, 6, 29, 23, 10, 34, 33, 18]
   # Define the dictionary of coin values and their tax values
   coin_values = {coin: tax for coin, tax in zip(coins, tax_values[coin] for coin in coins)}
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in the list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]
  
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)
       # Check if the current state is the goal state, ie the total value of the chosen coins is equal to 355
       if sum(state[0]) == goal_value:
           return actions
       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coin_values:
           # Check if the new state would be valid, ie the coin is not already chosen and the total value of the chosen coins does not exceed 355
           if coin not in state[0] and sum(state[0]) + coin <= goal_value:
               # Generate the new state
               new_state = (state[0].copy(), state[1])
               new_state[0].add(coin)
               new_state[1] += coin_values[coin]
               new_state = tuple(new_state)
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g + coin_values[coin]
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_value), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_value):
   # An admissible and consistent heuristic for this problem is the difference between the total value of the coins chosen so far and the goal value
   # This heuristic relaxes the constraint that the total value of the coins chosen must be equal to 355
   # It is admissible because it never overestimates the cost to reach the goal, as the cost of reaching the goal state is 0
   # It's consistent because moving a coin from the chosen set to the unchosen set reduces the heuristic cost of the successor node by a max of the value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the value of the moved coin) + h(n)
   return goal_value - sum(state[0])


print(a_star())
