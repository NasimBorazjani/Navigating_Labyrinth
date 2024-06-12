
import heapq


def initialize():
   # Define the initial state of the system as a 3-tuple of the current amounts of water in the unlabeled buckets
   initial_state = (0, 0, 0)
  
   # Encoding other variables given in the problem statement
   jug_capacities = [16, 124, 57, 40, 99, 45, 72, 98]
   target_amounts = [263, 341, 360]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, jug_capacities, target_amounts, visited_costs, queue
  
def a_star():
  
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the system, jug capacities, and target amounts)
   initial_state, jug_capacities, target_amounts, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check of the current state is the goal state
       if state == tuple(target_amounts):
           return actions


       # Generate all possible actions from the current state, which includes adding water from a jug to a bucket or removing water from a bucket to a jug
       for jug_capacity in jug_capacities:
           for bucket_ind in range(len(state)):
               # Check if the new state would be valid, ie the action must not overfill the bucket
               if state[bucket_ind] + jug_capacity <= target_amounts[bucket_ind]:
                   # Generate the new state
                   new_state = list(state)
                   new_state[bucket_ind] += jug_capacity
                   new_state = tuple(new_state)
                   # The cost so far is the number of actions made, as the task is to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, target_amounts), new_cost, actions + [('+', jug_capacity, bucket_ind)], new_state))


       # Generate all possible actions from the current state, which includes removing water from a bucket to a jug
       for bucket_ind in range(len(state)):
           for jug_capacity in jug_capacities:
               # Check if the new state would be valid, ie the action must not remove more water than the bucket has
               if state[bucket_ind] >= jug_capacity:
                   # Generate the new state
                   new_state = list(state)
                   new_state[bucket_ind] -= jug_capacity
                   new_state = tuple(new_state)
                   # The cost so far is the number of actions made, as the task is to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, target_amounts), new_cost, actions + [('-', jug_capacity, bucket_ind)], new_state))
   return None


def heuristic(state, target_amounts):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current amounts of water in the buckets and their target amounts
   # This heuristic relaxes the constraint that a bucket can only be filled to the top and emptied completely, and the unlabeled buckets cannot be overfilled
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched amount must be adjusted at least once
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the capacity of the jug used, which is equal to the cost of reaching the successor node
   h = 0
   for i in range(len(state)):
       h += abs(state[i] - target_amounts[i])
   return h


print(a_star())
