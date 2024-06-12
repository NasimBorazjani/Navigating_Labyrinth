
import heapq


def initialize():
   # Define the initial state of the system, with the capacities of the jugs and the amounts of water in the unlabeled buckets
   initial_state = ((52, 131, 82, 132, 117, 65), (0, 0, 0))
   # Define the goal state, with the amounts of water in the unlabeled buckets
   goal_state = ((0, 0, 0), (357, 384, 522))
   # Define the capacities of the jugs and the unlabeled buckets
   capacities = (52, 131, 82, 132, 117, 65, 0, 0, 0)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, goal_state, capacities, visited_costs, queue
  
def a_star():
  
   initial_state, goal_state, capacities, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[1] == goal_state[1]:
           return actions


       # Generate all possible actions from the current state, which involves adding or removing water from the unlabeled buckets
       for i in range(len(capacities)):
           for j in range(len(state[1])):
               # Check if the new state would be valid, ie the amount of water in the unlabeled bucket must not exceed the amount of water in the bucket placed after it
               if i < len(capacities) - len(state[1]) or state[1][j] + capacities[i] <= state[1][j + 1]:
                   # Generate the new state
                   new_state = (list(state[0]), list(state[1]))
                   new_state[1][j] += capacities[i]
                   new_state = (tuple(new_state[0]), tuple(new_state[1]))
                   # The cost so far is the number of actions made, as we aim to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('+', capacities[i], j)], new_state))


       for i in range(len(capacities)):
           for j in range(len(state[1])):
               # Check if the new state would be valid, ie the amount of water in the unlabeled bucket must not be negative
               if state[1][j] - capacities[i] >= 0:
                   # Generate the new state
                   new_state = (list(state[0]), list(state[1]))
                   new_state[1][j] -= capacities[i]
                   new_state = (tuple(new_state[0]), tuple(new_state[1]))
                   # The cost so far is the number of actions made, as we aim to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [('-', capacities[i], j)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the amounts of water in the unlabeled buckets in the current state and the goal state
   # This heuristic relaxes the constraint that the amount of water in each unlabeled bucket must not exceed the amount of water in the bucket placed after it
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be reduced by at least 1
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of 1 (if the moved water's amount matches the difference between the amounts of water in the new and old buckets), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state[1])):
       h += abs(state[1][i] - goal[1][i])
   return h


print(a_star())
