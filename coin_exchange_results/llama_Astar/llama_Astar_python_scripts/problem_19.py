
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the coins to be chosen, which is 243
   goal_sum = 243
   # Define the tax values for each coin
   tax_values = {20: 3, 9: 2, 23: 1, 10: 3, 5: 4, 21: 14, 22: 5, 18: 7, 16: 4, 13: 5, 2: 1, 8: 2, 19: 16, 7: 3, 6: 6, 11: 3, 14: 8, 4: 2, 12: 7, 15: 14}
   # Define the list of coins
   coins = [9, 20, 4, 23, 10, 11, 8, 6, 20, 8, 20, 12, 15, 20, 18, 16, 19, 21, 5, 6, 4, 5, 14, 5, 4, 18, 22, 7, 8, 15, 5, 15, 8, 19, 14, 12, 2, 5, 5, 15, 2, 6, 10, 18, 14, 13, 8, 10, 21, 14, 5, 18, 16, 6, 11]
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


       # Check if the current state is the goal state, ie the total sum of the chosen coins equals the goal sum
       if sum(state[0]) == goal_sum:
           return chosen_coins


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the total sum of the chosen coins does not exceed the goal sum
           if coin not in state[0] and sum(state[0]) + coin <= goal_sum:
               # Generate the new state
               new_state = (state[0] | {coin}, state[1] + tax_values[coin])
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g + tax_values[coin]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, chosen_coins + [coin], new_state))
   return None


def heuristic(state, goal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the remaining coins to be chosen, minus the goal sum
   # This heuristic relaxes the constraint that the coins must be chosen in increasing order, as the heuristic estimate for the goal state is 0, as the remaining coins to be chosen would be 0 in the goal state
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax of the chosen coin) + h(n)
   return goal_sum - sum(state[0])


print(a_star())
