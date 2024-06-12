
import heapq


def initialize():
   # Define the initial state of the problem, as a list of the capacities of the jugs and the amounts of water in the unlabeled buckets
   initial_state = ([71, 124, 95, 42, 56, 41], [0, 0, 0])
   # Define the goal state, as the amounts of water in the unlabeled buckets
   goal_state = [291, 292, 326]
   # Define the capacities of the jugs
   capacities = [71, 124, 95, 42, 56, 41]
   # Define the maximum index of the unlabeled buckets
   num_buckets = 3


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, goal_state, capacities, num_buckets, visited_costs, queue
  
def a_star():
  
   initial_state, goal_state, capacities, num_buckets, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[1] == goal_state:
           return actions


       # Generate all possible actions from the current state, which involves filling or emptying the unlabeled buckets with the jugs
       for i in range(len(capacities)):
           for j in range(num_buckets):
               # Check if the new state would be valid, ie the amount of water in the unlabeled bucket must not exceed the amount of water in the bucket placed after it
               if state[1][j] + capacities[i] <= state[1][j + 1]:
                   # Generate the new state
                   new_state = (list(capacities[:]), list(state[1][:]))
                   new_state[1][j] += capacities[i]
                   new_state = (tuple(new_state[0]), tuple(new_state[1]))
                   # The cost so far is the number of actions made, as the task is to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('+', capacities[i], j + 1)], new_state))


                   # Generate the new state by emptying the unlabeled bucket
                   new_state = (list(capacities[:]), list(state[1][:]))
                   new_state[1][j] -= capacities[i]
                   new_state = (tuple(new_state[0]), tuple(new_state[1]))
                   # The cost so far is the number of actions made
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('-', capacities[i], j + 1)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the amounts of water in the unlabeled buckets in the current state and the goal state
   # This heuristic relaxes the constraint that the amount of water in each unlabeled bucket cannot at any point in time exceed the amount of water in the bucket placed after it
   # It is admissible because it never overestimates the cost to reach the goal state
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the amount of water moved, which is equal to the cost of reaching the successor node
   return sum(abs(state[1][i] - goal[i]) for i in range(len(goal)))


print(a_star())
