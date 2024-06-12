
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (357, 384, 522)
    # Define the capacities of the jugs
    jugs = [52, 131, 82, 132, 117, 65]
    # Define the capacities of the buckets
    buckets = [357, 384, 522]

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state
        for jug in jugs:
            for bucket_num in range(3):
                # Check if the action is valid, i.e. the jug has water and the bucket can hold more water without exceeding the capacity of the next bucket
                if state[bucket_num] + jug <= buckets[bucket_num] and state[bucket_num] + jug <= state[bucket_num + 1]:
                    # Generate the new state after performing the action
                    new_state = list(state)
                    new_state[bucket_num] += jug
                    new_state = tuple(new_state)
                    # Calculate the cost of the new state
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug, bucket_num + 1)], new_state))

        for bucket_num in range(3):
            for jug in jugs:
                # Check if the action is valid, i.e. the bucket has water to be emptied
                if state[bucket_num] - jug >= 0:
                    # Generate the new state after performing the action
                    new_state = list(state)
                    new_state[bucket_num] -= jug
                    new_state = tuple(new_state)
                    # Calculate the cost of the new state
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + ('-', jug, bucket_num + 1), new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal water levels in each bucket
    # The heuristic relaxes the constraint that the unlabeled buckets cannot be overfilled, as it presumes we can always empty the buckets to the desired level
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of adding or removing water from a bucket is always 1, which is exactly the decrease in the absolute difference between the current and goal water levels
    return sum(abs(state[i] - goal[i]) for i in range(3))


print(a_star())
