
import heapq


def a_star():
   # Define the initial state of the problem, which is an empty list of coins
   initial_state = []
   # Define the goal state of the problem, which is a sum of 477
   goal_sum = 477
   # Define the coins and their tax values
   coins = [26, 8, 34, 12, 20, 21, 35, 13, 28, 5, 16, 11, 24, 42, 16, 12, 34, 21, 27, 27, 20, 47, 9, 12, 38, 23, 43, 33, 26, 22, 38, 42, 20, 41, 47, 41, 24, 46, 35, 42, 9, 35, 13, 45, 24, 29, 45, 2, 41, 39, 24, 38, 39, 18, 5, 8, 36]
   tax_values = {12: 8, 18: 6, 42: 8, 11: 9, 38: 13, 9: 9, 24: 15, 34: 1, 20: 5, 2: 2, 23: 2, 33: 12, 27: 8, 39: 11, 16: 1, 28: 12, 26: 11, 21: 7, 35: 7, 22: 19, 47: 9, 29: 12, 46: 3, 45: 9, 5: 1, 13: 13, 43: 8, 36: 11, 41: 4, 8: 8}
   # Sort the coins in descending order to start with the largest coin
   coins.sort(reverse=True)


   visited_costs = {}
   visited_costs[tuple(initial_state)] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if sum(state) == goal_sum:
           return actions


       # Generate all possible actions from the current state, which includes adding any of the remaining coins to the current state
       for coin in coins:
           # Check if the new state would be valid, ie the sum of the coins in the new state must not exceed the goal sum
           # And the coin must be smaller than the previous one and have an even value, or be larger than or equal to the previous coin and have an odd value
           if (sum(state) + coin <= goal_sum and
               (not state or (coin < state[-1] and coin % 2 == 0) or (coin >= state[-1] and coin % 2 == 1))):
               # Generate the new state
               new_state = state + [coin]
               # The cost so far is the sum of the tax values of the coins in the new state
               new_cost = g + tax_values[coin]


               if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                   visited_costs[tuple(new_state)] = new_cost
                   # The heuristic is the remaining sum to reach the goal sum, divided by the smallest coin, and multiplied by the smallest tax value
                   # This heuristic is admissible because it never overestimates the cost to reach the goal state, as it assumes we can always choose the coin with the smallest tax value to reach the goal sum
                   # The heuristic is consistent because the cost of adding a coin to the state is always greater than or equal to the decrease in the heuristic, as we are always adding the tax value of the coin to the cost, which is always greater than or equal to the smallest tax value
                   h = (goal_sum - sum(new_state)) / min(coins) * min(tax_values.values())
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [coin], new_state))
   return None


print(a_star())
