
import heapq

def initialize():
   # Define the initial state of the tubes, represented as a list of lists
   initial_state = [['Blue', 'Red', 'Red', 'Blue'], ['Green', 'Green', 'Red', 'Red'], ['Green', 'Green', 'Blue', 'Blue']]
   num_tubes = 3
   tube_capacity = 6
   goal_state = [['Blue', 'Blue', 'Blue', 'Blue'], ['Red', 'Red', 'Red', 'Red'], ['Green', 'Green', 'Green', 'Green']]

   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0

   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))
  
   return initial_state, num_tubes, tube_capacity, goal_state, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, tube_capacity, goal_state, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heappop(queue)

       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions

       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for i in range(num_tubes):
           for j in range(num_tubes):
               if i != j:
                   # Find the topmost ball in tube i
                   ball_to_move = state[i][-1]
                   # Check if tube j has space to accommodate the ball
                   if len(state[j]) < tube_capacity:
                       # Generate the new state after moving the ball
                       new_state = [list(row) for row in state]
                       new_state[j].append(ball_to_move)
                       new_state[i].pop()
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost of moving a ball is 1
                       new_cost = g + 1
                      
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # Calculate the heuristic for the new state
                           h = heuristic(new_state, goal_state)
                           heappush(queue, (g + h, new_cost, actions + [(i, j)], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the number of balls that are not in the correct position
   # The heuristic relaxes the constraint that only one ball can be moved at a time and presumes we can move multiple balls to their correct positions in one step
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost of the next node is higher if more balls are moved to their correct positions, and the heuristic estimate for the goal state is 0, as all balls would be in their correct positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != goal[i][j]:
               h += 1
   return h


print(a_star())
