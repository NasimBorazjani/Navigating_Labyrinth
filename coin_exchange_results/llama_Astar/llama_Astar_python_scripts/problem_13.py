
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the chosen coins equaling 216
   goal_sum = 216
   # Define the tax values for each coin
   tax_values = {6: 6, 8: 6, 16: 4, 15: 11, 12: 3, 10: 5, 20: 14, 9: 3, 17: 8, 7: 5, 5: 5, 2: 1, 11: 4, 23: 18, 19: 3, 13: 13, 18: 6, 4: 3, 21: 20}
   # Define the list of coins
   coins = [20, 19, 2, 12, 23, 18, 15, 13, 10, 6, 9, 4, 9, 16, 5, 8, 19, 6, 7, 2, 6, 15, 10, 9, 4, 6, 19, 10, 10, 16, 21, 17, 21, 16, 13, 6, 16, 8, 7, 11, 13, 7, 21, 15, 15, 6, 11, 19, 7]
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in the list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the sum of the chosen coins equals the goal sum
       if sum(state[0]) == goal_sum:
           return actions


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the sum of the chosen coins does not exceed the goal sum
           if coin not in state[0] and sum(state[0]) + coin <= goal_sum:
               # Generate the new state
               new_state = (state[0] | {coin}, state[1] + tax_values[coin])
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g + tax_values[coin]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the values of the remaining coins to be chosen, minus the goal sum
   # This heuristic relaxes the constraint that the coins must be chosen in increasing or decreasing order, as the heuristic only considers the remaining coins to be chosen
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax of the moved coin) + h(n)
   remaining_coins = goal_sum - sum(state[0])
   return remaining_coins


print(a_star())
