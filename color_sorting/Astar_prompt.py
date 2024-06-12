import heapq
from collections import Counter

def a_star():
    # Define the initial state of the tubes, as a 2d tuple of color of the balls in tubes 0 to 2
    initial_state = (('Green', 'Red', 'Green', 'Red'), ('Blue', 'Blue', 'Red', 'Green'), ('Red', 'Blue', 'Green', 'Blue'))
    
    # Encoding other variables given in the problem statement
    num_tubes = 3
    capacity = 6

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal 
    # Record the actions required to get to each state in a list; no actions perfomed to reach the initial state
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states 
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # Check of the current state is the goal state
        # The goal state is where each tube only contains balls of 1 single color
        if all(len(set(tube)) <= 1 for tube in state):
            return actions

        # Generate all possible actions from the current state, which inlcudes moving a ball from any of the 3 tubes to another tube
        for from_tube_ind in range(num_tubes):
            for to_tube_ind in range(num_tubes):
                # Check if the new state would be valid, ie from_tube and to_tube must not be the same tube
                # And from_tube must at least have 1 ball to move and the to_tube cannot be at capacity
                if from_tube_ind != to_tube_ind and state[from_tube_ind] and len(state[to_tube_ind]) < capacity:
                    # Generate the new state
                    new_state = [list(tube[:]) for tube in state]
                    # The ball to move is the topmost ball in the from_tube, at index 0
                    ball_to_move = new_state[from_tube_ind].pop(0)
                    # Add the ball tot he top of the to_tube
                    new_state[to_tube_ind].insert(0, ball_to_move)
                    new_state = tuple(tuple(tube) for tube in new_state)
                    # The cost so far is the number of moves made, as the task is to minimize the number of moves required 
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state), g + 1, actions + [(from_tube_ind, to_tube_ind)], new_state))
    return None

def heuristic(tubes):
    # An admissible and consistent heuristic for this problem is the count of balls that are not the same color as the most frequent color in their tube 
    # This heuristic relaxes the constraint that only the ball at the top of the tube can be moved
    # It is admissible because it never overestimates the cost to reach the goal, as each mismatched ball must be moved at least once
    # It's consistent because moving a ball from one tube to another reduces the heuristic cost of the successor node by a max of 1 (if the moved ball's color matches the most common color in the new tube but not in the old one), which is equal to the cost of reaching the successor node 
    # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
    h = 0
    for tube in tubes:
        if tube:
            # If there are ties in the frequency of colors, the most_commonm_color must be match the color of the balls lower that are in the tube, as moving lower balls is costlier           
            reversed_tube = tube[:]
            reversed_tube = reversed_tube[::-1]
            # Get the most common color
            most_common_color = Counter(reversed_tube).most_common(1)[0][0]
            for ball in tube:
                if ball != most_common_color:
                    h += 1
    return h

print(a_star())

