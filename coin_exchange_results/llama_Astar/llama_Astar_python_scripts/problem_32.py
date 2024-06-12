
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the coins to be chosen, and the total tax paid
   goal_state = (None, 264)
   # Define the set of all coins and their tax values
   coins = [19, 2, 25, 9, 6, 24, 4, 26, 17, 11, 11, 2, 17, 2, 5, 6, 3, 3, 3, 18, 26, 18, 21, 3, 5, 8, 12, 15, 8, 18, 24, 5, 19, 7, 18, 25, 12, 13, 12, 2, 25, 16, 17, 16, 3, 3]
   taxes = {26: 12, 25: 20, 17: 13, 13: 4, 16: 13, 11: 10, 24: 5, 5: 4, 8: 6, 7: 5, 4: 4, 12: 9, 18: 12, 3: 2, 21: 17, 19: 7, 2: 2, 9: 9, 6: 2, 15: 4}
   # Define the dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Define the priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in the list; no coins chosen initially
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
   # An admissible and consistent heuristic for this problem is the difference between the total sum of the chosen coins and the goal sum
   # This heuristic relaxes the constraint that the coins must be unique and can only be used once
   # It is admissible because it never overestimates the cost to reach the goal, as each coin that is not chosen must be added at least once
   # It's consistent because moving a coin from the chosen set to the unchosen set reduces the heuristic cost of the successor node by a max of the value of the coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the value of the coin) + h(n)
   h = goal[1] - sum(state[0])
   return h


print(a_star())
