
import heapq


def initialize():
   # Define the initial state and the goal state of the problem
   initial_state = (0, 0, 0, 0)
   goal_state = 208
   # Define the coins and their tax values
   coins = [14, 2, 5, 8, 65, 5, 16, 2, 5, 2, 12, 17, 16, 15, 20, 4, 19, 9, 10, 64, 2, 10, 14, 2, 17]
   tax = {20: 13, 4: 2, 17: 16, 19: 8, 64: 4, 5: 3, 14: 10, 10: 9, 65: 11, 16: 2, 12: 7, 8: 5, 2: 2, 15: 14, 9: 8}
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, goal_state, coins, tax, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem
   initial_state, goal_state, coins, tax, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if state[0] == goal_state:
           return actions


       # Generate all valid actions from the current state, which includes choosing any of the remaining coins
       for coin in coins:
           # Check if the coin is valid, ie if the coin is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
           if (coin < state[1] and coin % 2 == 0) or (coin >= state[1] and coin % 2 == 1):
               # The actions is valid, generate the new state
               new_state = (state[0] + coin, coin, state[2] + tax[coin], state[3] + 1)
               # The cost so far is the total tax paid, as our objective is to minimize the total tax paid to reach the goal state 
               new_cost = g + tax[coin]
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [coin], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the remaining amount to reach the goal state divided by the maximum coin value
   # The heuristic relaxes the constraint that a coin can only be used once and presumes we can reach the goal state by using the maximum coin value
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of choosing a coin is the tax of the coin, which is always greater than or equal to 1, the decrease in the remaining amount to reach the goal state, if the coin is chosen toward the goal state, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the remaining amount to reach the goal state would be 0 in the goal state.
   return (goal - state[0]) / max(coins)


print(a_star())
