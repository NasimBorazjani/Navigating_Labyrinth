
import heapq

def initialize():
   # Define the initial state of the tubes
   initial_state = [['Green', 'Red', 'Blue', 'Green'],
                    ['Red', 'Blue', 'Red', 'Blue'],
                    ['Red', 'Blue', 'Green', 'Green']]
   num_tubes = 3
   tube_capacity = 6

   visited_costs = {}
   visited_costs[str(initial_state)] = 0

   queue = []
   # No actions taken in the initial state
   heapq.heappush(queue, (0, 0, [], initial_state))
  
   return initial_state, num_tubes, tube_capacity, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, tube_capacity, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # If all tubes are sorted, return the actions taken
       if all(all(ball == state[0][0] for ball in tube) for tube in state):
           return actions

       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for i in range(num_tubes):
           for j in range(num_tubes):
               if i != j:
                   # Check if moving a ball from tube i to tube j is valid
                   if state[i] and len(state[j]) < tube_capacity and (not state[j] or state[i][0] == state[j][0]):
                       new_state = [list(tube) for tube in state]
                       new_state[j].insert(0, new_state[i].pop(0))
                       new_state = tuple([tuple(tube) for tube in new_state])
                       # The cost of each state is the number of moves made, as we aim to minimize the number of moves required to sort the balls
                       new_cost = g + 1
                      
                       if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                           visited_costs[str(new_state)] = new_cost
                           heapq.heappush(queue, (g + heuristic(new_state), new_cost, actions + [(i, j)], new_state))
                  
   return None


def heuristic(state):
   # An admissible and consistent heuristic is the number of balls that are not yet sorted in each tube
   # The heuristic relaxes the constraint that only one ball can be moved at a time, presuming we can move multiple balls at once to sort them, thus reporting a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the cost of moving a ball from one tube to another is 1, which is exactly the decrease in the number of balls that are not yet sorted
   h = 0
   for tube in state:
       for i in range(1, len(tube)):
           if tube[i] != tube[0]:
               h += 1
   return h


print(a_star())
