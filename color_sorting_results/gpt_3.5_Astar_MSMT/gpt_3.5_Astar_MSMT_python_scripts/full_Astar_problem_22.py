
import heapq

def initialize():
   # Define the initial state of the tubes, represented as a list of lists
   initial_state = [['Blue', 'Red', 'Blue', 'Green'], ['Red', 'Blue', 'Green', 'Red'], ['Blue', 'Green', 'Green', 'Red']]
   num_tubes = 3
   tube_capacity = 6

   visited_costs = {}
   visited_costs[str(initial_state)] = 0

   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))
  
   return initial_state, num_tubes, tube_capacity, visited_costs, queue
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial and goal state of the tubes, the number of tubes, and the capacity of the tubes)
   initial_state, num_tubes, tube_capacity, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heappop(queue)

       # If all tubes are sorted, return the actions taken
       if all(all(state[i][j] == state[i][0] for j in range(len(state[i]))) for i in range(num_tubes)):
           return actions

       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for i in range(num_tubes):
           for j in range(num_tubes):
               if i != j and len(state[i]) > 0 and len(state[j]) < tube_capacity:
                   # Create a new state by moving a ball from tube i to tube j
                   new_state = [list(tube) for tube in state]
                   new_state[j].append(new_state[i].pop())
                   new_state = [tube for tube in new_state if tube]
                   # The cost of moving a ball is 1
                   new_cost = g + 1
                  
                   if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                       visited_costs[str(new_state)] = new_cost
                       # Calculate the heuristic value for the new state
                       h = heuristic(new_state, num_tubes)
                       heappush(queue, (g + h, new_cost, actions + [(i, j)], new_state))
                  
   return None

def heuristic(state, num_tubes):
   # An admissible and consistent heuristic is the number of misplaced balls in each tube
   # The heuristic relaxes the constraint that only one ball can be moved at a time and presumes we can move multiple balls to their correct position in one action
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost of the next node is higher if more balls are misplaced in the next state, and the heuristic estimate for the goal state is 0, as all balls are in their correct position
   h = 0
   for i in range(num_tubes):
       for j in range(len(state[i])):
           if state[i][j] != state[i][0]:
               h += 1
   return h

print(a_star())
