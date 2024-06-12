
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, 59], [None, None, None], [38, None, None]]
   # Define the goal state, with the given sums of the row, column, and diagonal
   goal_state = (172, 212, 165)
   # Define the range of the numbers to fill in the grid
   num_range = range(34, 79)

   # Initialize the visited_costs dictionary and the priority queue
   visited_costs = {}
   visited_costs[initial_state] = 0
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, goal_state, num_range, visited_costs, queue
  
def a_star():
  
   initial_state, goal_state, num_range, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # If the current state is the goal state
       if state_sums(state) == goal_state:
           return actions

       # Generate all possible actions from the current state
       for row in range(len(state)):
           for col in range(len(state[row])):
               if state[row][col] is None:
                   for num in num_range:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[row][col] = num
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the number of actions taken
                       new_cost = g + 1

                       # If the new state is unvisited or we found a new path with a lower cost to reach this state
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(state, goal_state), new_cost, actions + [(row, col, num)], new_state))
   return None


def heuristic(state, goal):
   # The heuristic is the sum of the absolute differences between the sums of the current state and the goal state
   return sum(abs(state_sum(state, i) - goal[i]) for i in range(len(goal)))


def state_sum(state, i):
   # Calculate the sum of the specified row, column, or diagonal
   if i == 0:
       return sum(row[0] for row in state)
   elif i == 1:
       return sum(row[1] for row in state)
   elif i == 2:
       return sum(state[i][i] for i in range(len(state)))


def state_sums(state):
   # Return a tuple of the sums of the specified rows, columns, and diagonal
   return (state_sum(state, 0), state_sum(state, 1), state_sum(state, 2))


print(a_star())
