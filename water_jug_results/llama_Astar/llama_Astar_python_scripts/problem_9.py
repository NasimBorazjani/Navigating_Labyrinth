
import heapq


def a_star():
   # Define the initial state of the problem, with the capacities of the jugs and the amounts of water in the buckets
   initial_state = ((129, 57, 45, 105, 128, 78), (0, 0, 0))
   goal_state = ((0, 0, 0), (344, 376, 386))
  
   # Encoding other variables given in the problem statement
   num_jugs = 6
   num_buckets = 3


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[1] == goal_state[1]:
           return actions


       # Generate all possible actions from the current state, which includes adding water from any of the jugs to any of the buckets, or removing water from any of the buckets
       for jug_capacity in range(1, num_jugs + 1):
           for bucket_num in range(1, num_buckets + 1):
               # Check if the new state would be valid, ie the amount of water in the bucket must not exceed the amount of water in the next bucket
               if state[1][bucket_num - 1] + jug_capacity <= goal_state[1][bucket_num - 1] and state[1][bucket_num - 1] + jug_capacity <= state[0][jug_capacity - 1]:
                   # Generate the new state
                   new_state = (list(state[0]), list(state[1]))
                   new_state[1][bucket_num - 1] += jug_capacity
                   new_state = tuple(tuple(jug) for jug in new_state)
                   # The cost so far is the number of actions made, as the task is to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('+', jug_capacity, bucket_num)], new_state))


       for bucket_num in range(1, num_buckets + 1):
           # Check if the new state would be valid, ie the amount of water in the bucket must not be negative
           if state[1][bucket_num - 1] - 1 >= 0:
               # Generate the new state
               new_state = (list(state[0]), list(state[1]))
               new_state[1][bucket_num - 1] -= 1
               new_state = tuple(tuple(jug) for jug in new_state)
               # The cost so far is the number of actions made, as the task is to minimize the number of actions required
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('-', 0, bucket_num)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the amounts of water in the buckets in the current state and the amounts in the goal state
   # This heuristic relaxes the constraint that the amount of water in a bucket must not exceed the amount of water in the next bucket, as it allows the amounts of water in the buckets to be temporarily greater than the amounts in the goal state
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be reduced by at least 1
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of 1 (if the moved water is 1), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state[1])):
       h += abs(state[1][i] - goal_state[1][i])
   return h


print(a_star())
