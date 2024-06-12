
import heapq
from collections import defaultdict


def a_star():
   # Define the initial state of the problem, which is an empty list of coins
   initial_state = []
   # Define the goal state of the problem, which is a sum of 206
   goal_sum = 206
   # Define the coins available and their tax values
   coins = [9, 18, 7, 20, 4, 12, 5, 5, 18, 5, 2, 11, 5, 16, 19, 8, 10, 9, 12, 14, 17, 6, 14, 16, 20, 10, 10, 13, 4, 13, 7, 14, 14, 10, 2, 7, 14, 11, 16, 10, 10, 5, 14, 20, 4, 17]
   tax_values = {17: 16, 8: 8, 6: 6, 16: 12, 5: 4, 14: 12, 18: 9, 12: 1, 19: 12, 4: 2, 7: 3, 10: 7, 11: 7, 13: 6, 2: 1, 9: 1, 20: 10}
   # Define the constraints on the coins that can be chosen based on the previous coin chosen
   constraints = defaultdict(lambda: lambda x: x % 2 == 0, {True: lambda x: x % 2 == 1})


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


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


       # Generate all possible actions from the current state, which includes adding any of the coins to the current state
       for coin in coins:
           # Check if the new state would be valid, ie the coin must satisfy the constraints based on the previous coin chosen
           if (not state or constraints[state[-1] <= coin](coin)) and sum(state) + coin <= goal_sum:
               # Generate the new state
               new_state = state + [coin]
               # The cost so far is the sum of the tax values of the coins chosen, as the task is to minimize the total tax paid
               new_cost = g + tax_values[coin]


               # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   h = heuristic(new_state, goal_sum)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_sum):
   # An admissible and consistent heuristic for this problem is the difference between the goal sum and the sum of the coins chosen so far
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as each coin chosen increases the sum of the coins by its value, which is always less than or equal to the remaining sum required to reach the goal
   # It's consistent because the cost of choosing a coin is its tax value, which is always greater than or equal to 0, and the estimated cost of the successor node is always less than or equal to the estimated cost of the current node, as the sum of the coins in the successor node is always greater than or equal to the sum of the coins in the current node
   return goal_sum - sum(state)


print(a_star())
