
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0)
    # Define the goal state where the buckets are filled with 284, 297, and 436 liters of water respectively
    goal_state = (284, 297, 436)
    # Define the capacities of the water jugs
    jug_capacities = [43, 149, 131, 132, 70, 104]
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
        for jug in jug_capacities:
            for bucket in range(num_buckets):
                # Check if the action is valid, ie the water jug has enough water to fill or empty the bucket
                if (jug >= state[bucket] and
                        (bucket == num_buckets - 1 or state[bucket] + jug <= state[bucket + 1])):
                    # Generate the new state after performing the action
                    new_state = list(state)
                    new_state[bucket] = jug if state[bucket] == 0 else 0
                    new_state = tuple(new_state)
                    # Calculate the cost of the new state, which is the amount of water added or removed
                    new_cost = g + jug

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug, bucket + 1)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the differences between the current and goal water levels in each bucket
    # The heuristic relaxes the constraint that the buckets must be filled in ascending order, as it presumes we can move water between buckets freely
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving water from one bucket to another is the amount of water moved, which is exactly the decrease in the difference between the current and goal water levels
    # The cost of the goal state is 0, as the water levels in the buckets match the goal state

    h = sum(abs(state[i] - goal[i]) for i in range(len(state)))
    return h


print(a_star())
