
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the subset of chosen coins that sum to 337 and the total tax paid
   goal_state = (set([2, 33, 9, 31, 19, 17, 28, 24, 6, 22, 26, 27, 29, 4, 10, 3, 11, 15, 7, 1, 12, 30, 14, 32, 13]), 100)
   # Define the list of coins and their tax values
   coins = [31, 9, 2, 24, 32, 6, 13, 29, 33, 22, 12, 28, 10, 7, 33, 15, 28, 7, 14, 26, 1, 10, 28, 30, 7, 29, 17, 2, 28, 13, 28, 17, 3, 4, 4, 4, 13, 3, 19, 2, 4, 26, 27, 27, 11, 25, 12]
   taxes = {2: 1, 33: 8, 9: 9, 31: 3, 19: 11, 17: 8, 28: 3, 24: 12, 6: 1, 22: 7, 26: 7, 27: 5, 29: 9, 4: 4, 10: 3, 3: 2, 11: 3, 15: 12, 7: 2, 1: 1, 12: 3, 30: 2, 14: 12, 32: 7, 13: 2, 25: 9}
   # Define the total tax paid so far
   total_tax = 0
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in each state in a list; no coins chosen in the initial state
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the total tax paid after adding the coin's tax is less than the goal total tax
           if coin not in state[0] and total_tax + taxes[coin] <= goal_state[1]:
               # Generate the new state
               new_state = (state[0].copy(), state[1] + taxes[coin])
               new_state[0].add(coin)
               # The cost so far is the total tax paid so far, as our objective is to minimize the total tax paid
               new_cost = g + taxes[coin]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the values of the remaining coins to be chosen, minus the total tax paid so far
   # This heuristic relaxes the constraint that the coins must be chosen in increasing or decreasing order, as it only considers the remaining coins to be chosen and their values
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax of the moved coin) + h(n)
   remaining_coins = set(coins) - state[0]
   return sum(coin for coin in remaining_coins) - state[1]


print(a_star())
