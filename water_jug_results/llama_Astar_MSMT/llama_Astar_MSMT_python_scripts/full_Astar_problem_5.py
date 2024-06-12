
import heapq


def initialize():
   # Define the initial state of the system, as a tuple of the current amounts of water in the unlabeled buckets and the current amounts of water in the labeled jugs
   initial_state = ((0, 0, 0), (145, 101, 17, 75, 102, 129))
  
   # Encoding other variables given in the problem statement
   capacities = (145, 101, 17, 75, 102, 129)
   goal_amounts = (260, 287, 413)


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, capacities, goal_amounts, visited_costs, queue
  
def a_star():
  
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial and goal amounts of water in the buckets and the capacities of the jugs)
   initial_state, capacities, goal_amounts, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the amounts of water in the unlabeled buckets match the goal amounts
       if state[0] == goal_amounts:
           return actions


       # Generate all valid actions from the current state, which includes filling or emptying any of the unlabeled buckets with any of the jugs
       for i in range(len(capacities)):
           for j in range(3):
               # Check if the new state would be valid, ie the amount of water in the unlabeled bucket must not exceed the amount of water in the bucket placed after it
               if state[0][j] + capacities[i] <= state[0][j + 1]:
                   # Generate the new state
                   new_state = (tuple(state[0][k] + capacities[i] if k == j else state[0][k] for k in range(3)), state[1])
                   # The cost so far is the number of actions made, as our objective is to minimize the number of actions required to reach the goal state
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_amounts), new_cost, actions + [('+', capacities[i], j + 1)], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current amounts of water in the unlabeled buckets and the goal amounts
   # This heuristic relaxes the constraint that the amount of water in each unlabeled bucket can not at any point in time exceed the amount of water in the bucket placed after it
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be filled or emptied at least once
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the difference between the capacities of the jugs, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(3):
       h += abs(state[0][i] - goal[i])
   return h


print(a_star())
