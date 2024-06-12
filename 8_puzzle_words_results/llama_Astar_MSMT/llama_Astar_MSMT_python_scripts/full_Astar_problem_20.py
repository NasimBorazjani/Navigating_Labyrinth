
import heapq


def initialize():
    # Define the initial state of the board and the target words
    initial_state = [['r', 's', 'w', 'o', 'g'], ['t', 'n', 'e', 'm', 'a'], ['m', 'o', '_', 'u', 's'], ['a', 'w', 'i', 'r', 'i']]
    target_words = ['snog', 'trema', 'mosur', 'awiwi']

    # Define the dimensions of the board
    num_rows = 4
    num_cols = 5

    # Initialize the visited_costs dictionary and the priority queue
    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    return initial_state, num_rows, num_cols, target_words, visited_costs, queue


def a_star():
    initial_state, num_rows, num_cols, target_words, visited_costs, queue = initialize()

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == target_words:
            return actions

        # Generate all possible actions from the current state
        for row in range(num_rows):
            for col in range(num_cols):
                for new_row in range(num_rows):
                    for new_col in range(num_cols):
                        # Check if the new state would be valid, ie the blank tile can only move to a diagonal neighbor
                        if (row != new_row or col != new_col) and (abs(row - new_row) == abs(col - new_col)):
                            # Generate the new state
                            new_state = [list(row[:]) for row in state]
                            new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
                            new_state = tuple(tuple(row) for row in new_state)
                            # The cost so far is the number of swaps made, as the task is to minimize the number of swaps required
                            new_cost = g + 1

                            # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                            if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                                visited_costs[new_state] = new_cost
                                h = heuristic(state, target_words)
                                # In the problem statement the directions are indexed starting from 1, thus must add 1 to the direction indices
                                heappush(queue, (new_cost + h, new_cost, actions + [(row, col, new_row, new_col)], new_state))

    return None


def heuristic(state, target_words):
    # The heuristic function can be a count of the number of characters in the current state that are not in their correct positions in the target words
    # This heuristic is admissible because it never overestimates the cost to reach the goal
    # The heuristic is consistent as the estimated cost of the next node is higher if a character is moved away from its correct position, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number of characters that can be moved to their correct positions in the heuristic is by moving the blank tile to the correct position, which is exactly the character used to fill the blank tile in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != '_' and state[i][j] != target_words[i][j - (i > 0)]:
                h += 1
    return h


print(a_star())
