
import heapq


def initialize():
   # Define the initial state and the goal state of the puzzle, represented as 3x3 tuples
   initial_state = 'D'
   goal_state = ['K', 'Q']   
  
   # Encoding other variables given in the problem statement
   adjacency_matrix = {
       'S': ['I', 'Q'],
       'U': ['X'],
       'X': ['R', 'K'],
       'D': ['U', 'Z'],
       'I': ['U', 'Q'],
       'Z': ['I', 'K'],
       'R': ['S', 'U'],
       'M': ['X', 'I'],
       'K': ['R', 'M'],
       'Q': ['U', 'D', 'I', 'Z', 'K']
   }


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the swaps required to get to each state in a list; no swaps performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, goal_state, adjacency_matrix, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial and goal board and dimensions of the puzzle board)
   initial_state, goal_state, adjacency_matrix, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if all(actions.count(city) == 2 for city in goal_state):
           return actions


       # Generate all valid actions from the current state, which includes moving to any of the cities neighboring the current city
       for city in adjacency_matrix[state]:
           # The actions is valid, generate the new state
           new_state = city
           # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state 
           new_cost = g + 1
          
           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
               visited_costs[new_state] = new_cost
               heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of each tile from its goal position
   # The heuristic relaxes the constraint that a tile can only be swapped with the empty spot and presumes we can move the tiles to their goal position by swapping them with any of the other tiles
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving a tile to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if the tile is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of each tile from its goal position would be 0 in the goal state.
   h = 0
   for city in goal:
       if state != city:
           h += 1
   return h


print(a_star())
