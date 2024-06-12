
import heapq


def a_star():
   # Define the initial state of the grid, the range of unique integers, and the sums of the specified rows, columns, and diagonal
   initial_state = (('x', 'x', 'x'), ('x', 'x', '55'), ('x', 'x', 'x'))
   unique_integers = set(str(i) for i in range(48, 78))
   row_1_sum = 167
   col_1_sum = 190
   diagonal_sum = 172


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
       # The goal state is where all of the numbers in the grid are unique integers and the sum of the specified rows, columns, and diagonal equal the given amounts
       if all(cell != 'x' for row in state for cell in row) and sum(int(cell) for cell in state[1]) == row_1_sum and sum(int(state[i][1]) for i in range(3)) == col_1_sum and sum(int(state[i][2 - i]) for i in range(3)) == diagonal_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       for i in range(3):
           for j in range(3):
               if state[i][j] == 'x':
                   for number in unique_integers - set(cell for row in state for cell in row if cell != 'x'):
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = number
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                       new_cost = g + int(number)


                       # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, int(number))], new_state))
                   break
           else:
               continue
           break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the remaining 'x's in the grid multiplied by the minimum number in the range of unique integers
   # This heuristic relaxes the constraints that the numbers in the grid must be unique and that the sum of the specified rows, columns, and diagonal must equal the given amounts; ie It presumes we can replace all of the remaining 'x's in the grid with the minimum number in the range
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' in the grid with a number is the number itself, which is always greater than or equal to the minimum number in the range, the decrease in the heuristic estimate
   return sum(cell == 'x' for row in state for cell in row) * 48


print(a_star())
