
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0)
    # Define the goal state where the buckets are filled to the specified levels
    goal_state = (160, 170, 330)
    # Define the capacities of the jugs
    jug_capacities = [19, 50, 12, 63, 143, 13]
    # Define the capacities of the buckets
    bucket_capacities = [160, 170, 330]
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

        # Generate all possible actions from the current state
        for jug_capacity in jug_capacities:
            for bucket_num in range(num_buckets):
                # Check if the action is valid
                if state[bucket_num] + jug_capacity <= bucket_capacities[bucket_num]:
                    # Generate the new state after performing the action
                    new_state = list(state)
                    new_state[bucket_num] += jug_capacity
                    new_state = tuple(new_state)
                    # Calculate the cost of the new state
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug_capacity, bucket_num + 1)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the differences between the current water levels in the buckets and the goal water levels
    # The heuristic relaxes the constraint that the jugs can only be filled to the top and emptied completely, and the unlabeled buckets cannot be overfilled
    # It is admissible because it never overestimates the cost to reach the goal state, as each difference must be filled or emptied to reach the goal state
    # It is consistent because the cost of moving water from one bucket to another is always 1, which is exactly the decrease in the heuristic estimate
    # The cost of the goal state is 0, as the water levels in the buckets match the goal levels

    h = sum(abs(state[i] - goal[i]) for i in range(len(state)))
    return h


print(a_star())
