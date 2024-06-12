
import heapq


def initialize():
   # Define the initial state of the problem, where the first element is the list of capacities of the jugs, the second element is the list of target volumes of the buckets, and the third element is the current state of the buckets
   initial_state = (['76', '48', '35', '94', '93', '115', '16', '53'], ['247', '261', '273'], ['0', '0', '0'])
  
   # Encoding other variables given in the problem statement
   capacities = initial_state[0]
   target_volumes = initial_state[1]
   num_buckets = len(target_volumes)


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, capacities, target_volumes, num_buckets, visited_costs, queue
  
def a_star():
  
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the problem, the capacities of the jugs, the target volumes of the buckets, and the number of buckets)
   initial_state, capacities, target_volumes, num_buckets, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when all the buckets have the correct target volume
       if all(int(volume) == int(target_volumes[i]) for i, volume in enumerate(state[1])):
           return actions


       # Generate all possible actions from the current state, which includes adding water from a jug to a bucket, or removing water from a bucket and pouring it into another bucket
       for from_jug_capacity in capacities:
           for to_bucket_index in range(num_buckets):
               # Check if the new state would be valid, ie the from_jug_capacity must be less than or equal to the target volume of the to_bucket_index
               if int(from_jug_capacity) <= int(target_volumes[to_bucket_index]):
                   # Generate the new state
                   new_state = [list(state[0][:]), list(state[1][:])]
                   new_state[1][to_bucket_index] = str(int(new_state[1][to_bucket_index]) + int(from_jug_capacity))
                   # The cost so far is the number of actions made, as the task is to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if tuple(new_state) not in visited_costs or new_cost < visited_costs[tuple(new_state)]:
                       visited_costs[tuple(new_state)] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, target_volumes), new_cost, actions + [('+', from_jug_capacity, to_bucket_index + 1)], new_state))
   return None


def heuristic(state, target_volumes):
   # An admissible and consistent heuristic for this problem is the sum of the differences between the current volumes of the buckets and their target volumes
   # This heuristic relaxes the constraint that a jug can only be filled to the top and emptied completely, and the unlabeled buckets cannot be overfilled
   # It is admissible because it never overestimates the cost to reach the goal, as each difference between the current volume of a bucket and its target volume must be filled at least once
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the difference between the current volume of the from_bucket and its target volume, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state[1])):
       h += abs(int(state[1][i]) - int(target_volumes[i]))
   return h


print(a_star())
