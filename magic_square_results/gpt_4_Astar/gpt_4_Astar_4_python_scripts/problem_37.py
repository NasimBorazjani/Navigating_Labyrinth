
import heapq


def a_star():
   # Define the initial state of the grid, as a 2d tuple of strings
   initial_state = (('48', 'x', 'x'), ('x', 'x', 'x'), ('x', '49', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of unique integers that can be used to replace 'x's in the grid
   available_numbers = set(range(40, 90))
   # The sum of the numbers in the grid must be as low as possible, thus we must use the smallest numbers in the range first
   available_numbers = sorted(list(available_numbers), reverse=False)
   # The numbers already present in the initial state cannot be used to replace 'x's in the grid
   for row in initial_state:
       for cell in row:
           if cell != 'x':
               available_numbers.remove(int(cell))


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
       # The goal state is where all 'x's in the grid have been replaced with unique integers such that the sum of column 1 is 150, the sum of row 1 is 209, and the sum of the diagonal from the top right to the bottom left corner is 169
       if all(cell != 'x' for row in state for cell in row) and sum(int(cell) for cell in state[0]) == 150 and sum(int(cell) for cell in zip(*state)[1]) == 209 and sum(int(cell) for cell in zip(*state[::-1])[::-1]) == 169:
           return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       if any(cell == 'x' for row in state for cell in row):
           # Find the next 'x' in the grid
           for i in range(num_rows):
               for j in range(num_cols):
                   if state[i][j] == 'x':
                       # Replace the 'x' with each of the available numbers
                       for number in available_numbers:
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[i][j] = str(number)
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the sum of the numbers in the grid, as the task is to minimize the sum of the numbers in the grid
                           new_cost = sum(int(cell) for row in new_state for cell in row if cell != 'x')
                           # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               # The action is represented as a tuple of the row index, column index, and the number replaced with 'x' at that position
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state))
                               # The number used to replace 'x' is no longer available
                               available_numbers.remove(number)
                               break
                       break
               else:
                   continue
               break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the remaining 'x's in the grid multiplied by the smallest number in the range of unique integers
   # The heuristic relaxes the constraints that the sum of column 1 must be 150, the sum of row 1 must be 209, and the sum of the diagonal from the top right to the bottom left corner must be 169, and presumes we can replace all remaining 'x's in the grid with the smallest number in the range
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the cost of replacing an 'x' in the grid with a number is the number itself, which is always greater than or equal to the smallest number in the range, the decrease in the heuristic cost. Thus h(n) can never be greater than c(n, n’)(equal to the number used to replace 'x') + h(n’)
   return sum(cell == 'x' for row in state for cell in row) * 40


print(a_star())
