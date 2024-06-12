
import heapq

def initialize():
   # Define the initial state of the buckets as a tuple
   initial_state = (0, 0, 0)
   # Define the goal state of the buckets as a tuple
   goal_state = (274, 297, 343)
   # Define the capacities of the jugs as a list
   jug_capacities = [41, 26, 44, 75, 40, 136]
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, goal_state, jug_capacities, visited_costs, queue
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial and goal state of the buckets and the capacities of the jugs)
   initial_state, goal_state, jug_capacities, visited_costs, queue = initialize()

   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)

       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if state == goal_state:
           return actions

       # Generate all possible actions from the current state, which includes filling each of the 3 buckets with each of the 6 jugs, and emptying each of the 3 buckets with each of the 6 jugs
       for i in range(len(jug_capacities)):
           for j in range(len(state)):
               # Check if the new state would be valid, ie if the bucket can be filled with the jug without overflowing and if the amount of water in each bucket does not exceed the amount of water in the bucket placed after it
               if state[j] + jug_capacities[i] <= goal_state[j] and (j == len(state) - 1 or state[j] + jug_capacities[i] <= state[j + 1]):
                   # The action is valid, generate the new state
                   new_state = list(state)
                   new_state[j] += jug_capacities[i]
                   new_state = tuple(new_state)
                   # The cost so far is the number of actions performed, as our objective is to minimize the number of actions required to reach the goal state 
                   new_cost = g + 1
              
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug_capacities[i], j + 1)], new_state))
              
               # Similarly, check if the new state would be valid, ie if the bucket can be emptied with the jug and if the amount of water in each bucket does not exceed the amount of water in the bucket placed after it
               if state[j] - jug_capacities[i] >= 0 and (j == 0 or state[j] - jug_capacities[i] >= state[j - 1]):
                   # The action is valid, generate the new state
                   new_state = list(state)
                   new_state[j] -= jug_capacities[i]
                   new_state = tuple(new_state)
                   # The cost so far is the number of actions performed, as our objective is to minimize the number of actions required to reach the goal state 
                   new_cost = g + 1
              
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug_capacities[i], j + 1)], new_state))
   return None

def heuristic(state, goal):
   # An admissible and consistent heuristic is the sum of the differences between the current and goal amount of water in each bucket
   # The heuristic relaxes the constraint that the amount of water in each bucket can not at any point in time exceed the amount of water in the bucket placed after it and presumes we can fill or empty the buckets directly to their goal amount
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of filling or emptying a bucket is always 1, which is exactly the decrease or increase in the difference between the current and goal amount of water in the bucket, if the bucket is filled or emptied, respectively, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the difference between the current and goal amount of water in each bucket would be 0 in the goal state.
   return sum(abs(a - b) for a, b in zip(state, goal))

print(a_star())
