
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' replaced by None
   initial_state = [[37, 50, None, 70],
                    [None, 46, None, 65],
                    [41, 43, None, 49],
                    [None, 30, None, None]]
   # Define the goal state, where all 'x' are replaced by integers from the given range
   goal_state = [[i for i in range(22, 73)] for _ in range(4)]
   # Define the possible moves, which are the 4 directions a knight can move on a chessboard
   moves = [(2, 1), (1, 2), (-1, 2), (2, -1)]
   # Initialize the visited costs dictionary
   visited_costs = {}
   visited_costs[str(initial_state)] = 0
   # Initialize the priority queue with the initial state
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # If the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state
       for row in range(4):
           for col in range(4):
               # If the current position is marked with an 'x'
               if state[row][col] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   for num in range(22, 73):
                       # Check if the new state would be valid, ie the number is not in the same row or column
                       if num not in new_state[row] and num not in [new_state[i][col] for i in range(4)]:
                           new_state[row][col] = num
                           # The cost so far is the number of moves made, as the task is to minimize the number of moves required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                               visited_costs[str(new_state)] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(state, goal_state), new_cost, actions + [(row, col, num)], new_state))


   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the numbers in the current state and their positions in the goal state
   # This heuristic relaxes the constraint that the numbers must be in consecutive order in each row and column
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be moved at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number's position in the new state is closer to its position in the goal state), which is equal to the cost of reaching the successor node
   h = 0
   for row in range(4):
       for col in range(4):
           if state[row][col] is not None:
               # Get the position of the current number in the goal state
               goal_row, goal_col = [(i, j) for i in range(4) for j in range(4) if goal[i][j] == state[row][col]][0]
               # Add the absolute difference between the current position and the goal position to the estimate
               h += abs(row - goal_row) + abs(col - goal_col)
   return h


print(a_star())
