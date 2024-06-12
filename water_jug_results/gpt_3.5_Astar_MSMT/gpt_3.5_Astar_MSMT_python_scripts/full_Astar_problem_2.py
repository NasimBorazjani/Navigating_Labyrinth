
import heapq

def initialize():
   # Define the initial state of the problem, including the capacities of the jugs and the target amounts for the unlabeled buckets
   jug_capacities = [31, 102, 53, 33, 32, 24]
   bucket_targets = [188, 198, 289]
   num_buckets = 3

   visited_costs = {}
   visited_costs[(0, 0, 0, 0, 0, 0)] = 0

   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], (0, 0, 0, 0, 0, 0))]
  
   return jug_capacities, bucket_targets, num_buckets, visited_costs, queue
  
def a_star():
  
   jug_capacities, bucket_targets, num_buckets, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # Check if the current state is the goal state, where the unlabeled buckets have the target amounts
       if state[3:6] == tuple(bucket_targets):
           return actions

       # Generate all possible actions from the current state, which includes filling or emptying the unlabeled buckets using the jugs
       for i in range(len(jug_capacities)):
           for j in range(num_buckets):
               # Fill the unlabeled bucket j using the jug i
               new_state = list(state)
               new_state[j] = min(state[j] + jug_capacities[i], jug_capacities[j])
               # Update the cost of the new state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                   visited_costs[tuple(new_state)] = new_cost
                   heapq.heappush(queue, (g + heuristic(new_state, bucket_targets), new_cost, actions + [('+', jug_capacities[i], j+1)], tuple(new_state)))
                  
               # Empty the unlabeled bucket j using the jug i
               new_state = list(state)
               new_state[j] = 0
               # Update the cost of the new state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                   visited_costs[tuple(new_state)] = new_cost
                   heapq.heappush(queue, (g + heuristic(new_state, bucket_targets), new_cost, actions + [('-', jug_capacities[i], j+1)], tuple(new_state)))
                  
   return None


def heuristic(state, targets):
   # An admissible and consistent heuristic is the sum of the differences between the current amounts in the unlabeled buckets and their target amounts
   # The heuristic relaxes the constraint that the unlabeled buckets cannot be overfilled, presuming we can always empty the buckets to reach the target amounts
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the cost of filling or emptying a bucket is always 1, which is exactly the decrease in the difference between the current amount and the target amount
   # The cost of the goal state is 0, as the amounts in the unlabeled buckets match the target amounts

   h = 0
   for i in range(len(state)-3):
       h += abs(state[i] - targets[i])
   return h


print(a_star())
