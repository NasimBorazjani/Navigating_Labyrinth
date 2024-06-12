
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (385, 387, 491)
    # Define the capacities of the jugs
    jugs = [149, 128, 67, 43, 55, 38, 129]
    # Define the capacities of the buckets
    buckets = [385, 387, 491]

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
            for bucket_num in range(3):
                # Fill the bucket
                new_state = list(state)
                new_state[bucket_num] = min(buckets[bucket_num], new_state[bucket_num] + jug)
                # Check if the new state is valid
                if new_state[bucket_num] <= buckets[bucket_num] and new_state[bucket_num] <= new_state[bucket_num + 1]:
                    new_state = tuple(new_state)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        if jug in jugs:
                            actions.append(('+', jug, bucket_num + 1))
                        else:
                            actions.append(('-', jug, bucket_num + 1))
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions[:], new_state))
                        actions.pop()

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal state for each bucket
    # The heuristic relaxes the constraint that the buckets must be filled in a specific order and that the jugs must be used in a specific order
    # It is admissible because the sum of the differences is always less than or equal to the actual cost to reach the goal state
    # It is consistent because the cost of moving from one state to a successor state is always greater than or equal to the difference in the heuristic estimate between the two states
    return sum(abs(s - g) for s, g in zip(state, goal))


print(a_star())
