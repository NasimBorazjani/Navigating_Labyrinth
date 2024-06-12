
import heapq


def initialize():
   # Define the initial state of the system, with the capacities of the jugs and the amounts of water in the buckets
   initial_state = ((143, 117, 116, 103, 84, 87), (0, 0, 0))
   # Define the goal state, with the amounts of water in the buckets
   goal_state = (0, 398, 440, 440)
   # Define the capacities of the jugs and the amounts of water in the buckets
   capacities = (143, 117, 116, 103, 84, 87)
   num_jugs = len(capacities)
   num_buckets = len(goal_state) - 1


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, goal_state, capacities, num_jugs, num_buckets, visited_costs, queue
  
def a_star():
  
   initial_state, goal_state, capacities, num_jugs, num_buckets, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[1] == goal_state:
           return actions


       # Generate all possible actions from the current state, which involves filling or emptying the buckets with the jugs
       for jug_ind in range(num_jugs):
           for bucket_ind in range(num_buckets):
               # Check if the new state would be valid, ie the jug must not be empty and the bucket must not be full
               if state[0][jug_ind] > 0 and state[1][bucket_ind] < capacities[jug_ind]:
                   # Generate the new state
                   new_state = (list(state[0]), list(state[1]))
                   # The amount of water to transfer is the minimum of the amount of water in the jug and the capacity of the bucket
                   transfer_amount = min(state[0][jug_ind], capacities[jug_ind] - state[1][bucket_ind])
                   new_state[0][jug_ind] -= transfer_amount
                   new_state[1][bucket_ind] += transfer_amount
                   new_state = (tuple(new_state[0]), tuple(new_state[1]))
                   # The cost so far is the number of actions made, as the task is to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('+', jug_ind, bucket_ind)], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the differences between the amounts of water in the buckets and the amounts in the goal state
   # This heuristic relaxes the constraint that the amount of water in a bucket must not exceed the amount of water in the bucket placed after it
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be filled or emptied by at least one action
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the difference between the amounts of water in the two buckets, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for bucket_ind in range(len(goal) - 1):
       h += abs(state[1][bucket_ind] - goal[bucket_ind])
   return h


print(a_star())
