
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (278, 295, 323, 383)
    # Define the capacities of the water jugs
    jug_capacities = [73, 129, 120, 38, 72, 138]
    # Define the number of buckets
    num_buckets = 4

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes filling and emptying the buckets using the water jugs
        for i in range(len(jug_capacities)):
            for j in range(num_buckets):
                # Fill the jth bucket using the ith jug
                new_state = list(state)
                new_state[j] = min(state[j] + jug_capacities[i], goal_state[j])
                # Check if the new state is valid
                if new_state[j] >= state[j]:
                    new_state = tuple(new_state)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug_capacities[i], j+1)], new_state))

                # Empty the jth bucket using the ith jug
                new_state = list(state)
                new_state[j] = 0
                new_state = tuple(new_state)
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug_capacities[i], j+1)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal state for each bucket
    # The heuristic relaxes the constraint that the buckets must be filled in ascending order, as it presumes we can move water between buckets freely
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving water from one bucket to another is always 1, which is exactly the decrease in the absolute difference between the current and goal state
    h = sum(abs(state[i] - goal[i]) for i in range(len(state)))
    return h


print(a_star())
