
import heapq


def a_star():
   # Define the initial state of the problem, which is an empty list of coins
   initial_state = []
   # Define the goal state of the problem, which is a list of coins that sum up to 305
   goal_sum = 305
   # Define the list of coins and their tax values
   coins = [25, 29, 8, 11, 8, 25, 20, 16, 6, 4, 98, 7, 28, 24, 27, 16, 23, 26, 26, 99, 2, 7, 22, 7, 5, 24, 2]
   tax_values = {24: 5, 26: 16, 28: 20, 2: 1, 22: 16, 25: 11, 27: 7, 11: 4, 6: 3, 99: 17, 8: 5, 7: 5, 5: 3, 23: 5, 4: 4, 98: 16, 16: 3, 29: 5, 20: 19}
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(initial_state)] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   queue = [(0, 0, [], initial_state)]
   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)
       # If the sum of the coins in the current state equals the goal sum, return the actions taken
       if sum(state) == goal_sum:
           return actions
       # Generate all possible actions from the current state, which includes adding any of the remaining coins to the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin must be smaller than the previous one and have an even value, or be larger than or equal to the previous coin and have an odd value
           if (not state or (coin < state[-1] and coin % 2 == 0) or (coin >= state[-1] and coin % 2 == 1)) and coin not in state:
               # Generate the new state
               new_state = state + [coin]
               # The cost so far is the sum of the tax values of the coins in the state
               new_cost = g + tax_values[coin]
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                   visited_costs[tuple(new_state)] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_sum):
   # An admissible and consistent heuristic is the difference between the goal sum and the sum of the coins in the current state
   # The heuristic is admissible because it never overestimates the cost to reach the goal, as the sum of the coins in the state can never exceed the goal sum
   # The heuristic is consistent because the cost of adding a coin to the state is always less than or equal to the increase in the sum of the coins in the state, which is exactly the decrease in the heuristic
   return goal_sum - sum(state)


print(a_star())
