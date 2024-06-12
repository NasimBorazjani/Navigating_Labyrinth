
import heapq


def a_star():
   # Define the initial state of the problem, which is an empty list of coins
   initial_state = []
   # Define the goal state of the problem, which is a sum of 410
   goal_state = 410
   # Define the coins and their tax values
   coins = [14, 8, 11, 30, 3, 3, 27, 16, 19, 4, 6, 14, 7, 2, 39, 103, 15, 100, 27, 36, 7, 36, 13, 7, 18, 39, 14, 3, 28]
   tax_values = {13: 11, 18: 8, 36: 15, 11: 4, 6: 1, 16: 8, 100: 12, 39: 10, 28: 9, 27: 20, 103: 6, 19: 5, 30: 14, 2: 1, 4: 3, 3: 3, 15: 10, 8: 5, 7: 2, 14: 14}
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
           # Check if the new state would be valid, ie the coin must not already be in the state, and the sum of the coins in the new state must not exceed the goal state
           if coin not in state and sum(state) + coin <= goal_state:
               # The coin must be smaller than the previous one and have an even value, or be larger than or equal to the previous coin and have an odd value
               if (not state or (coin < state[-1] and coin % 2 == 0) or (coin >= state[-1] and coin % 2 == 1)):
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
   # The heuristic is admissible because it never overestimates the cost to reach the goal state, as the sum of the coins in the state can never exceed the goal state
   # The heuristic is consistent because the cost of adding a coin to the state is always less than or equal to the decrease in the heuristic, which is the value of the coin
   return goal - sum(state)


print(a_star())
