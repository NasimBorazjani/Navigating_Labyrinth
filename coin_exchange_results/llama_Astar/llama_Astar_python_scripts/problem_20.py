
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the coins to be chosen, and the total tax paid
   goal_state = (None, 246)
   # Define the set of all coins and their tax values
   coins = [12, 15, 3, 24, 10, 18, 10, 20, 21, 17, 9, 8, 2, 11, 5, 5, 3, 8, 6, 12, 20, 22, 4, 5, 17, 5, 14, 10, 15, 8, 9, 22, 4, 7, 15, 16, 4, 2, 5, 9, 24, 23, 3, 7, 20, 9, 12, 10, 4, 4, 8, 24, 11, 20, 2, 15]
   taxes = {20: 14, 15: 15, 6: 1, 14: 1, 7: 2, 18: 5, 2: 1, 16: 5, 21: 9, 3: 3, 12: 3, 17: 10, 22: 4, 10: 9, 4: 3, 11: 1, 5: 1, 23: 13, 24: 4, 9: 9, 8: 4}
   # Define the dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
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
   # An admissible and consistent heuristic for this problem is the difference between the total sum of the coins chosen in the current state and the goal sum
   # This heuristic relaxes the constraint that the coins must be chosen in increasing order, as the heuristic estimate for the goal state is 0, as the total sum of the coins chosen would be the goal sum
   return goal[1] - state[1]


print(a_star())
