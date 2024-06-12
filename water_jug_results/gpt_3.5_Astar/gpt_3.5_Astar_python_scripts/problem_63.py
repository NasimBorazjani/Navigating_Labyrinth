
import heapq
import math


def a_star():
    # Define the initial state of the buckets, where each bucket is represented by a tuple (current amount of water, maximum capacity)
    initial_state = ((0, 276), (0, 277), (0, 355), (0, 425))
    goal_state = ((276, 276), (277, 277), (355, 355), (425, 425))

    # Encoding other variables given in the problem statement
    jugs = [123, 124, 133, 85, 74]
    num_buckets = 4

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        if state == goal_state:
            return actions

        for i in range(len(jugs)):
            for j in range(num_buckets):
                new_state = list(state)
                # Fill the bucket j with the jug i
                if new_state[j][0] + jugs[i] <= new_state[j][1]:
                    new_state[j] = (new_state[j][0] + jugs[i], new_state[j][1])
                    new_state = tuple(new_state)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jugs[i], j + 1)], new_state))

                # Empty the bucket j using the jug i
                if new_state[j][0] - jugs[i] >= 0:
                    new_state[j] = (new_state[j][0] - jugs[i], new_state[j][1])
                    new_state = tuple(new_state)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jugs[i], j + 1)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the absolute differences between the current and goal water levels in each bucket
    # The heuristic relaxes the constraint that the buckets must be filled in ascending order, as it presumes we can move water between buckets freely
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving water from one bucket to another is always 1, which is exactly the decrease in the absolute difference between the current and goal water levels
    # The cost of the goal state is 0, as the water levels in each bucket match the goal state
    h = sum(abs(state[i][0] - goal[i][0]) for i in range(len(state)))
    return h


print(a_star())
