
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (245, 252, 264, 314)
    # Define the capacities of the water jugs
    jugs = [19, 42, 18, 127, 106, 32, 22, 137]
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

        # Generate all possible actions from the current state
        for jug in jugs:
            for i in range(num_buckets):
                # Fill the ith bucket with the jug
                new_state = list(state)
                new_state[i] = min(state[i] + jug, goal_state[i])
                # Check if the new state is valid
                if new_state[i] >= state[i]:
                    new_state = tuple(new_state)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug, i+1)], new_state))

                # Empty the ith bucket
                new_state = list(state)
                new_state[i] = 0
                new_state = tuple(new_state)
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug, i+1)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal state for each bucket
    # The heuristic relaxes the constraint that the buckets cannot be overfilled, as it assumes we can always empty the buckets if needed
    # It is admissible because it never overestimates the cost to reach the goal state, as the sum of the differences is always less than or equal to the actual cost
    # It is consistent because the cost of moving water from one bucket to another is always 1, which is exactly the decrease in the heuristic estimate
    return sum(abs(s - g) for s, g in zip(state, goal))


print(a_star())
