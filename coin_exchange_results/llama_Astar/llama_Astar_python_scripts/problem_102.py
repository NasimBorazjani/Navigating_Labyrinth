
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the chosen coins equaling 449
   goal_sum = 449
   # Define the tax values for each coin
   tax_values = {11: 4, 10: 3, 41: 9, 34: 4, 7: 2, 17: 16, 29: 8, 37: 1, 44: 8, 30: 13, 32: 9, 20: 18, 23: 8, 6: 4, 5: 3, 14: 3, 13: 7, 35: 4, 33: 5, 39: 9, 40: 11, 28: 3, 4: 2, 43: 14, 42: 15, 38: 14, 16: 5, 36: 5, 12: 9, 26: 1}
   # Define the list of coins
   coins = [14, 29, 39, 40, 16, 35, 17, 37, 43, 30, 28, 26, 13, 13, 42, 30, 10, 7, 44, 5, 34, 7, 32, 11, 40, 35, 12, 34, 35, 38, 29, 42, 33, 26, 4, 36, 41, 35, 26, 34, 16, 6, 38, 13, 41, 23, 20]
   # Sort the coins in descending order
   coins.sort(reverse=True)
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in a list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, chosen_coins, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the sum of the chosen coins equals the goal sum
       if sum(state[0]) == goal_sum:
           return chosen_coins


       # Generate all valid actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the sum of the chosen coins does not exceed the goal sum
           if coin not in state[0] and sum(state[0]) + coin <= goal_sum:
               # Generate the new state
               new_state = (state[0] | {coin}, state[1] + tax_values[coin])
               # The cost so far is the total tax paid so far, as our objective is to minimize the total tax paid
               new_cost = g + tax_values[coin]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, chosen_coins + [coin], new_state))
   return None


def heuristic(state, goal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the values of the remaining coins to be chosen, minus the goal sum
   # This heuristic relaxes the constraint that the coins must be chosen in descending order
   # It is admissible because it never overestimates the cost to reach the goal, as the remaining coins to be chosen must be chosen at least once
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax of the moved coin) + h(n)
   remaining_coins = goal_sum - sum(state[0])
   return remaining_coins


print(a_star())
