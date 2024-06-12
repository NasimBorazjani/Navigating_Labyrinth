
import heapq


def a_star():
   # Define the initial state and the goal state of the tubes, represented as 3x6 tuples
   initial_state = (('Red', 'Blue', 'Green', 'Red', 'Blue', 'Green'), ('Blue', 'Green', 'Green', 'Blue', 'Red', 'Blue'), ('Green', 'Red', 'Red', 'Green', 'Blue', 'Red'))
   goal_state = (('Red', 'Red', 'Red', 'Red', 'Red', 'Red'), ('Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'), ('Green', 'Green', 'Green', 'Green', 'Green', 'Green'))   
  
   # Encoding other variables given in the problem statement
   num_tubes = 3
   tube_capacity = 9


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the moves required to get to each state in a list; no moves performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if state == goal_state:
           return actions


       # Generate all valid actions from the current state, which includes moving the top ball from any tube to any other tube
       for tube_from in range(num_tubes):
           # Check if the tube from which we want to move a ball is not empty
           if state[tube_from]:
               for tube_to in range(num_tubes):
                   # Check if the tube to which we want to move a ball is not full
                   if len(state[tube_to]) < tube_capacity:
                       # The action is valid, generate the new state
                       new_state = [list(tube[:]) for tube in state]
                       # Move the ball
                       new_state[tube_to].append(new_state[tube_from].pop())
                       new_state = tuple(tuple(tube) for tube in new_state)
                       # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state 
                       new_cost = g + 1
              
                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [(tube_from, tube_to)], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the sum of the number of misplaced balls in each tube
   # The heuristic relaxes the constraint that a ball can only be moved if it is on the top of a tube and presumes we can move the balls to their goal position by moving them directly
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving a ball to a neighboring tube is always 1, which is exactly the decrease in the number of misplaced balls, if the ball is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the number of misplaced balls would be 0 in the goal state.
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           # Can't compare integers with "_" when finding the goal position of each ball, thus ignore the "_" ball
           if state[i][j] != goal[i][j]:
               # Add the the Manhattan distance of the current and goal coordinates of the ball to the estimate
               h += 1
   return h


print(a_star())
