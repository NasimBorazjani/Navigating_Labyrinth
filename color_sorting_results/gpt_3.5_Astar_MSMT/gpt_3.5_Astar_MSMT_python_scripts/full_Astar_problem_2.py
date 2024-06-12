
import heapq

def initialize():
   # Define the initial state of the tubes as a list of lists
   initial_state = [['Red', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Red', 'Green'], ['Green', 'Blue', 'Red', 'Red']]
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
               # Check if moving a ball from tube i to tube j is valid
               if i != j and state[i] and len(state[j]) < tube_capacity:
                   new_state = [list(tube) for tube in state]
                   new_state[j].append(new_state[i].pop())
                   new_state = [tuple(tube) for tube in new_state]
                   # The cost of each action is 1, as we aim to minimize the number of moves required to sort the balls
                   new_cost = g + 1
                  
                   if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                       visited_costs[str(new_state)] = new_cost
                       # Calculate the heuristic estimate for the cost to reach the goal state
                       h = heuristic(new_state, goal_state)
                       heapq.heappush(queue, (g + h, new_cost, actions + [(i, j)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the sum of the number of balls in each tube that are not in their correct position
   # The heuristic relaxes the constraint that only one ball can be moved at a time and presumes we can move multiple balls to their correct positions in one move
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost of the next node is higher if more balls are moved to their correct positions, and the heuristic estimate for the goal state is 0, as all balls are in their correct positions
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != goal[i][j]:
               h += 1
   return h


print(a_star())
