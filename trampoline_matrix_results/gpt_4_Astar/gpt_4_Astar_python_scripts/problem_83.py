
import heapq


def a_star():
   # Define the initial state and the goal state of the problem, represented as tuples
   initial_state = (13, 10)
   goal_state = (4, 0)
   # Define the map of the park
   park_map = [[0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1],
               [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
               [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
               [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
               [0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
               [0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
               [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
               [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
               [1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
               [1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
               [1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
               [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0]]
   num_rows = len(park_map)
   num_cols = len(park_map[0])
   # Define the directions of movement
   directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]


   visited_costs = {}
   visited_costs[(initial_state, 0)] = 0


   queue = [(0, 0, [], initial_state, 0)]


   while queue:
       _, g, actions, state, num_diagonal_jumps = heapq.heappop(queue)


       if state == goal_state:
           return actions


       for d_row, d_col in directions:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state is valid, ie within the bounds of the park and the trampoline is not broken
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and park_map[new_row][new_col] == 0:
               new_state = (new_row, new_col)
               # If the jump is diagonal, increment the count of diagonal jumps
               if abs(d_row) == abs(d_col):
                   new_num_diagonal_jumps = num_diagonal_jumps + 1
               else:
                   new_num_diagonal_jumps = num_diagonal_jumps
               # The new state is valid only if the number of diagonal jumps is less than or equal to 4
               if new_num_diagonal_jumps <= 4:
                   # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal state
                   new_cost = g + 1
                   if (new_state, new_num_diagonal_jumps) not in visited_costs or new_cost < visited_costs[(new_state, new_num_diagonal_jumps)]:
                       visited_costs[(new_state, new_num_diagonal_jumps)] = new_cost
                       h = heuristic(new_state, goal_state)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state], new_state, new_num_diagonal_jumps))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) from the current state to the goal state
   # The heuristic relaxes the constraint that Alex must make exactly 4 diagonal jumps and presumes Alex can move to the goal state by jumping to any of the neighboring trampolines
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if Alex moves toward the goal state, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the distance of the goal state from itself would be 0.
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
