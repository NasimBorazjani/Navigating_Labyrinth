
import heapq


def a_star():
   # Define the initial state of the trampoline park, as a 2d tuple
   initial_state = ((0, 0, 0, 1, 1, 1, 0, 1, 0, 0),
                   (0, 0, 0, 1, 1, 0, 1, 1, 0, 1),
                   (1, 0, 1, 1, 1, 1, 0, 0, 1, 1),
                   (0, 1, 0, 1, 0, 0, 1, 1, 1, 1),
                   (0, 0, 0, 0, 0, 0, 1, 1, 1, 1),
                   (1, 1, 1, 0, 0, 0, 1, 1, 1, 0),
                   (1, 0, 1, 1, 0, 0, 1, 1, 1, 1),
                   (1, 0, 1, 1, 1, 0, 0, 0, 0, 0),
                   (1, 1, 0, 1, 0, 1, 1, 1, 0, 0),
                   (0, 1, 1, 1, 0, 1, 1, 1, 1, 1))
  
   # Define the goal state
   goal_state = (7, 6)
  
   # Define the possible moves
   moves = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
  
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


       # Check if the current state is the goal state
       if state[goal_state[0]][goal_state[1]] == 0:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 8 adjacent trampolines
       for move in moves:
           new_row, new_col = goal_state[0] + move[0], goal_state[1] + move[1]
           # Check if the new state would be valid, ie the new position is within the grid and the trampoline is not broken
           if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]) and state[new_row][new_col] == 0:
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[new_row][new_col] = 1
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(new_row, new_col)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the goal state
   # This heuristic relaxes the constraint that Alex must make exactly 3 diagonal jumps, as it allows Alex to make more or less diagonal jumps
   # It is admissible because it never overestimates the cost to reach the goal, as each diagonal jump must be made at least once
   # It's consistent because moving a diagonal jump results in a decrease in the heuristic cost of the successor node by a max of 1 (if the moved diagonal jump is made in the new state), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] == 0:
               h += abs(i - goal[0]) + abs(j - goal[1])
   return h


print(a_star())
