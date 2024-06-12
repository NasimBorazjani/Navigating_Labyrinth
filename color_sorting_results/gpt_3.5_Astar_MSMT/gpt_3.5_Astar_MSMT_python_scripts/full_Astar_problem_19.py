
import heapq

def initialize():
   # Define the initial state of the tubes, represented as a list of lists
   initial_state = [['Blue', 'Green', 'Green', 'Red'], ['Red', 'Blue', 'Green', 'Red'], ['Blue', 'Red', 'Green', 'Blue']]
   num_tubes = 3
   tube_capacity = 6

   visited_costs = {}
   visited_costs[str(initial_state)] = 0

   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))
  
   return initial_state, num_tubes, tube_capacity, visited_costs, queue
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial and goal state of the tubes)
   initial_state, num_tubes, tube_capacity, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heappop(queue)

       # Check if the tubes are sorted by color, with each tube containing balls of only one color
       if all(all(ball == state[0][0] for ball in tube) for tube in state):
           return actions

       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for i in range(num_tubes):
           for j in range(num_tubes):
               if i != j and len(state[i]) > 0 and len(state[j]) < tube_capacity:
                   # Generate the new state by moving the top ball from tube i to tube j
                   new_state = [list(tube) for tube in state]
                   new_state[j].append(new_state[i].pop(0))
                   new_state = [tuple(tube) for tube in new_state]
                   # The cost of moving a ball is 1, as we aim to minimize the number of moves required to sort the tubes
                   new_cost = g + 1
                  
                   if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                       visited_costs[str(new_state)] = new_cost
                       # Calculate the heuristic estimate for the new state
                       h = heuristic(new_state)
                       heappush(queue, (g + h, new_cost, actions + [(i, j)], new_state))
                  
   return None

def heuristic(state):
   # An admissible and consistent heuristic is the number of balls that are not in their correct position
   # The heuristic relaxes the constraint that only one ball can be moved at a time and presumes we can move multiple balls to their correct position in one step
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost of the next node is higher if more balls are moved to their correct position, and the heuristic estimate for the goal state is 0, as all balls would be in their correct position
   h = 0
   for tube in state:
       for i, ball in enumerate(tube):
           if ball != tube[0]:
               h += 1
   return h

print(a_star())
