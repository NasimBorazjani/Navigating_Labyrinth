
import heapq


def initialize():
   # Define the initial state of the system as a tuple of the capacities of the jugs and the amounts of water in the buckets
   initial_state = ((144, 37, 73, 79, 75, 74), (0, 0, 0))
   # Define the goal state, where the amounts of water in the buckets are 236, 333, 386 liters respectively
   goal_state = ((144, 37, 73, 79, 75, 74), (236, 333, 386))
   # Define the capacities of the jugs and the amounts of water in the buckets
   capacities = (144, 37, 73, 79, 75, 74)
   # Define the amounts of water in the buckets in the goal state
   goal_water = (236, 333, 386)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, goal_state, capacities, goal_water, visited_costs, queue
  
def a_star():
  
   initial_state, goal_state, capacities, goal_water, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state
       for i in range(len(capacities)):
           for j in range(len(state[1])):
               # Check if the new state would be valid, ie the amount of water in the bucket cannot exceed the amount of water in the bucket placed after it
               if j == len(state[1]) - 1 or state[1][j] <= state[1][j + 1]:
                   # Generate the new state
                   new_state = (capacities, list(state[1]))
                   new_state[1][j] += capacities[i]
                   # The cost so far is the number of actions made, as we are trying to minimize the number of actions required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state, capacities), new_cost, actions + [('+', capacities[i], j + 1)], new_state))


       for j in range(len(state[1])):
           # Check if the new state would be valid, ie the amount of water in the bucket cannot be negative
           if state[1][j] > 0:
               # Generate the new state
               new_state = (capacities, list(state[1]))
               new_state[1][j] -= capacities[i]
               # The cost so far is the number of actions made, as we are trying to minimize the number of actions required
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state, capacities), new_cost, actions + [('-', capacities[i], j + 1)], new_state))
   return None


def heuristic(state, goal_state, capacities):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the amounts of water in the buckets in the current state and the goal state
   # This heuristic relaxes the constraint that the amount of water in each bucket cannot exceed the amount of water in the bucket placed after it
   # It is admissible because it never overestimates the cost to reach the goal state
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the capacity of the jug used, which is equal to the cost of reaching the successor node
   h = 0
   for i in range(len(state[1])):
       h += abs(state[1][i] - goal_state[1][i])
   return h


print(a_star())
