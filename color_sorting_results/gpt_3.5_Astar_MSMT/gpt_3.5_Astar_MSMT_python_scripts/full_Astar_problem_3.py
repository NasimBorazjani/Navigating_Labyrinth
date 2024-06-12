
import heapq

def initialize():
   # Define the initial state of the tubes, represented as a list of lists
   initial_state = [['Red', 'Blue', 'Blue', 'Red'], ['Red', 'Blue', 'Blue', 'Green'], ['Green', 'Green', 'Red', 'Green']]
   num_tubes = 3
   tube_capacity = 6
   goal_state = [['Red', 'Red', 'Red', 'Red'], ['Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green', 'Green']]

   visited_costs = {}
   visited_costs[str(initial_state)] = 0

   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_tubes, tube_capacity, goal_state, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, tube_capacity, goal_state, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions

       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for i in range(num_tubes):
           for j in range(num_tubes):
               if i != j:
                   # Check if the move is valid, ie the tube from which the ball is taken is not empty and the tube to which the ball is moved is not at capacity
                   if state[i] and len(state[j]) < tube_capacity:
                       # Generate the new state after the move
                       new_state = [list(tube) for tube in state]
                       ball = new_state[i].pop(0)
                       new_state[j].insert(0, ball)
                       new_state = [tuple(tube) for tube in new_state]
                       # The cost of the new state is the number of moves made, as we aim to minimize the number of moves required to sort the balls
                       new_cost = g + 1

                       if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                           visited_costs[str(new_state)] = new_cost
                           heapq.heappush(queue, (g + 1, new_cost, actions + [(i, j)], new_state))
                  
   return None

print(a_star())
