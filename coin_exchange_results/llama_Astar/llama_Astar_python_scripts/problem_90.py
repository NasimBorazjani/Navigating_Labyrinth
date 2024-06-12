
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total value of the coins that must be equal to 453
   goal_value = 453
   # Define the tax values for each coin
   tax_values = {13: 7, 9: 1, 38: 9, 19: 4, 31: 18, 25: 18, 40: 13, 4: 2, 15: 8, 45: 2, 10: 10, 20: 18, 5: 3, 35: 12, 30: 8, 8: 5, 21: 5, 43: 12, 32: 10, 6: 2, 24: 18, 3: 2, 33: 7, 42: 4, 36: 10, 34: 6, 26: 5, 18: 6}
   # Define the list of coins
   coins = [45, 45, 40, 38, 26, 3, 3, 21, 3, 35, 24, 9, 43, 10, 19, 5, 21, 36, 15, 18, 13, 33, 42, 34, 6, 20, 38, 25, 42, 19, 32, 9, 31, 4, 4, 25, 30, 8]
   # Define the dictionary of coin values and their tax values
   coin_tax_values = {coin: tax_values[coin] for coin in coins}
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


       # Check if the current state is the goal state, ie the total value of the chosen coins is equal to 453
       if sum(state[0]) == goal_value:
           return chosen_coins


       # Generate all valid actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the coin can be chosen, ie it is not already chosen and the total value of the chosen coins does not exceed 453
           if coin not in state[0] and sum(state[0]) + coin <= goal_value:
               # The coin can be chosen, generate the new state
               new_state = (state[0] | {coin}, state[1] + coin_tax_values[coin])
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g + coin_tax_values[coin]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_value), new_cost, chosen_coins + [coin], new_state))
   return None


def heuristic(state, goal_value):
   # An admissible and consistent heuristic for this problem is the difference between the total value of the coins chosen so far and the goal value
   # This heuristic relaxes the constraint that the total value of the coins chosen must be equal to 453
   # It is admissible because it never overestimates the cost to reach the goal, as the cost of choosing a coin is always equal to or greater than the decrease in the heuristic cost of the successor node
   # It's consistent because moving a coin from the chosen set to the unchosen set reduces the heuristic cost of the successor node by a max of the value of the coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the value of the coin) + h(n)
   return goal_value - sum(state[0])


print(a_star())
