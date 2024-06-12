
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the empty list of chosen coin values
   initial_state = (set(), [])
   # Define the goal state, as the sum of the chosen coin values equal to 474
   goal_state = (None, 474)
   # Define the list of coins and their tax values
   coins = [21, 13, 10, 18, 21, 43, 42, 29, 14, 19, 9, 2, 15, 19, 32, 45, 24, 31, 25, 7, 21, 24, 29, 29, 4, 36, 29, 19, 29, 12, 3, 44, 40, 46, 33, 3, 28, 44, 25, 6, 36, 3, 4, 19, 31]
   taxes = {6: 3, 9: 7, 13: 11, 19: 11, 36: 17, 32: 11, 46: 1, 4: 3, 21: 14, 3: 1, 18: 5, 29: 18, 12: 9, 2: 2, 15: 14, 43: 11, 24: 5, 25: 15, 14: 10, 42: 11, 44: 7, 31: 11, 40: 2, 33: 10, 45: 20, 7: 6, 10: 3, 28: 5}
   # Define the dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in a list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[1] == goal_state[1]:
           return actions


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the sum of the chosen coin values does not exceed the goal sum
           if coin not in state[0] and sum(state[0]) + coin <= goal_state[1]:
               # Generate the new state
               new_state = (state[0] | {coin}, state[1] + coin)
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g + taxes[coin]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the difference between the goal sum of the chosen coin values and the current sum of the chosen coin values
   # This heuristic relaxes the constraint that the coin chosen must have an even value if it is smaller than the previous one, and an odd value if it is larger than or equal to the previous coin chosen
   # It is admissible because it never overestimates the cost to reach the goal, as the cost of choosing a coin is always less than or equal to the cost of reaching the successor node
   # It's consistent because moving a coin from one state to another reduces the heuristic cost of the successor node by a max of the tax of the moved coin, which is equal to the cost of reaching the successor node
   return goal[1] - state[1]


print(a_star())
