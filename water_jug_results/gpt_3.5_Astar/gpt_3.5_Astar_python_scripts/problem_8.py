
import heapq


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0)
    # Define the goal state where the buckets are filled with 196, 210, and 238 liters of water respectively
    goal_state = (196, 210, 238)
    # Define the capacities of the water jugs
    jug_capacities = [59, 68, 104, 106, 69, 42]
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
        for jug_capacity in jug_capacities:
            for bucket_num in range(num_buckets):
                # Fill the bucket with water from the jug
                new_state = list(state)
                new_state[bucket_num] = min(state[bucket_num] + jug_capacity, goal_state[bucket_num])
                # Check if the new state is valid, i.e., the water in each bucket does not exceed the capacity of the next bucket
                if all(new_state[i] <= new_state[i+1] for i in range(num_buckets-1)):
                    new_state = tuple(new_state)
                    # Calculate the cost of the new state
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of unvisited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        if state[bucket_num] < new_state[bucket_num]:
                            actions.append(('+', jug_capacity, bucket_num+1))
                        else:
                            actions.append(('-', jug_capacity, bucket_num+1))
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions[:], new_state))
                        actions.pop()

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the differences between the current water levels in the buckets and the goal water levels
    # The heuristic relaxes the constraint that the water jugs can only be filled to the top and emptied completely
    # It is admissible because it never overestimates the cost to reach the goal state, as each difference must be filled or emptied at least once
    # It is consistent because the cost of moving water from one bucket to another is always 1, which is exactly the decrease in the heuristic estimate
    return sum(abs(state[i] - goal[i]) for i in range(len(state)))


print(a_star())
