
import heapq


def a_star():
   # Define the initial state of the trampoline park as a 2d tuple
   initial_state = ((0, 1, 0, 1, 0, 1, 1, 1, 1),
                   (0, 0, 1, 1, 0, 0, 0, 0, 1),
                   (0, 0, 0, 1, 1, 1, 0, 0, 1),
                   (0, 0, 0, 0, 0, 0, 0, 1, 0),
                   (0, 0, 0, 0, 0, 1, 1, 1, 1),
                   (0, 0, 1, 1, 1, 1, 0, 1, 1),
                   (0, 0, 0, 1, 1, 1, 1, 1, 0),
                   (1, 0, 1, 1, 1, 1, 1, 0, 1),
                   (0, 1, 1, 1, 1, 1, 0, 1, 0))
   num_rows = 9
   num_cols = 9
   start = (8, 0)
   goal = (2, 7)
   # The heuristic is the Manhattan distance between the current position and the goal position
   heuristic = lambda state: abs(state[0] - goal[0]) + abs(state[1] - goal[1])


   visited_costs = {}
   visited_costs[start] = 0


   queue = [(0, 0, [], start)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state
       if state == goal:
           return actions


       # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines, as long as they are not broken (represented by 0)
       for row_offset, col_offset in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
           new_state = (state[0] + row_offset, state[1] + col_offset)
           # Check if the new state would be valid, ie the new state must be within the grid and the trampoline must not be broken
           if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and initial_state[new_state[0]][new_state[1]] == 0):
               # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal state
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the Manhattan distance between the new state and the goal state
                   h = heuristic(new_state)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state], new_state))
   return None


print(a_star())
