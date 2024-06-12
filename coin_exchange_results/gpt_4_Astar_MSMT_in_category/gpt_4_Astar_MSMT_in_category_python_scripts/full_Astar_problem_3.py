
import heapq


def initialize():
   # Define the initial state and the goal state of the problem
   initial_state = (0, 0, 0, 0)
   goal_sum = 215
   coins = [13, 19, 9, 4, 18, 17, 2, 14, 17, 17, 8, 6, 4, 10, 19, 37, 20, 19, 14, 7, 6, 11, 21, 9, 3, 10, 21, 20, 2, 17, 2]
   taxes = {14: 2, 18: 9, 11: 10, 9: 6, 10: 9, 13: 10, 37: 9, 6: 5, 2: 2, 4: 1, 8: 3, 19: 10, 17: 7, 7: 6, 3: 3, 21: 3, 20: 4}
   num_coins = len(coins)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, goal_sum, coins, taxes, num_coins, visited_costs, queue
  
def a_star():
  
   initial_state, goal_sum, coins, taxes, num_coins, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the sum of the coins in the current state equals the goal sum, return the actions taken
       if state[1] == goal_sum:
           return actions


       # Generate all possible actions from the current state, which includes choosing any of the remaining coins
       for i in range(state[0], num_coins):
           # Check if adding the coin to the current sum results in a valid state, ie the sum must not exceed the goal sum
           if state[1] + coins[i] <= goal_sum:
               # The coin must be smaller than the previous coin and have an even value, or be larger than or equal to the previous coin and have an odd value
               if (coins[i] < state[2] and coins[i] % 2 == 0) or (coins[i] >= state[2] and coins[i] % 2 == 1):
                   # Generate the new state
                   new_state = (i + 1, state[1] + coins[i], coins[i], state[3] + taxes[coins[i]])
                   # The cost so far is the sum of the taxes of the coins chosen, as our objective is to minimize the total tax paid
                   new_cost = g + taxes[coins[i]]


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The heuristic is the sum of the taxes of the remaining coins, as we are trying to minimize the total tax paid
                       h = heuristic(new_state, goal_sum, coins, taxes)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [coins[i]], new_state))
   return None




def heuristic(state, goal_sum, coins, taxes):
   # The heuristic function can be a simulation of choosing the remaining coins greedily, choosing the coin with the smallest tax repeatedly as long as the sum of the coins does not exceed the goal sum
   # This heuristic is admissible because it is greedy, always opting for the action that minimizes the total tax paid, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a coin is removed from the state, or equal or less by at most the tax of the coin (equal to the cost of reaching the successor node, ie the tax of the coin) as the coin with the smallest tax is chosen to be added to the state in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to the tax of the coin) + h(n’)
   h = 0
   # Sort the remaining coins by increasing tax
   remaining_coins = sorted(coins[state[0]:], key=lambda x: taxes[x])
   # Iterate through the remaining coins
   for coin in remaining_coins:
       # Add the coin to the state as long as the sum of the coins does not exceed the goal sum
       if state[1] + coin <= goal_sum:
           # Increment the estimated cost to the goal by the tax of the coin
           h += taxes[coin]
   return h


print(a_star())
