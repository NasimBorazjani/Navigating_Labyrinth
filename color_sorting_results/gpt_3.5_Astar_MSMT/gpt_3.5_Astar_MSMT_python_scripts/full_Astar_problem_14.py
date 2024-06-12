
import heapq

def initialize():
   # Define the initial state of the tubes, represented as a list of lists
   initial_state = [['Green', 'Blue', 'Green', 'Blue'], ['Red', 'Green', 'Red', 'Red'], ['Green', 'Blue', 'Red', 'Blue']]
   num_tubes = 3
   tube_capacity = 6

   visited_costs = {}
   visited_costs[str(initial_state)] = 0

   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))
  
   return initial_state, num_tubes, tube_capacity, visited_costs, queue
  
def a_star():
  
   initial_state, num_tubes, tube_capacity, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heappop(queue)

       # Check if the tubes are sorted by color, ie each tube contains balls of only one color
       if all(len(set(tube)) == 1 for tube in state):
           return actions

       # Generate all possible actions from the current state, which includes moving a ball from one tube to another
       for i in range(num_tubes):
           for j in range(num_tubes):
               if i != j and len(state[i]) > 0 and len(state[j]) < tube_capacity:
                   # Create a new state by moving the top ball from tube i to tube j
                   new_state = [list(tube) for tube in state]
                   ball = new_state[i].pop(0)
                   new_state[j].insert(0, ball)
                   new_state = [tuple(tube) for tube in new_state]
                   # The cost of moving a ball is 1
                   new_cost = g + 1
                  
                   if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                       visited_costs[str(new_state)] = new_cost
                       # Calculate the heuristic cost to reach the goal state
                       h = heuristic(new_state)
                       heappush(queue, (g + h, new_cost, actions + [(i, j)], new_state))
   return None

def heuristic(state):
   # The heuristic is the number of balls that are not in the correct position
   # This heuristic is admissible because it underestimates the cost to reach the goal state, as each move can only correct one ball at a time
   # The heuristic is consistent because the cost of moving a ball is 1, which is exactly the decrease in the heuristic estimate if the ball is moved to the correct position
   correct_state = [['Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Red']]
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] != correct_state[i][j]:
               h += 1
   return h

print(a_star())
