
import heapq


def initialize():
   # Define the initial state of the system, with the capacities of the jugs and the amounts of water in the buckets
   initial_state = ((59, 68, 104, 106, 69, 42), (0, 0, 0))
   # Define the goal state, with the amounts of water in the buckets
   goal_state = (0, (196, 210, 238))
   # Define the capacities of the jugs and the amounts of water in the buckets
   capacities = (59, 68, 104, 106, 69, 42)
   # Define the amounts of water in the buckets
   goal_water = (196, 210, 238)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, goal_state, capacities, goal_water, visited_costs, queue
  
def a_star():
  
   initial_state, goal_state, capacities, goal_water, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state[1] == goal_state[1]:
           return actions


       # Generate all possible actions from the current state, which involves filling or emptying the buckets with the jugs
       for i in range(len(capacities)):
           for j in range(2):
               # Check if the new state would be valid, ie the amount of water in the bucket cannot exceed the amount of water in the next bucket
               if j == 0:
                   new_state = (state[0], (state[1][0] + min(capacities[i], goal_water[0] - state[1][0]), state[1][1], state[1][2]))
               else:
                   new_state = (state[0], (state[1][0], state[1][1] + min(capacities[i], goal_water[1] - state[1][1]), state[1][2]))
               # The cost so far is the number of actions made, as we are trying to minimize the number of actions required
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state, capacities, goal_water), new_cost, actions + [('+', capacities[i], j)], new_state))


               # Generate the new state by emptying the bucket
               new_state = (state[0], (state[1][0] - min(state[1][0], capacities[i]), state[1][1] - min(state[1][1], capacities[i]), state[1][2] - min(state[1][2], capacities[i])))
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state, capacities, goal_water), new_cost, actions + [('-', capacities[i], j)], new_state))
   return None


def heuristic(state, goal_state, capacities, goal_water):
   # An admissible and consistent heuristic for this problem is the sum of the differences between the amounts of water in the buckets and the goal amounts
   # This heuristic relaxes the constraint that the amount of water in a bucket cannot exceed the amount of water in the next bucket
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be filled or emptied at least once
   # It's consistent because moving water from one bucket to another reduces the heuristic cost of the successor node by a max of the capacity of the jug used, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the capacity of the jug used) + h(n)
   h = 0
   for i in range(2):
       h += abs(state[1][i] - goal_water[i])
   return h


print(a_star())
