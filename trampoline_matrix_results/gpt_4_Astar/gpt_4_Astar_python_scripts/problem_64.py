
import heapq


def a_star():
   # Define the initial state and the goal state of the problem, represented as tuples
   initial_state = (0, 7)
   goal_state = (12, 1)
  
   # Encoding other variables given in the problem statement
   num_rows = 13
   num_cols = 13
   park_map = [[1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
               [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
               [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
               [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
               [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
               [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1],
               [0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
               [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
               [0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1],
               [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0]]
   # The 8 possible moves from a trampoline
   moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state, 0)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state, num_diagonal_moves = heapq.heappop(queue)


       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if state == goal_state:
           return actions


       # Generate all valid actions from the current state, which includes jumping to any of the 8 neighboring trampolines
       for move in moves:
           new_state = (state[0] + move[0], state[1] + move[1])
           # Check if the new state is valid, ie if the new state is within the bounds of the park and the trampoline is not broken
           if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and park_map[new_state[0]][new_state[1]] == 0):
               # The cost so far is the number of jumps made, as our objective is to minimize the number of jumps required to reach the goal state 
               new_cost = g + 1
               # If the move is diagonal, increment the count of diagonal moves
               new_num_diagonal_moves = num_diagonal_moves + 1 if move in [(1, 1), (-1, -1), (1, -1), (-1, 1)] else num_diagonal_moves
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the Manhattan distance from the current state to the goal state
                   h = abs(new_state[0] - goal_state[0]) + abs(new_state[1] - goal_state[1])
                   # If the number of diagonal moves is less than 4, add 4 - num_diagonal_moves to the heuristic, as we must make at least 4 diagonal moves
                   if new_num_diagonal_moves < 4:
                       h += 4 - new_num_diagonal_moves
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state], new_state, new_num_diagonal_moves))
   return None


print(a_star())
