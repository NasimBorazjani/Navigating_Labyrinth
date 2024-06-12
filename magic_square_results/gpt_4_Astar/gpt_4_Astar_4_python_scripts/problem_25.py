
import heapq


def a_star():
   # Define the initial state of the grid, the goal sums of the specified rows, columns, and diagonal, and the range of unique integers that can be used to replace 'x's
   initial_state = (('x', '16', 'x'), ('x', 'x', 'x'), ('45', 'x', 'x'))
   goal_sums = {'row1': 60, 'col1': 67, 'diag': 89}
   num_range = set(range(9, 49))


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where all 'x's have been replaced with unique integers such that the sum of the specified rows, columns, and diagonal equals the given amounts
       if all(cell != 'x' for row in state for cell in row) and sum(int(cell) for row in state for cell in row if cell != 'x') == sum(goal_sums.values()) and sum(int(row[1]) for row in state) == goal_sums['col1'] and sum(int(state[i][1]) for i in range(len(state))) == goal_sums['row1'] and sum(int(state[i][2 - i]) for i in range(len(state))) == goal_sums['diag']:
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
       # The available unique integers are all numbers in the range - numbers present in the current state
       available_numbers = num_range - set(int(cell) for row in state for cell in row if cell != 'x')
       for number in available_numbers:
           # Find the next 'x' in the grid
           for i in range(len(state)):
               for j in range(len(state[i])):
                   if state[i][j] == 'x':
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(number)
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                       new_cost = sum(int(cell) for row in new_state for cell in row if cell != 'x')


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sums), new_cost, actions + [(i, j, number)], new_state))
                       # Stop the loop after the first 'x' is replaced
                       break
               else:
                   continue
               break
   return None


def heuristic(state, goal_sums):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums and the goal sums of the specified rows, columns, and diagonal
   # The heuristic relaxes the constraints that each number in the grid must be unique and that the sum of all of the numbers in the grid must be as low as possible; ie It presumes we can replace any 'x' with any number in the range
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to 1, the decrease in the sum of the absolute differences between the current sums and the goal sums of the specified rows, columns, and diagonal
   h = 0
   # Calculate the current sum of the specified row, column, and diagonal
   current_sums = {'row1': sum(int(state[1][j]) for j in range(len(state[1])) if state[1][j] != 'x'), 'col1': sum(int(state[i][1]) for i in range(len(state)) if state[i][1] != 'x'), 'diag': sum(int(state[i][2 - i]) for i in range(len(state)) if state[i][2 - i] != 'x')}
   # Add the absolute difference between the current and goal sums of the specified row, column, and diagonal to the estimate
   for key in goal_sums.keys():
       h += abs(current_sums[key] - goal_sums[key])
   return h


print(a_star())
