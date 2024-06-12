
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total value of the coins that adds up to 214
   goal_value = 214
   # Define the tax values for each coin
   tax_values = {15: 6, 5: 5, 17: 1, 14: 4, 2: 2, 8: 2, 10: 9, 59: 9, 16: 8, 4: 3, 18: 10, 20: 11, 21: 8, 6: 6, 9: 9, 3: 3}
   # Define the list of coins
   coins = [4, 17, 8, 15, 6, 14, 2, 4, 16, 10, 6, 5, 14, 8, 18, 2, 17, 9, 17, 59, 3, 10, 21, 4, 9, 14, 14, 20, 14, 8, 14, 18, 5, 16, 14, 17, 5, 3]
   # Define the set of unique coins
   unique_coins = set(coins)
   # Define the dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in the list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, chosen_coins, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the total value of the chosen coins is equal to the goal value
       if sum(state[0]) == goal_value:
           return chosen_coins


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in unique_coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the total value of the chosen coins does not exceed the goal value
           if coin not in state[0] and sum(state[0]) + coin <= goal_value:
               # Generate the new state
               new_state = (state[0].copy(), state[1])
               new_state[0].add(coin)
               # Calculate the additional tax paid for the new coin
               new_tax = tax_values[coin]
               # The total tax paid in the new state is the total tax paid in the current state plus the additional tax paid for the new coin
               new_state[1] += new_tax
               # The cost so far is the total tax paid in the new state, as the task is to minimize the total tax paid
               new_cost = g + new_tax


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_value), new_cost, chosen_coins + [coin], new_state))
   return None


def heuristic(state, goal_value):
   # An admissible and consistent heuristic for this problem is the difference between the goal value and the total value of the chosen coins
   # This heuristic relaxes the constraint that the coins must be unique and can only be used once
   # It is admissible because it never overestimates the cost to reach the goal, as the cost of reaching the goal state is always less than or equal to the cost of reaching any other state
   # It's consistent because moving a coin from one state to another reduces the heuristic cost of the successor node by a max of the value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the value of the moved coin) + h(n)
   return goal_value - sum(state[0])


print(a_star())
