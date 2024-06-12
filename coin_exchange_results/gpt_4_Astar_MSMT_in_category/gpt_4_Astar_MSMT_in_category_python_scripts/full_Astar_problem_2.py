
import heapq


def initialize():
   # Define the initial state and the goal state of the problem, represented as tuples
   initial_state = (0, 0, 0)
   goal_state = 203
   # Encoding other variables given in the problem statement
   coins = [13, 10, 12, 10, 16, 7, 9, 14, 13, 18, 36, 11, 7, 14, 7, 8, 19, 7, 39, 13, 3, 18, 20, 4, 3, 18, 15, 2, 19, 16]
   taxes = {15: 5, 36: 15, 39: 9, 9: 8, 13: 3, 2: 2, 18: 10, 12: 12, 3: 3, 8: 8, 11: 6, 10: 4, 4: 4, 14: 10, 7: 3, 16: 16, 20: 18, 19: 17}


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, goal_state, coins, taxes, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial and goal state, coins, and taxes)
   initial_state, goal_state, coins, taxes, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if state[0] == goal_state:
           return actions


       # Generate all valid actions from the current state, which includes choosing any of the remaining coins
       for coin in coins:
           # Check if the coin is valid, ie if the coin is smaller than the previous one, it must have an even value, otherwise, if the coin is larger than or equal to the previous coin chosen, it must have an odd value
           if (coin < state[1] and coin % 2 == 0) or (coin >= state[1] and coin % 2 == 1):
               # The action is valid, generate the new state
               new_state = (state[0] + coin, coin, state[2] + taxes[coin])
               # The cost so far is the total tax paid, as our objective is to minimize the total tax paid
               new_cost = g + taxes[coin]
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [coin], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the difference between the goal sum and the current sum of the coins
   # The heuristic relaxes the constraints that the coins must be unique, that the coins carry a tax value, and that the coins must be smaller or larger than the previous one based on their parity; ie It presumes we can choose any coin to reach the goal sum
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of choosing a coin is the tax of the coin, which is always greater than or equal to 1, the decrease in the difference between the goal sum and the current sum, if the coin is chosen toward the goal sum, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the difference between the goal sum and the current sum would be 0 in the goal state.
   return goal - state[0]


print(a_star())
