
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (256, 399, 410)
    # Define the capacities of the water jugs
    jugs = [19, 122, 104, 145, 38, 141, 126, 82, 37, 33]

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes filling or emptying each bucket using each jug
        for jug in jugs:
            for i in range(3):
                new_state = list(state)
                # Fill the ith bucket with the jug
                if actions and actions[-1][2] == i and actions[-1][0] == '+':
                    continue
                if actions and actions[-1][2] == i and actions[-1][0] == '-':
                    continue
                if state[i] + jug <= goal_state[i] and state[i] + jug <= state[i+1]:
                    new_state[i] += jug
                    new_state = tuple(new_state)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug, i)], new_state))

                # Empty the ith bucket using the jug
                if state[i] - jug >= 0 and state[i] - jug <= state[i+1]:
                    new_state = list(state)
                    new_state[i] -= jug
                    new_state = tuple(new_state)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug, i)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal state for each bucket
    # The heuristic relaxes the constraint that the unlabeled buckets cannot be overfilled, as it presumes we can always empty the buckets to reach the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of filling or emptying a bucket is always 1, which is exactly the decrease in the absolute difference between the current and goal state
    # The cost of the goal state is 0, as the buckets are filled to the specified amounts
    h = sum(abs(state[i] - goal[i]) for i in range(3))
    return h


print(a_star())
