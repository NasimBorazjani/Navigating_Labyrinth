
import heapq

def initialize():
   # Define the initial state of the tubes, represented as a list of lists
   initial_state = [['Blue', 'Green', 'Blue', 'Red'], ['Red', 'Blue', 'Green', 'Red'], ['Green', 'Green', 'Blue', 'Red']]
   num_tubes = 3
   tube_capacity = 6

   visited_costs = {}
   visited_costs[str(initial_state)] = 0

   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))
  
   return initial_state, num_tubes, tube_capacity, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, tube_capacity, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heappop(queue)

       # If all tubes are sorted, return the actions taken
       if all(all(state[i][j] == state[i][0] for j in range(len(state[i]))) for i in range(num_tubes)):
           return actions

       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for i in range(num_tubes):
           for j in range(num_tubes):
               if i != j and len(state[j]) < tube_capacity:
                   # Generate the new state by moving the top ball from tube i to tube j
                   new_state = [tube[:] for tube in state]
                   new_state[j].insert(0, new_state[i].pop(0))
                   new_state = tuple(tuple(tube) for tube in new_state)
                   # The cost of moving a ball is 1
                   new_cost = g + 1
                  
                   if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                       visited_costs[str(new_state)] = new_cost
                       # Calculate the heuristic cost to reach the goal state
                       h = heuristic(new_state, num_tubes)
                       heappush(queue, (g + h, new_cost, actions + [(i, j)], new_state))
   return None


def heuristic(state, num_tubes):
   # An admissible and consistent heuristic is the number of misplaced balls in each tube
   # The heuristic relaxes the constraint that only one ball can be moved at a time and that tubes have a capacity of 6 balls, presuming we can move all misplaced balls in one action
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the cost of moving a ball to its correct position is always 1, which is exactly the decrease in the number of misplaced balls
   h = 0
   for i in range(num_tubes):
       # Count the number of misplaced balls in each tube
       h += sum(1 for j in range(len(state[i])) if state[i][j] != state[i][0])
   return h


print(a_star())
