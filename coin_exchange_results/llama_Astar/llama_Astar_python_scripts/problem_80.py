
import heapq


def a_star():
   # Define the initial state of the problem, as the empty set of chosen coins and the total tax paid so far
   initial_state = (set(), 0)
   # Define the goal state, as the total sum of the coins to be chosen, and the total tax paid
   goal_state = (None, 397)
   # Define the list of coins and their tax values
   coins = [8, 7, 5, 24, 3, 18, 36, 39, 36, 25, 25, 33, 16, 20, 34, 9, 1, 22, 25, 13, 8, 37, 35, 39, 11, 26, 36, 25, 25, 27, 2, 4, 35, 2, 16, 22, 12, 15, 19, 2, 17, 25, 28, 12, 26, 17, 33, 5, 30, 3, 21, 3]
   taxes = {13: 7, 39: 4, 20: 18, 5: 1, 12: 7, 9: 5, 28: 20, 24: 11, 3: 3, 17: 3, 21: 9, 37: 6, 16: 8, 15: 1, 26: 10, 36: 6, 22: 9, 2: 2, 8: 1, 25: 20, 4: 3, 7: 5, 19: 7, 30: 6, 27: 12, 1: 1, 34: 7, 35: 5, 11: 6, 18: 12, 33: 4}
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
   # This heuristic relaxes the constraint that the coin chosen must be smaller than the previous one, or larger than or equal to the previous one, and has an even or odd value, respectively
   # It is admissible because it never overestimates the cost to reach the goal, as the cost of choosing a coin is always equal to or less than the cost of reaching the successor node
   # It's consistent because moving a coin from one state to another reduces the heuristic cost of the successor node by a max of the value of the moved coin, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the value of the moved coin) + h(n)
   return goal[1] - state[1]


print(a_star())
