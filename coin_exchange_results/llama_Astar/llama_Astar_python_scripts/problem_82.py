
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the chosen coins equaling 389
   goal_sum = 389
   # Define the tax values for each coin
   tax_values = {28: 10, 36: 13, 18: 13, 17: 8, 24: 3, 37: 19, 60: 16, 13: 5, 14: 8, 30: 18, 20: 5, 27: 16, 26: 11, 2: 2, 21: 3, 7: 7, 8: 6, 3: 3, 25: 20, 22: 8, 15: 12, 12: 4, 32: 11, 9: 5, 34: 15, 4: 2, 29: 5, 33: 6, 6: 6, 10: 3, 61: 10}
   # Define the list of coins
   coins = [7, 2, 20, 24, 9, 24, 29, 6, 32, 26, 17, 61, 33, 14, 12, 20, 15, 34, 60, 18, 18, 37, 25, 9, 9, 21, 24, 30, 28, 3, 21, 32, 13, 10, 4, 2, 33, 36, 13, 24, 27, 7, 21, 4, 8, 17, 22, 3, 21, 12]
   # Define the visited costs dictionary, where the key is the set of chosen coins and the value is the total tax paid so far
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in a list; no coins chosen initially
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
               new_state = (state[0] | {coin}, g + tax_values[coin])
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g + tax_values[coin]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the remaining coins to be chosen, minus the goal sum
   # This heuristic relaxes the constraint that the coin chosen must be smaller than the previous one, or larger than or equal to the previous coin chosen
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the value of the coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax of the coin) + h(n)
   return goal_sum - sum(state[0])


print(a_star())
