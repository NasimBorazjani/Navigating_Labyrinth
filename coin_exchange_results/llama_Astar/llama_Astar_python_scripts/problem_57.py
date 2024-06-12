
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total value of the coins that must be equal to 322
   goal_value = 322
   # Define the tax values for each coin
   tax_values = {11: 1, 14: 4, 7: 2, 25: 4, 12: 5, 20: 19, 13: 6, 15: 11, 30: 18, 1: 1, 2: 2, 31: 6, 10: 2, 23: 1, 6: 2, 21: 18, 18: 8, 28: 15, 17: 5, 26: 6, 22: 6, 9: 1, 19: 2, 5: 4}
   # Define the list of coins
   coins = [25, 22, 28, 23, 5, 14, 28, 14, 20, 6, 22, 1, 25, 18, 30, 10, 19, 12, 17, 17, 6, 28, 21, 28, 21, 2, 20, 2, 19, 14, 31, 31, 14, 7, 20, 13, 7, 18, 22, 15, 6, 6, 21, 9, 18, 11, 20, 26, 15]
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in a list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, chosen_coins, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the total value of the chosen coins is equal to 322
       if sum(state[0]) == goal_value:
           return chosen_coins


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the total value of the chosen coins does not exceed 322
           if coin not in state[0] and sum(state[0]) + coin <= goal_value:
               # Generate the new state
               new_state = (state[0] | {coin}, state[1] + tax_values[coin])
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g + tax_values[coin]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_value), new_cost, chosen_coins + [coin], new_state))
   return None


def heuristic(state, goal_value):
   # An admissible and consistent heuristic for this problem is the difference between the total value of the coins chosen so far and the goal value
   # This heuristic relaxes the constraint that the coins must be chosen in increasing order of their values
   # It is admissible because it never overestimates the cost to reach the goal, as the cost of choosing a coin is always equal to or less than the cost of reaching the successor node
   # It's consistent because moving a coin from one state to another reduces the heuristic cost of the successor node by a max of the value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax of the moved coin) + h(n)
   return goal_value - sum(state[0])


print(a_star())
