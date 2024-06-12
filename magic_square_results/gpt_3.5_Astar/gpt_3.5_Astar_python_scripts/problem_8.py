
import heapq


def a_star():
   # Define the initial state of the magic square grid, with unknown numbers represented as 'x'
   initial_state = [['52', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]
   # Define the goal state, which is the magic square grid with the specified sums in the rows, columns, and diagonal
   goal_state = [['52', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]
   # Define the range of unique integers that can be placed in the grid
   unique_integers = list(range(35, 60))


   visited_costs = {}
   visited_costs[str(initial_state)] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))


   while queue:
       _, g, actions, state = heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes replacing 'x' with unique integers in the grid
       for row in range(3):
           for col in range(3):
               if state[row][col] == 'x':
                   for num in unique_integers:
                       new_state = [row[:] for row in state]
                       new_state[row][col] = str(num)
                       # The cost so far is the sum of the numbers in the grid, as the objective is to minimize this sum
                       new_cost = g + num
                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of unvisited states
                       if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                           visited_costs[str(new_state)] = new_cost
                           heapq.heappush(queue, (new_cost, new_cost, actions + [(row, col, num)], new_state))
   return None


print(a_star())
