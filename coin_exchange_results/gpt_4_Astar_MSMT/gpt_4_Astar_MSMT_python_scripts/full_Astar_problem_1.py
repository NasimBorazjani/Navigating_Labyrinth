
import heapq

def initialize():
   # Define the initial state of the problem, which includes the coins available, the sum of the coins chosen so far, the tax paid so far, and the value of the last coin chosen
   initial_state = ((14, 2, 5, 8, 65, 5, 16, 2, 5, 2, 12, 17, 16, 15, 20, 4, 19, 9, 10, 64, 2, 10, 14, 2, 17), 0, 0, 0)
   goal_sum = 208
   tax_values = {20: 13, 4: 2, 17: 16, 19: 8, 64: 4, 5: 3, 14: 10, 10: 9, 65: 11, 16: 2, 12: 7, 8: 5, 2: 2, 15: 14, 9: 8}

   visited_costs = {}
   visited_costs[initial_state] = 0

   queue = [(0, 0, [], initial_state)]
  
   return initial_state, goal_sum, tax_values, visited_costs, queue
  
def a_star():
  
   initial_state, goal_sum, tax_values, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # Unpack the information encoded in each state
       coins, sum_coins, tax_paid, last_coin = state

       # If the sum of the coins chosen so far equals the goal sum, return the coins chosen
       if sum_coins == goal_sum:
           return actions

       # If the sum of the coins chosen so far is less than the goal sum, generate all possible actions from the current state, which includes choosing any of the remaining coins
       elif sum_coins < goal_sum:
           for coin in coins:
               # Check if the new state, containing the new coin, would be valid; ie the coin must be even if it is smaller than the last coin chosen, and odd if it is larger than or equal to the last coin chosen
               if (coin < last_coin and coin % 2 == 0) or (coin >= last_coin and coin % 2 == 1):
                   # Generate the new state
                   new_state = (tuple(c for c in coins if c != coin), sum_coins + coin, tax_paid + tax_values[coin], coin)
                   # The additional cost of this state is the tax paid for the new coin as we are trying to minimize the total tax paid
                   new_cost = g + tax_values[coin]

                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The new coin must be added to the actions
                       heapq.heappush(queue, (g + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_sum):
   # An admissible and consistent heuristic for this problem is the difference between the goal sum and the sum of the coins chosen so far
   # The heuristic assumes we can reach the goal sum without paying any additional tax, thus reporting a lower cost estimate to reach the goal state, making it admissible
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of choosing a coin is the tax paid for that coin, which is always greater than or equal to 0, the decrease in the difference between the goal sum and the sum of the coins chosen so far
   # Also the cost of the goal state is 0, as the sum of the coins chosen equals the goal sum and there are no more coins to choose

   return goal_sum - state[1]


print(a_star())
