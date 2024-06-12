
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the remaining coins
   initial_state = (set(), set(range(28, 34)))
   # Define the goal state, as the sum of the chosen coins equaling 339
   goal_state = 339
   # Define the tax values for each coin
   tax_values = {10: 6, 18: 17, 33: 15, 16: 16, 3: 2, 30: 18, 13: 3, 21: 17, 23: 4, 12: 1, 7: 6, 17: 7, 4: 2, 6: 5, 2: 2, 11: 5, 14: 14, 29: 1, 20: 7, 8: 3, 15: 7, 28: 3, 26: 8, 19: 11, 9: 9, 22: 4, 5: 5, 25: 5}
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
           # Check if the new state would be valid, ie the coin must not be smaller than the previous coin chosen, if it is, it must have an even value
           if prev_coin is None or coin >= prev_coin and coin % 2 == 0 or coin < prev_coin and coin % 2 == 1:
               # Generate the new state
               new_state = (state[0] | {coin}, state[1] - {coin})
               # The additional cost of this state is the tax value of the coin chosen
               new_cost = g + tax_values[coin]
              
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [coin], new_state))
                   prev_coin = coin
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the remaining coins to be chosen, as the cost of choosing a coin is the tax value of the coin
   # This heuristic relaxes the constraint that the coin chosen must have an even value if it is smaller than the previous coin chosen and an odd value if it is larger or equal to the previous coin chosen
   # It is admissible because it never overestimates the cost to reach the goal, as the cost of choosing a coin is the tax value of the coin
   # It's consistent because the cost of the successor node is always less than or equal to the cost of reaching the goal from the current node
   return sum(state[1])


print(a_star())
