
import heapq

def initialize():
   # Define the initial state of the problem, which includes the capacities of the jugs and the target amounts for the unlabeled buckets
   jugs = [36, 88, 132, 70, 87, 111]
   buckets = [225, 237, 243]
   num_buckets = len(buckets)
   num_jugs = len(jugs)

   visited_costs = {}
   visited_costs[(0, 0, 0, 0, 0, 0)] = 0

   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   queue = [(0, 0, [], (0, 0, 0, 0, 0, 0))]
  
   return jugs, buckets, num_buckets, num_jugs, visited_costs, queue
  
def a_star():
  
   jugs, buckets, num_buckets, num_jugs, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # Check if the current state is the goal state, where the unlabeled buckets are filled as specified
       if state[:num_buckets] == tuple(buckets):
           return actions

       # Generate all possible actions from the current state, which includes filling or emptying the unlabeled buckets using the jugs
       for i in range(num_jugs):
           for j in range(num_buckets):
               # Fill the j-th bucket using the i-th jug
               new_state = list(state)
               new_state[j] = min(buckets[j], new_state[j] + jugs[i])
               # Check if the new state is valid, ie the amount of water in each bucket does not exceed the amount in the next bucket
               if all(new_state[k] <= new_state[k + 1] for k in range(num_buckets - 1)):
                   new_state = tuple(new_state)
                   # The cost of the new state is the amount of water added or removed from the bucket
                   new_cost = g + jugs[i]
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (g + 1, new_cost, actions + [('+', jugs[i], j + 1)], new_state))
                  
               # Empty the j-th bucket using the i-th jug
               new_state = list(state)
               new_state[j] = 0
               # Check if the new state is valid, ie the amount of water in each bucket does not exceed the amount in the next bucket
               if all(new_state[k] <= new_state[k + 1] for k in range(num_buckets - 1)):
                   new_state = tuple(new_state)
                   # The cost of the new state is the amount of water added or removed from the bucket
                   new_cost = g + jugs[i]
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (g + 1, new_cost, actions + [('-', jugs[i], j + 1)], new_state))
   return None

print(a_star())
