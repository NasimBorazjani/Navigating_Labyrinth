
import heapq


def initialize():
   # Define the initial state of the system, with the capacities of the jugs and the amounts of water in the buckets
   initial_state = ((76, 135, 134, 19, 10, 30), (0, 0, 0))
   # Define the goal state, with the amounts of water in the buckets
   goal_state = (0, 390, 420, 439)
   # Define the capacities of the jugs and the amounts of water in the buckets
   capacities = (76, 135, 134, 19, 10, 30)
   # Define the amounts of water in the buckets
   bucket_amounts = (0, 390, 420, 439)
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, goal_state, capacities, bucket_amounts, visited_costs, queue
  
def a_star():
  
   initial_state, goal_state, capacities, bucket_amounts, visited_costs, queue = initialize()


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[1] == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes filling or emptying each bucket with each jug
       for jug_capacity in capacities:
           for bucket_num in range(len(state[1])):
               # Check if the new state would be valid, ie the amount of water in the bucket must not exceed the amount of water in the next bucket
               if state[1][bucket_num] + jug_capacity <= state[1][bucket_num + 1]:
                   # Generate the new state
                   new_state = (capacities, list(state[1]))
                   new_state[1][bucket_num] += jug_capacity
                   # The cost so far is the number of actions made, as the task is to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('+', jug_capacity, bucket_num)], new_state))


                   # Generate the new state by emptying the bucket
                   new_state = (capacities, list(state[1]))
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
   # This heuristic relaxes the constraint that the amount of water in a bucket must not exceed the amount of water in the next bucket
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be filled or emptied by a max of the jug capacity
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the jug capacity, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state[1])):
       h += abs(state[1][i] - goal[i])
   return h


print(a_star())
