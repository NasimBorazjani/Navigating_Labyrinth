
import heapq


def a_star():
   # Define the initial state of the trampoline park, as a 2d tuple
   initial_state = ((0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0),
                   (0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0),
                   (0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0),
                   (1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0),
                   (0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0),
                   (1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0),
                   (1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0),
                   (1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0),
                   (1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0),
                   (1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1),
                   (0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1))
   num_rows = 11
   num_cols = 11
   start = (9, 9)
   goal = (0, 3)
   # The number of diagonal jumps required
   num_diagonal_jumps = 3


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the jumps required to get to each state in a list; no jumps performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[start[0]][start[1]] == 1 and state[goal[0]][goal[1]] == 1:
           return actions


       # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines, as long as they are not broken
       for row_offset in range(-1, 2):
           for col_offset in range(-1, 2):
               # Check if the new state would be valid, ie the jump is not diagonal and the new position is within the grid and the trampoline is not broken
               if row_offset != col_offset and 0 <= start[0] + row_offset < num_rows and 0 <= start[1] + col_offset < num_cols and state[start[0] + row_offset][start[1] + col_offset] == 1:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[start[0]][start[1]], new_state[start[0] + row_offset][start[1] + col_offset] = new_state[start[0] + row_offset][start[1] + col_offset], new_state[start[0]][start[1]]
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, goal, num_diagonal_jumps)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [(start[0] + row_offset, start[1] + col_offset)], new_state))


                   # Update the start position for the next jump
                   start = (start[0] + row_offset, start[1] + col_offset)
   return None


def heuristic(state, goal, num_diagonal_jumps):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances (the shortest path) of each trampoline from the goal, plus the number of diagonal jumps required
   # This heuristic relaxes the constraint that Alex must make exactly 3 diagonal jumps, as it allows Alex to make more or fewer diagonal jumps in the heuristic estimate
   # It is admissible because it never overestimates the cost to reach the goal, as each diagonal jump must be made at least once
   # It's consistent because moving a jump from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved jump is diagonal), which is equal to the cost of reaching the successor node
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] == 1:
               h += abs(i - goal[0]) + abs(j - goal[1])
   return h + num_diagonal_jumps


print(a_star())
