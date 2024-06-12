
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (307, 316, 325, 622)
    # Define the capacities of the water jugs
    jug_capacities = [143, 34, 117, 130, 50, 142, 144, 150, 29, 78]
    # Define the number of buckets
    num_buckets = 4

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If the current state is the goal state, return the sequence of actions
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes filling or emptying each bucket using the water jugs
        for jug in jug_capacities:
            for i in range(num_buckets):
                new_state = list(state)
                # Fill the bucket
                if state[i] + jug <= goal_state[i] and state[i] + jug <= state[i+1]:
                    new_state[i] += jug
                    new_cost = g + 1
                    new_state = tuple(new_state)

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug, i+1)], new_state))

                # Empty the bucket
                if state[i] - jug >= 0 and state[i] - jug <= state[i+1]:
                    new_state = list(state)
                    new_state[i] -= jug
                    new_cost = g + 1
                    new_state = tuple(new_state)

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug, i+1)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal state for each bucket
    # The heuristic relaxes the constraint that the unlabeled buckets cannot be overfilled, as it assumes we can always empty the buckets to reach the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving water from one bucket to another is always 1, which is exactly the decrease in the absolute difference between the current and goal state
    # The cost of the goal state is 0, as the buckets are filled to the specified amounts
    h = sum(abs(state[i] - goal[i]) for i in range(len(state)))
    return h


print(a_star())
