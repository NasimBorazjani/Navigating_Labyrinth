
import heapq

def initialize():
    # Define the initial state of the board and the target words
    initial_state = [['o', 'm', 'y', 'i'], ['g', 'd', 'o', 'e'], ['_', 'o', 'b', 'd'], ['p', 'o', 'c', 'k']]
    target_words = ['moi', 'good', 'boyd', 'peck']

    # Initialize the visited_costs dictionary and the priority queue
    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    return initial_state, target_words, visited_costs, queue

def a_star():
    initial_state, target_words, visited_costs, queue = initialize()

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == [list(word) for word in target_words]:
            return actions

        # Generate all possible actions from the current state
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == '_':
                    for new_i, new_j in [(i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]:
                        if 0 <= new_i < len(state) and 0 <= new_j < len(state[i]) and state[new_i][new_j] != '_':
                            # Generate the new state
                            new_state = [list(row[:]) for row in state]
                            new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
                            new_state = tuple(tuple(row) for row in new_state)
                            # The cost so far is the number of actions taken
                            new_cost = g + 1

                            if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                                visited_costs[new_state] = new_cost
                                # The heuristic is the number of characters in the current state that are not in their correct position in the goal state
                                h = heuristic(state, target_words)
                                heapq.heappush(queue, (new_cost + h, new_cost, actions + [(i, j, new_i, new_j)], new_state))

    return None

def heuristic(state, target_words):
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != target_words[i][j - (i > 0)]:
                h += 1
    return h

print(a_star())
