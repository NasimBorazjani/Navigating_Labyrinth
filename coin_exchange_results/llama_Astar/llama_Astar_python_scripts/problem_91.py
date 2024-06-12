
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the chosen coins equaling 445
   goal_sum = 445
   # Define the tax values for each coin
   tax_values = {36: 14, 27: 19, 21: 6, 13: 8, 23: 17, 26: 17, 15: 6, 25: 7, 31: 20, 30: 5, 18: 14, 12: 6, 37: 2, 221: 18, 14: 13, 24: 10, 33: 4, 43: 11, 29: 18, 40: 1, 7: 6, 17: 2}
   # Define the list of coins
   coins = [36, 40, 17, 7, 15, 23, 18, 26, 29, 24, 15, 43, 13, 12, 31, 33, 30, 31, 26, 37, 14, 31, 43, 25, 30, 7, 37, 27, 221, 13, 26, 21]
   # Define the previous chosen coin
   prev_coin = None


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if sum(state[0]) == goal_sum:
           return actions


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the total tax paid does not exceed the goal tax
           if coin not in state[0] and state[1] + tax_values[coin] <= goal_sum:
               # Check the tax constraint
               if prev_coin is not None and coin < prev_coin and tax_values[coin] % 2 != 0:
                   continue
               if prev_coin is not None and coin >= prev_coin and tax_values[coin] % 2 == 0:
                   continue
               # Generate the new state
               new_state = (state[0].copy(), state[1] + tax_values[coin])
               new_state[0].add(coin)
               # The cost so far is the total tax paid so far
               new_cost = g + tax_values[coin]
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, actions + [coin], new_state))
                   prev_coin = coin
   return None


def heuristic(state, goal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the values of the remaining coins to be chosen, minus the goal sum
   # This heuristic relaxes the constraint that the tax for coins of the same value is the same
   # It is admissible because it never overestimates the cost to reach the goal, as each remaining coin must be chosen at least once
   # It's consistent because moving a coin from the remaining set to the chosen set reduces the heuristic cost of the successor node by a max of the value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the value of the moved coin) + h(n)
   remaining_coins = set(coins) - state[0]
   return sum(remaining_coins) - goal_sum


print(a_star())
