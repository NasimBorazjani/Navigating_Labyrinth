
import heapq


def a_star():
   # Define the initial state of the problem, with the capacities of the jugs, the capacities of the unlabeled buckets, and the current amount of water in each bucket
   initial_state = ((46, 99, 145, 131, 78, 100), (247, 340, 368), (0, 0, 0))
  
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
       # The goal state is when all the unlabeled buckets have the correct amount of water
       if state[1] == (247, 340, 368):
           return actions


       # Generate all possible actions from the current state, which includes adding water from a jug to a bucket, or removing water from a bucket to a jug
       for jug_ind in range(num_jugs):
           for bucket_ind in range(num_buckets):
               # Check if the new state would be valid, ie the amount of water in the bucket must not exceed the amount of water in the next bucket
               if state[1][bucket_ind] + state[0][jug_ind] <= state[1][bucket_ind + 1]:
                   # Generate the new state
                   new_state = (list(state[0]), list(state[1]), list(state[2]))
                   # Add water from the jug to the bucket
                   new_state[1][bucket_ind] += new_state[0][jug_ind]
                   new_state = (tuple(new_state[0]), tuple(new_state[1]), tuple(new_state[2]))
                   # The cost so far is the number of actions made, as the task is to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state), g + 1, actions + [('+', jug_ind, bucket_ind)], new_state))


       for bucket_ind in range(num_buckets):
           for jug_ind in range(num_jugs):
               # Check if the new state would be valid, ie the amount of water in the bucket must not be less than the amount of water in the next bucket
               if state[1][bucket_ind] - state[0][jug_ind] >= state[1][bucket_ind - 1]:
                   # Generate the new state
                   new_state = (list(state[0]), list(state[1]), list(state[2]))
                   # Remove water from the bucket to the jug
                   new_state[1][bucket_ind] -= new_state[0][jug_ind]
                   new_state = (tuple(new_state[0]), tuple(new_state[1]), tuple(new_state[2]))
                   # The cost so far is the number of actions made, as the task is to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state), g + 1, actions + [('-', jug_ind, bucket_ind)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current amount of water in each bucket and the goal amount of water in each bucket
   # This heuristic relaxes the constraint that the amount of water in a bucket cannot exceed the amount of water in the next bucket
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be reduced by a max of the capacity of the jugs
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the capacity of the jugs, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the capacity of the jugs) + h(n)
   h = 0
   for bucket_ind in range(len(state[1])):
       h += abs(state[1][bucket_ind] - state[1][bucket_ind + 1])
   return h


print(a_star())
