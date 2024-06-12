
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the coins to be chosen, and the total tax paid
   goal_state = (None, 419)
   # Define the set of all coins and their tax values
   coins = [5, 15, 15, 77, 12, 38, 41, 30, 31, 30, 13, 19, 9, 2, 23, 37, 14, 34, 29, 22, 22, 4, 16, 2, 12, 17, 9, 18, 19, 21, 4, 28, 40, 11, 30, 24, 19, 9, 10, 76, 34]
   taxes = {13: 8, 29: 10, 4: 4, 2: 2, 77: 17, 16: 10, 11: 2, 22: 18, 17: 10, 18: 18, 38: 7, 9: 6, 5: 2, 41: 14, 31: 3, 12: 10, 19: 5, 24: 16, 40: 6, 14: 4, 34: 13, 15: 3, 23: 20, 76: 16, 37: 2, 21: 2, 28: 3, 10: 2, 30: 16}
   # Define the dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in a list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[1] == goal_state[1]:
           return actions


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
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [coin], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the difference between the total sum of the coins chosen in the current state and the goal sum
   # This heuristic relaxes the constraint that the coins must be chosen in order, and presumes we can choose any coin at any time
   # It is admissible because it never overestimates the cost to reach the goal, as each unchosen coin must be chosen at least once
   # It's consistent because moving a coin from the unchosen to the chosen set reduces the heuristic cost of the successor node by a max of the value of the coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the value of the coin) + h(n)
   h = goal[1] - state[1]
   return h


print(a_star())
