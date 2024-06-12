
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the coins to be chosen, and the total tax paid
   goal_state = (None, 284)
   # Define the set of all coins and their tax values
   coins = [28, 5, 25, 22, 26, 13, 20, 20, 18, 28, 7, 20, 18, 19, 18, 5, 15, 23, 28, 27, 22, 10, 8, 17, 3, 8, 5, 11, 21, 17, 65, 23, 11, 3, 12]
   taxes = {20: 12, 21: 3, 5: 2, 3: 2, 7: 1, 15: 8, 8: 7, 27: 6, 17: 8, 18: 14, 28: 5, 13: 1, 23: 4, 65: 8, 26: 8, 22: 5, 25: 3, 11: 11, 12: 8, 19: 19, 10: 7}
   # Define the dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in a list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, chosen_coins, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[1] == goal_state[1]:
           return chosen_coins


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the coin is not already chosen and the total tax paid does not exceed the goal tax
           if coin not in state[0] and g + taxes[coin] <= goal_state[1]:
               # Generate the new state
               new_state = (state[0] | {coin}, g + taxes[coin])
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, chosen_coins + [coin], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the difference between the total sum of the chosen coins and the goal sum
   # This heuristic relaxes the constraint that the coins must be unique and can only be used once
   # It is admissible because it never overestimates the cost to reach the goal, as each unchosen coin must be chosen at least once
   # It's consistent because moving a coin from the chosen set to the unchosen set reduces the heuristic cost of the successor node by a max of the value of the coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the value of the coin) + h(n)
   return goal[1] - state[1]


print(a_star())
