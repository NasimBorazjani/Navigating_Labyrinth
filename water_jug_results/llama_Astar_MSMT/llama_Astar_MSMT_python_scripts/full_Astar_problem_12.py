
import heapq


def initialize():
   # Define the initial state of the system, with the capacities of the jugs and the amounts of water in the buckets
   initial_state = ((46, 99, 145, 131, 78, 100), (0, 0, 0))
   # Define the goal state, with the amounts of water in the buckets
   goal_state = ((0, 0, 0), (247, 340, 368))
   # Define the capacities of the jugs and the amounts of water in the buckets
   capacities = (46, 99, 145, 131, 78, 100)
   # Define the amounts of water in the buckets
   goal_volumes = (247, 340, 368)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, goal_state, capacities, goal_volumes, visited_costs, queue
  
def a_star():
  
   initial_state, goal_state, capacities, goal_volumes, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[1] == goal_state[1]:
           return actions


       # Generate all possible actions from the current state
       for i in range(len(capacities)):
           for j in range(len(state[1])):
               # Check if the new state would be valid, ie the amount of water in the bucket cannot exceed the amount of water in the next bucket
               if state[1][j] + capacities[i] <= goal_volumes[j] and state[1][j] + capacities[i] <= state[1][j + 1]:
                   # Generate the new state
                   new_state = (list(state[0]), list(state[1]))
                   new_state[1][j] += capacities[i]
                   new_state = (tuple(new_state[0]), tuple(new_state[1]))
                   # The cost so far is the number of actions made, as we are trying to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state, capacities, goal_volumes), new_cost, actions + [('+', capacities[i], j + 1)], new_state))


                   # Similarly, check if the new state, with the water removed from the bucket, would be valid
                   if state[1][j] - capacities[i] >= 0:
                       new_state = (list(state[0]), list(state[1]))
                       new_state[1][j] -= capacities[i]
                       new_state = (tuple(new_state[0]), tuple(new_state[1]))
                       new_cost = g + 1


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state, capacities, goal_volumes), new_cost, actions + [('-', capacities[i], j + 1)], new_state))
   return None


def heuristic(state, goal_state, capacities, goal_volumes):
   # An admissible and consistent heuristic for this problem is the sum of the differences between the amounts of water in the buckets in the current state and the amounts in the goal state
   # This heuristic relaxes the constraints that the amount of water in a bucket cannot exceed the amount of water in the next bucket, and the amount of water in a bucket can only be added or removed using the jugs with the specified capacities
   # It is admissible because it never overestimates the cost to reach the goal state
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the capacity of the jug used, which is equal to the cost of reaching the successor node
   h = 0
   for i in range(len(state[1])):
       h += abs(state[1][i] - goal_state[1][i])
   return h


print(a_star())
