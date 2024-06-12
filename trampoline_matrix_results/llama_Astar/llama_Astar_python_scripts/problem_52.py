
import heapq


def a_star():
   # Define the initial state of the trampoline park, as a 12x12 2d list
   initial_state = [[1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                   [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0],
                   [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
                   [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1],
                   [0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1],
                   [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
                   [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0],
                   [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0],
                   [1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0],
                   [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0]]
  
   # Define the start and goal positions
   start = (8, 1)
   goal = (1, 11)


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the jumps required to get to each state in a list; no jumps performed to reach the initial state
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal:
           return actions


       # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines, as long as they are not broken
       for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
           new_state = (state[0] + dx, state[1] + dy)
           # Check if the new state would be valid, ie the new state must be within the grid and not be a broken trampoline
           if (0 <= new_state[0] < 12 and 0 <= new_state[1] < 12 and initial_state[new_state[0]][new_state[1]] == 0):
               # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal state
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal), new_cost, actions + [new_state], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the goal state
   # This heuristic relaxes the constraint that Alex must make exactly 4 diagonal jumps, as the heuristic estimate for the goal state is 0, as the distance of the goal state would be 0 in the goal state
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
