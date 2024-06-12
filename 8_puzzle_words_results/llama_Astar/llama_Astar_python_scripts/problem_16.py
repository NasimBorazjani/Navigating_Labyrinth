
import heapq


def a_star():
   # Define the initial state of the board and the target words
   initial_state = [['o', 'g', 'h', 'a'], ['y', 'c', 'd', 'l'], ['o', 'a', '_', 'l'], ['a', 'w', 'l', 'e']]
   target_words = ['goa', 'yodh', 'wall', 'acle']
   num_rows = 4
   num_cols = 4


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == [list(word) for word in target_words]:
           return actions


       # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
       for row_shift in [-1, 0, 1]:
           for col_shift in [-1, 0, 1]:
               # Check if the new state would be valid, ie the new state must not have the blank space out of the board
               if 0 <= state.index('_') + row_shift < num_rows and 0 <= state[0].index('_') + col_shift < num_cols:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[state.index('_') + row_shift][state[0].index('_') + col_shift], new_state[state.index('_')][state[0].index('_')] = new_state[state.index('_')][state[0].index('_')], new_state[state.index('_') + row_shift][state[0].index('_') + col_shift]
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
                   new_cost = g + 1


                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       # The direction of the swap is the direction in which the blank space was swapped in
                       direction = (row_shift, col_shift)
                       heapq.heappush(queue, (new_cost + heuristic(state, target_words, direction), new_cost, actions + [direction], new_state))
   return None




def heuristic(state, target_words, direction):
   # The heuristic function can be a simulation of swapping the blank space greedily, using the next direction as the direction of the swap
   # This heuristic is admissible because it is greedy, always opting for the action that sorts the board the most, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if the blank space is swapped to a position that is further from the goal, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum distance that the blank space can be swapped in one action is by using the largest possible shift in one direction, which is exactly the shift used to swap the blank space in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] == '_':
               # Calculate the Manhattan distance from the current position of the blank space to the goal position
               h += abs(i - target_words.index(state[i][j - 1:i + 1])) + abs(j - len(state[i][j - 1:i + 1]))
   return h


print(a_star())
