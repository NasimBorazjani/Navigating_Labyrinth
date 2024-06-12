
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total value of the coins that adds up to 403
   goal_value = 403
   # Define the list of coins and their tax values
   coins = [8, 8, 6, 36, 7, 36, 33, 3, 31, 17, 21, 28, 41, 17, 23, 16, 39, 2, 3, 40, 23, 20, 5, 30, 8, 28, 17, 34, 38, 26, 16, 21, 15, 21, 11, 33, 5, 33, 2, 27, 26, 21, 14, 13, 7, 23]
   taxes = {28: 16, 5: 1, 3: 3, 40: 18, 33: 20, 34: 12, 20: 4, 39: 13, 2: 2, 31: 11, 36: 2, 17: 14, 7: 1, 14: 6, 23: 12, 8: 1, 30: 15, 27: 13, 15: 2, 21: 3, 11: 6, 26: 14, 41: 2, 38: 10, 6: 5, 16: 4, 13: 11}
   # Define the dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in a list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the total value of the chosen coins adds up to 403
       if sum(state[0]) == goal_value:
           return actions


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the total value of the chosen coins does not exceed 403
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
   # This heuristic relaxes the constraint that the coin chosen must have an even value if it is smaller than the previous one, and an odd value if it is larger than or equal to the previous coin chosen
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax of the moved coin) + h(n)
   remaining_coins = goal_value - sum(state[0])
   return remaining_coins


print(a_star())
