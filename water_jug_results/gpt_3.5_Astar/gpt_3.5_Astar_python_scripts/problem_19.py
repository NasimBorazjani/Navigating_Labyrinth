
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (280, 338, 353)
    # Define the capacities of the water jugs
    jugs = [21, 62, 98, 143, 61, 110, 140, 40]
    # Define the number of buckets
    num_buckets = 3

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes filling and emptying the buckets using the water jugs
        for jug in jugs:
            for i in range(num_buckets):
                new_state = list(state)
                # Fill the bucket
                if state[i] + jug <= goal_state[i] and state[i] + jug <= state[i+1]:
                    new_state[i] += jug
                    new_state = tuple(new_state)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug, i+1)], new_state))

                # Empty the bucket
                if state[i] - jug >= 0 and state[i] - jug <= state[i+1]:
                    new_state = list(state)
                    new_state[i] -= jug
                    new_state = tuple(new_state)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug, i+1)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal state for each bucket
    # The heuristic relaxes the constraint that the buckets cannot be overfilled, as it presumes we can move water between buckets without exceeding the goal amounts
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving water between buckets is always 1, which is exactly the decrease in the absolute difference between the current and goal state
    # The cost of the goal state is 0, as the buckets are filled to the specified amounts
    h = sum(abs(state[i] - goal[i]) for i in range(len(state)))
    return h


print(a_star())