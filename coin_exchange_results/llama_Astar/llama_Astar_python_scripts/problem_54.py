
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the coins to be chosen, and the total tax paid so far
   goal_state = (None, 328)
   # Define the set of all coins and their tax values
   coins = [4, 17, 14, 12, 1, 3, 12, 10, 14, 9, 30, 20, 11, 17, 11, 16, 22, 17, 30, 5, 10, 16, 19, 27, 6, 18, 20, 19, 32, 25, 30, 15, 30, 21, 19, 25, 31, 33, 19, 10, 8, 16, 8]
   taxes = {1: 1, 31: 13, 25: 13, 11: 3, 3: 1, 10: 8, 33: 14, 8: 4, 9: 9, 4: 1, 20: 4, 12: 8, 27: 13, 30: 14, 16: 10, 18: 9, 32: 5, 21: 20, 6: 4, 5: 5, 22: 11, 17: 11, 19: 2, 14: 10, 15: 6}
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
   # An admissible and consistent heuristic for this problem is the difference between the total sum of the chosen coins and the goal sum
   # This heuristic relaxes the constraint that the coins must be chosen in order, and presumes we can choose any coin at any time
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of choosing a coin is always equal to its value plus its tax, which is a non-decreasing function of the number of coins chosen
   # Thus h(s) is always less than or equal to c(s, n)(equal to the value of the chosen coin plus its tax) + h(n)
   return goal[1] - state[1]


print(a_star())
