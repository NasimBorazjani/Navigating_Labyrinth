
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0)
    # Define the goal state where the buckets are filled with 279, 488, and 578 liters of water respectively
    goal_state = (279, 488, 578)
    # Define the capacities of the water jugs
    jugs = [22, 98, 38, 116, 140, 115, 21, 80, 92, 27]
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

        # Generate all possible actions from the current state, which includes filling or emptying each bucket using the water jugs
        for jug in jugs:
            for bucket in range(num_buckets):
                # Check if the action is valid, ie the jug has enough water to fill or the bucket has water to empty
                if (jug <= state[bucket] or state[bucket] == 0) and (state[bucket] + jug <= goal_state[bucket]):
                    # Generate the new state after performing the action
                    new_state = list(state)
                    new_state[bucket] += jug if state[bucket] + jug <= goal_state[bucket] else goal_state[bucket] - state[bucket]
                    new_state = tuple(new_state)
                    # Calculate the cost of the new state, which is the amount of water added or removed
                    new_cost = g + jug

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug, bucket + 1)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the differences between the current and goal state for each bucket
    # The heuristic relaxes the constraint that the buckets must be filled in ascending order, as it presumes we can move water between buckets freely
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving water from one bucket to another is always greater than or equal to the decrease in the difference between the current and goal state
    return sum(abs(state[i] - goal[i]) for i in range(len(state)))


print(a_star())
