
import heapq
import math


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0)
    # Define the goal state where the buckets are filled to the specified amounts
    goal_state = (215, 219, 262)
    # Define the capacities of the water jugs
    jugs = [14, 46, 13, 110, 38, 21, 45, 130]
    # Define the capacities of the unlabeled buckets
    buckets = [215, 219, 262]
    # Define the number of buckets
    num_buckets = 3

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
            for bucket in range(num_buckets):
                # Fill the bucket with water from the jug
                new_state = list(state)
                new_state[bucket] += jug
                # Check if the new state is valid, i.e., the amount of water in each bucket does not exceed its capacity
                if all(new_state[i] <= buckets[i] for i in range(num_buckets)):
                    new_state = tuple(new_state)
                    # Calculate the cost of the new state
                    new_cost = g + 1
                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug, bucket + 1)], new_state))

                # Empty the bucket
                new_state = list(state)
                new_state[bucket] = 0
                new_state = tuple(new_state)
                # Calculate the cost of the new state
                new_cost = g + 1
                # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug, bucket + 1)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the differences between the current water levels in the buckets and the goal water levels
    # The heuristic relaxes the constraint that the unlabeled buckets cannot be overfilled, presuming we can always empty the buckets to reach the goal state
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of adding or removing water from a bucket is always 1, which is exactly the decrease in the heuristic estimate if the water level is moved towards the goal level
    return sum(abs(state[i] - goal[i]) for i in range(len(state)))


print(a_star())
