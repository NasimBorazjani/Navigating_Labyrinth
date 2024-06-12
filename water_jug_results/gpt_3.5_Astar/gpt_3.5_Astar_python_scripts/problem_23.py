
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0)
    # Define the goal state where the buckets are filled with 226, 258, and 296 liters of water respectively
    goal_state = (226, 258, 296)
    # Define the capacities of the jugs
    jugs = [118, 15, 88, 145, 84, 14, 107, 31]
    # Define the number of buckets
    num_buckets = 3

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the sequence of actions
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state
        for i in range(len(jugs)):
            for j in range(num_buckets):
                # Fill the jth bucket with the ith jug
                new_state = list(state)
                new_state[j] = min(state[j] + jugs[i], goal_state[j])
                # Check if the new state is valid
                if new_state[j] >= state[j]:
                    new_state = tuple(new_state)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jugs[i], j + 1)], new_state))

                # Empty the jth bucket using the ith jug
                new_state = list(state)
                new_state[j] = max(state[j] - jugs[i], 0)
                # Check if the new state is valid
                if new_state[j] <= state[j]:
                    new_state = tuple(new_state)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + ('-', jugs[i], j + 1), new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal state for each bucket
    # The heuristic relaxes the constraint that the jugs can only be filled to the top and emptied completely
    # It is admissible because the sum of the absolute differences is always less than or equal to the actual cost to reach the goal state
    # It is consistent because the cost of moving water from one bucket to another is always 1, which is equal to the decrease in the heuristic estimate
    return sum([abs(state[i] - goal[i]) for i in range(len(state))])


print(a_star())
