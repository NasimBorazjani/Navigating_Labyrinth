
import heapq


def a_star():
   # Define the initial state of the grid, as a 2d tuple of integers and 'x's
   initial_state = (('x', 77, 'x'), (49, 'x', 'x'), ('x', 'x', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   available_numbers = set(range(34, 79))


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
       # The goal state is where all the 'x's in the grid are replaced with unique integers such that the sum of column 1 is 180, sum of row 1 is 156, and the sum of the diagonal from the top right to the bottom left corner is 127
       if all(cell != 'x' for row in state for cell in row) and sum(int(cell) for cell in state[0]) == 180 and sum(int(state[i][1]) for i in range(num_rows)) == 156 and sum(int(state[i][num_cols - i - 1]) for i in range(num_rows)) == 127:
           return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       if any(cell == 'x' for row in state for cell in row):
           # Find the next 'x' in the grid
           for i in range(num_rows):
               for j in range(num_cols):
                   if state[i][j] == 'x':
                       # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
                       for number in available_numbers - set(cell for row in state for cell in row if cell != 'x'):
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[i][j] = number
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the sum of all the numbers in the grid, as the task is to minimize the sum of all the numbers in the grid
                           new_cost = sum(int(cell) for row in new_state for cell in row if cell != 'x')


                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state))
                       return
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number for each remaining 'x' in the grid
   # This heuristic is admissible because it always chooses the smallest available number to replace the 'x's, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a number is added to the grid, or equal or less by at most the smallest available number (equal to the cost of reaching the successor node, ie the smallest available number) as the minimum number that can be added to the grid is the smallest available number, which is exactly the number used to replace the 'x's in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to the smallest available number) + h(n’)
   h = 0
   available_numbers = set(range(34, 79)) - set(cell for row in state for cell in row if cell != 'x')
   for row in state:
       for cell in row:
           if cell == 'x':
               h += min(available_numbers)
               available_numbers.remove(min(available_numbers))
   return h


print(a_star())
