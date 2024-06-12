
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total value of the coins that must be equal to 295
   goal_value = 295
   # Define the tax values for each coin
   tax_values = {2: 1, 13: 11, 26: 13, 5: 1, 4: 2, 9: 8, 15: 8, 18: 6, 20: 18, 3: 1, 17: 17, 6: 2, 10: 10, 12: 1, 23: 10, 7: 6, 29: 13, 25: 15, 11: 10, 27: 2, 24: 18, 25: 15, 29: 13, 27: 2}
   # Define the list of coins
   coins = [27, 17, 6, 5, 20, 3, 4, 29, 25, 27, 20, 18, 18, 25, 2, 13, 15, 4, 12, 4, 26, 12, 26, 24, 17, 23, 2, 6, 2, 29, 3, 20, 12, 7, 9, 12, 26, 11, 2, 5, 10, 25, 3, 13, 7, 25]
   # Define the dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in a list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, chosen_coins, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the total value of the chosen coins is equal to 295
       if sum(state[0]) == goal_value:
           return chosen_coins


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the total value of the chosen coins does not exceed 295
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
   # An admissible and consistent heuristic for this problem is the difference between the goal value and the current total value of the chosen coins
   # This heuristic relaxes the constraint that the coins must be chosen in increasing order, as the heuristic estimate for the goal state is 0, as the total value of the chosen coins would be equal to the goal value
   return goal_value - sum(state[0])


print(a_star())
