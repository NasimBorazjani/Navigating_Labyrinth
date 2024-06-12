
import heapq


def a_star():
   # Define the initial state of the problem, with the capacities of the jugs and the amounts of water in the unlabeled buckets
   initial_state = ((62, 144, 80, 72, 100, 127, 18, 82, 42, 99), (0, 0, 0))
   goal_state = ((0, 0, 0), (258, 310, 514))
  
   # Encoding other variables given in the problem statement
   jug_capacities = [62, 144, 80, 72, 100, 127, 18, 82, 42, 99]
   num_jugs = len(jug_capacities)
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


       # Generate all possible actions from the current state, which includes adding water from any of the jugs to any of the unlabeled buckets, or removing water from any of the unlabeled buckets
       for jug_capacity in jug_capacities:
           for bucket_num in range(num_buckets):
               # Check if the new state would be valid, ie the amount of water in the unlabeled bucket must not exceed the amount of water in the bucket placed after it
               if state[1][bucket_num] + jug_capacity <= state[1][bucket_num + 1]:
                   # Generate the new state
                   new_state = (list(state[0]), list(state[1]))
                   new_state[1][bucket_num] += jug_capacity
                   new_state = (tuple(new_state[0]), tuple(new_state[1]))
                   # The cost so far is the number of actions made, as the task is to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('+', jug_capacity, bucket_num + 1)], new_state))


                   # Generate the new state by removing water from the bucket
                   new_state = (list(state[0]), list(state[1]))
                   new_state[1][bucket_num] -= jug_capacity
                   new_state = (tuple(new_state[0]), tuple(new_state[1]))
                   # The cost so far is the number of actions made
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('-', jug_capacity, bucket_num + 1)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the amounts of water in the unlabeled buckets in the current state and the goal state
   # This heuristic relaxes the constraint that the amount of water in each unlabeled bucket cannot at any point in time exceed the amount of water in the bucket placed after it
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be reduced by a max of the jug capacity in each action
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the jug capacity, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state[1])):
       h += abs(state[1][i] - goal[1][i])
   return h


print(a_star())
