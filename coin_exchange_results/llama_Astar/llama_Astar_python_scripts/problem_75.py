
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total value of the coins that sum up to 408
   goal_value = 408
   # Define the list of coins and their tax values
   coins = [8, 31, 28, 24, 19, 18, 26, 31, 43, 32, 3, 21, 21, 10, 36, 40, 19, 38, 3, 5, 24, 12, 11, 14, 40, 7, 19, 4, 22, 5, 33, 31, 40, 7, 5, 34, 33, 22, 14, 6, 14, 29]
   taxes = {31: 12, 40: 17, 32: 19, 26: 14, 12: 1, 5: 3, 36: 1, 33: 5, 3: 2, 6: 1, 34: 19, 18: 18, 8: 7, 21: 11, 43: 20, 22: 20, 4: 4, 11: 6, 28: 20, 7: 3, 38: 13, 24: 12, 19: 16, 10: 7, 14: 9, 29: 3}
   # Define the dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in a list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the total value of the chosen coins is equal to the goal value
       if sum(state[0]) == goal_value:
           return actions


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the total value of the chosen coins does not exceed the goal value
           if coin not in state[0] and sum(state[0]) + coin <= goal_value:
               # Generate the new state
               new_state = (state[0] | {coin}, state[1] + taxes[coin])
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g + taxes[coin]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_value), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_value):
   # An admissible and consistent heuristic for this problem is the sum of the values of the remaining coins to be chosen, to reach the goal value
   # This heuristic relaxes the constraint that the coins must be chosen in increasing or decreasing order, and the tax values must be paid
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax of the moved coin) + h(n)
   remaining_coins = goal_value - sum(state[0])
   return remaining_coins


print(a_star())
