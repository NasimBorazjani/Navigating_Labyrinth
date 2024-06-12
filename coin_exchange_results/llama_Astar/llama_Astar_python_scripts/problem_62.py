
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the empty list of chosen coin values
   initial_state = (set(), [])
   # Define the goal state, as the sum of the chosen coins equaling 356
   goal_state = 356
   # Define the list of coins and their tax values
   coins = [35, 14, 9, 23, 25, 24, 21, 20, 12, 17, 12, 5, 2, 17, 25, 25, 26, 31, 7, 21, 10, 2, 27, 19, 32, 29, 11, 33, 3, 27, 17, 3, 18, 14, 2, 32, 14, 21, 12, 8, 3, 34, 13, 12, 2, 23, 13, 3, 3, 31, 23, 23, 6, 30, 30, 11, 21]
   taxes = {3: 1, 32: 16, 6: 5, 20: 13, 13: 5, 31: 9, 23: 10, 35: 14, 24: 17, 11: 11, 9: 1, 12: 10, 5: 3, 8: 5, 34: 11, 17: 16, 25: 9, 26: 6, 30: 17, 27: 17, 7: 2, 18: 17, 33: 5, 14: 2, 29: 14, 10: 3, 2: 2, 21: 12, 19: 9}
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in the list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, chosen_coins, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the sum of the chosen coins is equal to 356
       if sum(state[1]) == goal_state:
           return chosen_coins


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the sum of the chosen coins plus the new coin does not exceed the goal state
           if coin not in state[0] and sum(state[1]) + coin <= goal_state:
               # Generate the new state
               new_state = (state[0] | {coin}, state[1] + [coin])
               # The cost so far is the sum of the taxes of the chosen coins, as we are trying to minimize the total tax paid
               new_cost = g + sum(taxes[c] for c in new_state[1])


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state, taxes), new_cost, chosen_coins + [coin], new_state))
   return None


def heuristic(state, goal, taxes):
   # An admissible and consistent heuristic for this problem is the sum of the taxes of the coins not chosen yet, plus the difference between the goal state and the sum of the chosen coins
   # This heuristic relaxes the constraint that the coins must be chosen in increasing order, as it considers the coins not chosen yet
   # It is admissible because it never overestimates the cost to reach the goal, as each unchosen coin must be chosen at least once
   # It's consistent because moving a coin from the unchosen set to the chosen set reduces the heuristic cost of the successor node by a max of the tax of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax of the moved coin) + h(n)
   h = 0
   for coin in state[0]:
       h += taxes[coin]
   h += goal - sum(state[1])
   return h


print(a_star())
