
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the coins that need to be chosen
   goal_sum = 355
   # Define the tax values for each coin
   tax_values = {26: 4, 34: 4, 7: 5, 28: 11, 35: 8, 18: 13, 25: 19, 14: 10, 23: 7, 6: 1, 10: 5, 21: 8, 13: 13, 2: 1, 3: 1, 30: 5, 4: 4, 31: 18, 11: 3, 9: 1, 8: 3, 5: 3, 32: 5, 15: 15, 33: 18, 16: 4}
   # Define the list of coins
   coins = [4, 33, 14, 32, 9, 32, 2, 35, 25, 10, 11, 6, 8, 26, 10, 25, 34, 21, 13, 15, 3, 15, 25, 3, 16, 3, 2, 25, 15, 23, 31, 35, 13, 14, 5, 7, 2, 18, 10, 8, 25, 30, 13, 35, 3, 26, 33, 2, 5, 26, 26, 28, 6]
   # Define the dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in a list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, chosen_coins, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the total sum of the chosen coins equals the goal sum
       if sum(state[0]) == goal_sum:
           return chosen_coins


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the total sum of the chosen coins does not exceed the goal sum
           if coin not in state[0] and sum(state[0]) + coin <= goal_sum:
               # Generate the new state
               new_state = (state[0] | {coin}, state[1] + tax_values[coin])
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g + tax_values[coin]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, chosen_coins + [coin], new_state))
   return None


def heuristic(state, goal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the remaining coins to be chosen, minus the goal sum
   # This heuristic relaxes the constraint that the coins must be chosen in increasing order, as the heuristic estimate for the goal state is 0, as the remaining coins to be chosen would be 0 in the goal state
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax of the moved coin) + h(n)
   remaining_coins = goal_sum - sum(state[0])
   return remaining_coins


print(a_star())
