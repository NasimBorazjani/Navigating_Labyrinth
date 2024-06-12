
import heapq


def a_star():
   # Define the initial state of the problem, which is an empty list of coins
   initial_state = []
   # Define the goal state of the problem, which is a sum of 324
   goal_sum = 324
   # Define the coins and their tax values
   coins = [11, 6, 147, 6, 19, 29, 28, 32, 18, 20, 12, 22, 4, 20, 27, 3, 3, 18, 19, 9, 2, 28, 31, 20, 2, 27, 22, 30, 3]
   tax_values = {27: 18, 6: 2, 22: 12, 18: 11, 4: 3, 12: 4, 28: 6, 147: 10, 32: 6, 19: 3, 29: 12, 31: 19, 20: 4, 2: 2, 30: 17, 3: 2, 11: 10, 9: 2}
   # Sort the coins in descending order to ensure that we always choose the largest possible coin first
   coins.sort(reverse=True)


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(initial_state)] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if sum(state) == goal_sum:
           return actions


       # Generate all possible actions from the current state, which includes adding any of the remaining coins to the current state
       for coin in coins:
           # Check if adding the coin to the current state results in a valid state, ie the sum of the coins in the state does not exceed the goal sum
           if sum(state) + coin <= goal_sum:
               # Check if the coin satisfies the condition of being even if it is smaller than the last coin added, or odd if it is larger or equal
               if (state and coin < state[-1] and coin % 2 == 0) or (state and coin >= state[-1] and coin % 2 == 1) or not state:
                   # Generate the new state
                   new_state = state + [coin]
                   # The cost so far is the sum of the tax values of the coins in the state
                   new_cost = g + tax_values[coin]
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                       visited_costs[tuple(new_state)] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the difference between the goal sum and the current sum of the coins in the state
   # The heuristic is admissible because it never overestimates the cost to reach the goal, as we can never add a coin that makes the sum of the coins in the state exceed the goal sum
   # The heuristic is consistent because the cost of moving to a successor state is always 1, which is exactly the decrease in the heuristic, as we add a coin to the state
   return goal - sum(state)


print(a_star())
