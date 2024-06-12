
import heapq


def a_star():
   # Define the initial state of the trampoline park, as a 2d tuple
   initial_state = ((0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                   (0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1),
                   (0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0),
                   (0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1),
                   (0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0),
                   (1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1),
                   (1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0),
                   (1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0),
                   (1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1),
                   (1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1),
                   (0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1),
                   (0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0))
  
   # Define the start and goal positions
   start = (1, 1)
   goal = (10, 8)
  
   # Define the possible moves
   moves = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
  
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the moves required to get to each state in a list; no moves performed to reach the initial state
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal:
           return actions


       # Generate all possible moves from the current state
       for move in moves:
           # Calculate the new state
           new_state = (state[0] + move[0], state[1] + move[1])
           # Check if the new state is valid, ie within the grid and not a broken trampoline
           if (0 <= new_state[0] < len(initial_state) and 0 <= new_state[1] < len(initial_state[0]) and initial_state[new_state[0]][new_state[1]] == 0):
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal state
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the Manhattan distance to the goal state
                   h = abs(new_state[0] - goal[0]) + abs(new_state[1] - goal[1])
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state], new_state))
   return None


print(a_star())
