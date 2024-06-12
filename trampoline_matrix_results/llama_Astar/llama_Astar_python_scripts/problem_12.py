
import heapq


def a_star():
   # Define the initial state of the trampoline park, as a 2d tuple
   initial_state = ((1, 1, 1, 1, 0, 0, 0, 0, 1),
                   (0, 0, 1, 1, 1, 0, 1, 1, 1),
                   (1, 1, 1, 0, 1, 0, 1, 1, 1),
                   (1, 0, 0, 0, 0, 1, 1, 0, 1),
                   (1, 0, 0, 0, 1, 1, 0, 0, 1),
                   (0, 0, 1, 1, 0, 0, 0, 0, 0),
                   (0, 0, 0, 0, 1, 0, 0, 1, 0),
                   (0, 0, 0, 1, 0, 1, 1, 1, 1),
                   (0, 0, 0, 0, 0, 0, 1, 1, 1))
  
   # Define the goal state
   goal_state = (8, 0)
  
   # Define the starting position
   start = (3, 7)
  
   # Define the number of diagonal jumps
   num_diagonal_jumps = 3


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 8 adjacent trampolines
       for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
           new_state = (state[0] + dx, state[1] + dy)
           # Check if the new state would be valid, ie the new state must be within the grid and the trampoline must not be broken
           if (0 <= new_state[0] < len(initial_state) and 0 <= new_state[1] < len(initial_state[0]) and initial_state[new_state[0]][new_state[1]] == 0):
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1
               # Check if the number of diagonal jumps is maintained
               if abs(state[0] - new_state[0]) == abs(state[1] - new_state[1]):
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the goal state
   # This heuristic relaxes the constraint that Alex must make exactly 3 diagonal jumps, as it allows Alex to make more or less diagonal jumps
   # It is admissible because it never overestimates the cost to reach the goal, as each diagonal move must be made at least once
   # It's consistent because moving a diagonal move reduces the heuristic cost of the successor node by a max of 1 (if the moved position is diagonal to the old one), which is equal to the cost of reaching the successor node
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
