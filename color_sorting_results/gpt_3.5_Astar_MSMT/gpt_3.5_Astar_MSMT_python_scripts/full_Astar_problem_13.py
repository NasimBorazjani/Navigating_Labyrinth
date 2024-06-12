
import heapq

def initialize():
   # Define the initial state of the tubes, represented as a list of lists
   initial_state = [['Green', 'Blue', 'Blue', 'Green'],
                    ['Red', 'Green', 'Red', 'Blue'],
                    ['Red', 'Green', 'Blue', 'Red']]
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
       if all(all(ball == state[0][0] for ball in tube) for tube in state):
           return actions

       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for i in range(num_tubes):
           for j in range(num_tubes):
               if i != j:
                   # Check if moving a ball from tube i to tube j is valid
                   if state[i] and len(state[j]) < tube_capacity and (not state[j] or state[j][0] == state[i][0]):
                       new_state = [list(tube) for tube in state]
                       ball = new_state[i].pop(0)
                       new_state[j].insert(0, ball)
                       new_state = [tuple(tube) for tube in new_state]
                       new_state_str = str(new_state)
                       new_cost = g + 1
                      
                       if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                           visited_costs[new_state_str] = new_cost
                           heapq.heappush(queue, (g + 1, new_cost, actions + [(i, j)], new_state))
                  
   return None

print(a_star())
