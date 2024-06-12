
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total value of the coins that adds up to 215
   goal_value = 215
   # Define the tax values for each coin
   tax_values = {14: 2, 18: 9, 11: 10, 9: 6, 10: 9, 13: 10, 37: 9, 6: 5, 2: 2, 4: 1, 8: 3, 19: 10, 17: 7, 7: 6, 3: 3, 21: 3, 20: 4}
   # Define the list of coins
   coins = [13, 19, 9, 4, 18, 17, 2, 14, 17, 17, 8, 6, 4, 10, 19, 37, 20, 19, 14, 7, 6, 11, 21, 9, 3, 10, 21, 20, 2, 17, 2]
   # Define the dictionary of coin values and their tax values
   coins_dict = {coin: tax for coin, tax in zip(coins, tax_values[coin] for coin in coins)}
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in the list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie the total value of the chosen coins is equal to the goal value
       if sum(state[0]) == goal_value:
           return actions


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the total value of the chosen coins does not exceed the goal value
           if coin not in state[0] and sum(state[0]) + coin <= goal_value:
               # Generate the new state
               new_state = (state[0].copy(), state[1])
               new_state[0].add(coin)
               # The tax paid for the new state is the tax paid in the current state plus the tax of the chosen coin
               new_state[1] += coins_dict[coin]
               # The cost so far is the tax paid in the new state, as the task is to minimize the tax paid
               new_cost = new_state[1]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_value), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal_value):
   # An admissible and consistent heuristic for this problem is the difference between the goal value and the total value of the chosen coins
   # This heuristic relaxes the constraint that the coins must be chosen in increasing order, as it does not consider the order of the chosen coins
   # It is admissible because it never overestimates the cost to reach the goal, as the heuristic cost of the successor node is always less than or equal to the cost of reaching the goal state
   # It's consistent because moving a coin from the unchosen set to the chosen set reduces the heuristic cost of the successor node by a max of the value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the value of the moved coin) + h(n)
   return goal_value - sum(state[0])


print(a_star())
