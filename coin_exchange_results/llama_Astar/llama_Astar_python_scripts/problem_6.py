
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total value of the coins that must be equal to 250
   goal_value = 250
   # Define the tax values for each coin
   tax_values = {12: 12, 19: 8, 84: 20, 24: 1, 5: 1, 3: 1, 4: 2, 87: 7, 10: 5, 25: 7, 6: 5, 20: 5, 15: 7, 23: 17, 13: 4, 17: 16, 2: 1, 8: 5}
   # Define the list of coins
   coins = [20, 25, 10, 4, 13, 3, 10, 17, 5, 25, 17, 2, 19, 24, 25, 10, 19, 8, 2, 20, 15, 84, 23, 87, 19, 8, 12, 17, 23, 6]
   # Sort the coins in descending order
   coins.sort(reverse=True)
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in the list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the total value of the chosen coins is equal to 250
       if sum(state[0]) == goal_value:
           return actions


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the total value of the chosen coins does not exceed 250
           if coin not in state[0] and sum(state[0]) + coin <= goal_value:
               # Generate the new state
               new_state = (state[0] | {coin}, state[1] + tax_values[coin])
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g + tax_values[coin]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_value), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_value):
   # An admissible and consistent heuristic for this problem is the difference between the goal value and the current total value of the chosen coins
   # This heuristic relaxes the constraint that the coins must be chosen in descending order
   # It is admissible because it never overestimates the cost to reach the goal, as the cost of choosing a coin is always equal to or less than the difference between the goal value and the current total value
   # It's consistent because moving a coin from the chosen set to the unchosen set reduces the heuristic cost of the successor node by a max of the value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax of the moved coin) + h(n)
   return goal_value - sum(state[0])


print(a_star())
