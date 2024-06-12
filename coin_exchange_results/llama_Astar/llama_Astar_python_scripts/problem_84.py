
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the remaining coins
   initial_state = (set(), set(range(1, 43)))
   # Define the goal state, as the sum of the chosen coins equal to 426
   goal_state = 426
   # Define the tax values for each coin
   tax_values = {37: 11, 10: 3, 36: 8, 32: 3, 3: 1, 18: 16, 14: 5, 35: 5, 16: 15, 8: 5, 42: 20, 29: 4, 6: 1, 25: 9, 11: 4, 20: 15, 39: 6, 38: 14, 34: 6, 40: 11, 9: 2, 17: 6, 19: 8, 4: 4, 22: 20, 31: 3, 1: 1, 33: 18, 2: 2}
   # Define the previous coin chosen
   prev_coin = None


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if sum(state[0]) == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes choosing a coin from the remaining coins
       for coin in state[1]:
           # Check if the new state would be valid, ie the coin must not be smaller than the previous coin chosen and have an even value, or larger than or equal to the previous coin chosen and have an odd value
           if (prev_coin is None or coin > prev_coin and coin % 2 == 1 or coin < prev_coin and coin % 2 == 0):
               # Generate the new state
               new_state = (state[0] | {coin}, state[1] - {coin})
               # The additional cost of this state is the tax value of the coin
               new_cost = g + tax_values[coin]
              
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [coin], new_state))
                   prev_coin = coin
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the remaining coins to be chosen
   # This heuristic relaxes the constraint that the coin chosen must have an even value if it is smaller than the previous coin chosen and an odd value if it is larger than or equal to the previous coin chosen
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining coins to the chosen coins reduces the heuristic cost of the successor node by a max of the tax value of the coin, which is equal to the cost of reaching the successor node
   return goal - sum(state[1])


print(a_star())
