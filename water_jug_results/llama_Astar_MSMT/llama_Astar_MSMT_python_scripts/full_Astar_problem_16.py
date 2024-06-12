
import heapq


def initialize():
   # Define the initial state of the system, with the capacities of the jugs and the amounts of water in the buckets
   initial_state = ((102, 130, 82, 131, 133, 116), (0, 0, 0))
   # Define the goal state, with the amounts of water in the buckets
   goal_state = ((0, 0, 0), (265, 368, 378))
   # Define the capacities of the jugs
   capacities = (102, 130, 82, 131, 133, 116)
   # Define the amounts of water in the buckets
   bucket_capacities = (265, 368, 378)
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, goal_state, capacities, bucket_capacities, visited_costs, queue
  
def a_star():
  
   initial_state, goal_state, capacities, bucket_capacities, visited_costs, queue = initialize()


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[1] == goal_state[1]:
           return actions


       # Generate all possible actions from the current state, which involves filling or emptying a bucket with a jug
       for jug_capacity in capacities:
           for bucket_num in range(len(state[1])):
               # Check if the new state would be valid, ie the bucket must not be overfilled
               if state[1][bucket_num] + jug_capacity <= bucket_capacities[bucket_num]:
                   # Generate the new state
                   new_state = (state[0], list(state[1]))
                   new_state[1][bucket_num] += jug_capacity
                   # The cost so far is the number of actions made, as the task is to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('+', jug_capacity, bucket_num)], new_state))


       # Generate all possible actions from the current state, which involves emptying a bucket into a jug
       for bucket_num in range(len(state[1])):
           for jug_capacity in capacities:
               # Check if the new state would be valid, ie the jug must not be emptied completely
               if state[1][bucket_num] - jug_capacity >= 0:
                   # Generate the new state
                   new_state = (state[0], list(state[1]))
                   new_state[1][bucket_num] -= jug_capacity
                   # The cost so far is the number of actions made, as the task is to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('-', jug_capacity, bucket_num)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the amounts of water in the buckets in the current state and the goal state
   # This heuristic relaxes the constraint that a jug can only be filled to the top and emptied completely, and the unlabeled buckets cannot be overfilled
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be filled or emptied at least once
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the capacity of the jug, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the capacity of the jug) + h(n)
   h = 0
   for i in range(len(state[1])):
       h += abs(state[1][i] - goal[1][i])
   return h


print(a_star())
