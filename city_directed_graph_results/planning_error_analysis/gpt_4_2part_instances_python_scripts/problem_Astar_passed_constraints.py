
import heapq


def initialize():
   # Define the initial state and the goal state of the puzzle, represented as 3x3 tuples
   initial_state = 'H'
   goal_state = ['K', 'K', 'Z', 'Z']   
  
   # Encoding other variables given in the problem statement
   adjacency_matrix = [[0, 0, 1, 1, 0, 0, 1, 1, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                       [0, 1, 0, 1, 0, 1, 1, 0, 0, 1],
                       [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
                       [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
   cities = ['K', 'B', 'Z', 'S', 'X', 'H', 'O', 'E', 'U', 'V']


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[(initial_state, tuple(goal_state))] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], (initial_state, tuple(goal_state)))]
  
   return initial_state, goal_state, adjacency_matrix, cities, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial and goal board and dimensions of the puzzle board)
   initial_state, goal_state, adjacency_matrix, cities, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)
       current_city, remaining_cities = state


       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if not remaining_cities:
           return actions


       # Generate all valid actions from the current state, which includes moving to any of the cities connected to the current city
       for i in range(len(cities)):
           if adjacency_matrix[cities.index(current_city)][i] == 1:
               next_city = cities[i]
               # Check if the next city is a destination city and we have not visited it twice already
               if next_city in remaining_cities:
                   new_remaining_cities = list(remaining_cities)
                   new_remaining_cities.remove(next_city)
                   new_state = (next_city, tuple(new_remaining_cities))
                   new_cost = g + 1
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [next_city], new_state))
               # If the next city is not a destination city and we have not visited it before, we can move to it
               elif next_city not in actions:
                   new_state = (next_city, remaining_cities)
                   new_cost = g + 1
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [next_city], new_state))
   return None


def heuristic(state, goal_state):
   # An admissible and consistent heuristic is the number of remaining cities to visit
   # The heuristic relaxes the constraint that we can only move to cities connected to the current city and presumes we can move to any of the remaining cities directly from the current city
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a city is always 1, which is exactly the decrease in the number of remaining cities to visit, if the city is a destination city, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as there are no remaining cities to visit in the goal state.
   return len(state[1])


print(a_star())
