
import heapq

def initialize():
   # Define the initial state of the tubes, represented as a list of lists
   initial_state = [['Red', 'Blue', 'Green', 'Blue'], ['Red', 'Red', 'Red', 'Green'], ['Blue', 'Green', 'Blue', 'Green']]
   num_tubes = 3
   tube_capacity = 6
   goal_state = [['Red', 'Red', 'Red', 'Red'], ['Green', 'Green', 'Green', 'Green'], ['Blue', 'Blue', 'Blue', 'Blue']]
  
   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = 0

   queue = []
   # No actions taken in the initial state
   heapq.heappush(queue, (0, 0, [], initial_state))
  
   return initial_state, num_tubes, tube_capacity, goal_state, visited_costs, queue
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial and goal state of the tubes, the number of tubes, and the capacity of the tubes)
   initial_state, num_tubes, tube_capacity, goal_state, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # Check if the current state is the goal state by comparing the state with the predefined goal state
       if state == goal_state:
           return actions

       # Generate all valid actions from the current state, which includes moving a ball from one tube to another
       for from_tube in range(num_tubes):
           for to_tube in range(num_tubes):
               # Check if the move is valid, ie if the from_tube is not empty and the to_tube is not at capacity
               if state[from_tube] and len(state[to_tube]) < tube_capacity:
                   new_state = [list(row[:]) for row in state]
                   # Move the ball from the top of the from_tube to the top of the to_tube
                   new_state[to_tube].append(new_state[from_tube].pop())
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of moves made, as the objective is to minimize the number of moves required to sort the balls
                   new_cost = g + 1
                  
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [(from_tube, to_tube)], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the number of balls not in the correct position in each tube
   # The heuristic relaxes the constraint that only one ball can be moved at a time, presuming we can move all balls not in the correct position to their correct position in one move
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the cost of moving a ball to its correct position is 1, which is exactly the decrease in the number of balls not in the correct position, and the heuristic estimate for the goal state is 0, as all balls are in the correct position
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != goal[i][j]:
               h += 1
   return h


print(a_star())
