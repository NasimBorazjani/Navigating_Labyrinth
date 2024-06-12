import heapq
from collections import Counter
import sys

def a_star(initial_state, capacity):
    initial_state = tuple(tuple(tube) for tube in initial_state)
    num_tubes = len(initial_state)

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue with initial cost and heuristic, cost, actions and state 
    queue = [(0, 0, [], initial_state)]

    while queue:
        # Pop the state with the lowest cost and heuristic sum from the queue
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state
        if all(len(set(tube)) <= 1 for tube in state):
            return actions

        # Generate all possible actions from the current state, which inlcudes moving a ball from any of the tubes to another tube
        for from_tube_ind in range(num_tubes):
            for to_tube_ind in range(num_tubes):
                # Check if the new state would be valid 
                if from_tube_ind != to_tube_ind and state[from_tube_ind] and len(state[to_tube_ind]) < capacity:
                    # Generate the new state
                    new_state = [list(tube[:]) for tube in state]
                    ball_to_move = new_state[from_tube_ind].pop(0)
                    new_state[to_tube_ind].insert(0, ball_to_move)
                    new_state = tuple(tuple(tube) for tube in new_state)
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state), g + 1, actions + [(from_tube_ind, to_tube_ind)], new_state))
    return None

def heuristic(tubes):
    # The heuristic function is the number of balls that are not the same color as the most frequent color in their tube
    h = 0
    for tube in tubes:
        if tube:
            """reversed_tube = tube[:]
            reversed_tube = reversed_tube[::-1]
            # Get the most common color
            # if there are multiple most common colors then return the one that has a ball lower in the tube
            most_common_color = Counter(reversed_tube).most_common(1)[0][0]
            #most_common_color = Counter(tube).most_common(1)[0][0]
            for i in range(len(tube) - 1, -1, -1):
                if tube[i] != most_common_color:
                    h += i + 1
                    break"""
                    
            #most_common_color = Counter(tube).most_common(1)[0][0]
            reversed_tube = tube[:]
            reversed_tube = reversed_tube[::-1]
            # Get the most common color
            # if there are multiple most common colors then return the one that has a ball lower in the tube
            most_common_color = Counter(reversed_tube).most_common(1)[0][0]
            for ball in tube:
                if ball != most_common_color:
                    h += 1
    #print(tubes, h1, h2)        
    return h

import time

def main():
    # Read the initial state from the command line
    initial_state = eval(sys.argv[1])
    capacity = eval(sys.argv[2])
    start = time.time()
    print(a_star(initial_state, capacity))
    end = time.time()
    #print(end - start)

if __name__ == "__main__":
    main()