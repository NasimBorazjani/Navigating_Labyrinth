
import heapq

def initialize():
   # Define the initial state of the tubes, represented as a list of lists
   initial_state = [['Red', 'Red', 'Blue', 'Blue'], ['Red', 'Blue', 'Red', 'Green'], ['Green', 'Blue', 'Green', 'Green']]
   num_tubes = 3

   visited_costs = {}
   visited_costs[str(initial_state)] = 0

   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # Check if the tubes are sorted, meaning each tube contains balls of only one color
       if all(len(set(tube)) == 1 for tube in state):
           return actions

       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for i in range(num_tubes):
           for j in range(num_tubes):
               if i != j and len(state[j]) < 6 and state[i]:
                   # Create a new state by moving the top ball from tube i to tube j
                   new_state = [list(tube) for tube in state]
                   new_state[j].append(new_state[i].pop())
                   new_state = [tuple(tube) for tube in new_state]
                   new_state_key = str(new_state)
                   # The cost of this state is the number of moves made so far
                   new_cost = g + 1
                  
                   if new_state_key not in visited_costs or new_cost < visited_costs[new_state_key]:
                       visited_costs[new_state_key] = new_cost
                       # Calculate the heuristic estimate for this state
                       h = heuristic(new_state)
                       heapq.heappush(queue, (g + h, new_cost, actions + [(i, j)], new_state))
   return None


def heuristic(state):
   # The heuristic is the sum of the number of balls in each tube that are not in the correct order
   # This heuristic is admissible because it underestimates the cost to reach the goal state, as it only counts the number of balls out of order and does not consider the cost of moving them to the correct position
   # The heuristic is consistent because the cost of moving a ball to the correct position is at least 1, which is the decrease in the heuristic value, and the heuristic value for the goal state is 0
   h = 0
   for tube in state:
       for i in range(len(tube) - 1):
           if tube[i] != tube[i + 1]:
               h += 1
   return h


print(a_star())
