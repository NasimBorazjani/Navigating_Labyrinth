
import heapq


def a_star():
   # Define the initial state of the problem, which is an empty list of coins
   initial_state = []
   # Define the goal state of the problem, which is a sum of 307
   goal_state = 307
   # Define the coins and their tax values
   coins = [29, 29, 22, 23, 23, 3, 26, 9, 15, 8, 21, 15, 29, 25, 71, 27, 23, 6, 7, 9, 15, 21, 6, 8, 19, 17, 18, 6, 26, 24, 24, 3, 25, 2]
   tax_values = {24: 14, 2: 1, 25: 2, 26: 14, 18: 12, 27: 15, 29: 19, 19: 3, 15: 7, 9: 1, 8: 1, 21: 18, 6: 1, 71: 3, 23: 4, 17: 7, 7: 2, 22: 11, 3: 1}
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(initial_state)] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   queue = [(0, 0, [], initial_state)]
   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)
       # If the sum of the coins in the current state is equal to the goal state, return the actions taken
       if sum(state) == goal_state:
           return actions
       # Generate all possible actions from the current state, which includes adding any of the remaining coins to the current state
       for coin in coins:
           # Check if the new state would be valid, ie the coin must be smaller than the previous one and have an even value, or be larger than or equal to the previous coin and have an odd value
           if (not state or (coin < state[-1] and coin % 2 == 0) or (coin >= state[-1] and coin % 2 == 1)) and sum(state) + coin <= goal_state:
               # Generate the new state
               new_state = state + [coin]
               # The cost so far is the sum of the tax values of the coins in the state
               new_cost = g + tax_values[coin]
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                   visited_costs[tuple(new_state)] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the difference between the goal state and the sum of the coins in the current state
   # The heuristic is admissible because it never overestimates the cost to reach the goal state, as the sum of the coins in the current state can only increase
   # The heuristic is consistent because the cost of adding a coin to the current state is always less than or equal to the decrease in the heuristic, which is the value of the coin added
   return goal - sum(state)


print(a_star())
