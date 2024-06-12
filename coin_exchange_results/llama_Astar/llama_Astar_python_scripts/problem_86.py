
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = ([], 0)
   # Define the goal state, as a subset of coins with a sum of 490
   goal_state = ([], 490)
   # Define the set of coins and their tax values
   coins = [31, 8, 22, 27, 2, 25, 2, 8, 49, 26, 65, 6, 37, 49, 15, 21, 27, 5, 34, 28, 47, 15, 7, 42, 32, 20, 34, 48, 39, 7, 13]
   taxes = {7: 1, 65: 16, 21: 18, 25: 18, 15: 14, 31: 15, 6: 2, 37: 2, 5: 1, 22: 1, 8: 7, 26: 2, 2: 1, 32: 8, 27: 2, 13: 8, 39: 17, 28: 11, 47: 6, 42: 10, 34: 15, 20: 8, 48: 11, 49: 13}
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coins chosen in the list; no coins chosen initially
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, chosen_coins, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[1] == 490:
           return chosen_coins


       # Generate all possible actions from the current state, which includes choosing a coin from the list
       for coin in coins:
           # Check if the new state would be valid, ie the sum of the chosen coins so far plus the value of the new coin is not greater than 490
           if state[1] + coin <= 490:
               # Generate the new state
               new_state = ([coin] + state[0], state[1] + coin + taxes[coin])
               # The cost so far is the total tax paid so far, as the task is to minimize the total tax paid
               new_cost = g + taxes[coin]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, chosen_coins + [coin], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the difference between the total value of the chosen coins in the current state and the goal state
   # This heuristic relaxes the constraint that the sum of the chosen coins must be 490
   # It is admissible because it never overestimates the cost to reach the goal, as the cost of moving from the current state to the goal state is always a non-negative number
   # It's consistent because moving a coin from the current state to the goal state reduces the heuristic cost of the successor node by a non-negative number, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the tax of the moved coin) + h(n)
   return abs(goal[1] - state[1])


print(a_star())
