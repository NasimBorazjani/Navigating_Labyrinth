
import heapq


def initialize():
   # Define the initial state of the system, with the capacities of the jugs and the amounts of water in the buckets
   initial_state = ((19, 50, 12, 63, 143, 13), (0, 0, 0))
   # Define the goal state, with the amounts of water in the buckets
   goal_state = (0, 160, 170, 330)
   # Define the capacities of the jugs and the amounts of water in the buckets
   capacities = (19, 50, 12, 63, 143, 13)
   # Define the amounts of water in the buckets
   bucket_amounts = (0, 160, 170, 330)
   # Define the number of jugs and buckets
   num_jugs = 5
   num_buckets = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, goal_state, capacities, bucket_amounts, num_jugs, num_buckets, visited_costs, queue
  
def a_star():
  
   initial_state, goal_state, capacities, bucket_amounts, num_jugs, num_buckets, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[1] == goal_state:
           return actions


       # Generate all possible actions from the current state, which involves filling or emptying the buckets with the jugs
       for jug_ind in range(num_jugs):
           for bucket_ind in range(num_buckets):
               # Check if the new state would be valid, ie the amount of water in the bucket must not exceed the amount of water in the next bucket
               if state[1][bucket_ind] + capacities[jug_ind] <= state[1][bucket_ind + 1]:
                   # Generate the new state
                   new_state = (capacities, list(state[1]))
                   new_state[1][bucket_ind] += capacities[jug_ind]
                   # The cost so far is the number of actions made, as the task is to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('+', capacities[jug_ind], bucket_ind + 1)], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the differences between the amounts of water in the buckets in the current state and the goal state
   # This heuristic relaxes the constraint that the amount of water in a bucket cannot exceed the amount of water in the next bucket
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be filled or emptied at least once
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the capacity of the jug used, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the capacity of the jug used) + h(n)
   h = 0
   for i in range(len(state[1])):
       h += abs(state[1][i] - goal[i])
   return h


print(a_star())
