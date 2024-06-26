
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (191, 269, 328)
    # Define the capacities of the jugs
    jug_capacities = [76, 63, 111, 59, 11, 108, 16, 66, 75, 67]
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

        # Generate all possible actions from the current state, which includes filling or emptying each bucket with each jug
        for jug_capacity in jug_capacities:
            for bucket_num in range(num_buckets):
                # Fill the bucket
                new_state = list(state)
                new_state[bucket_num] = min(state[bucket_num] + jug_capacity, goal_state[bucket_num])
                new_state = tuple(new_state)
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug_capacity, bucket_num + 1)], new_state))

                # Empty the bucket
                new_state = list(state)
                new_state[bucket_num] = 0
                new_state = tuple(new_state)
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug_capacity, bucket_num + 1)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal amounts in each bucket
    # The heuristic relaxes the constraint that the buckets must be filled in ascending order and that the jugs can only be used to fill or empty the buckets
    # It is admissible because it never overestimates the cost to reach the goal state, as the sum of the absolute differences is always less than or equal to the actual cost to reach the goal state
    # It is consistent because the cost of moving water from one bucket to another is always 1, which is exactly the decrease in the heuristic estimate if the water is moved towards the goal amount, otherwise the estimated cost of the successor node is the same or higher
    return sum([abs(state[i] - goal[i]) for i in range(len(state))])


print(a_star())
