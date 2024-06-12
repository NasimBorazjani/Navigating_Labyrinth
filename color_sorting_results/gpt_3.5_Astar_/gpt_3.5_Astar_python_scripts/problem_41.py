
import heapq


def a_star():
    # Define the initial state of the tubes
    initial_state = (['Green', 'Blue', 'Red', 'Blue'], ['Red', 'Green', 'Blue', 'Green'], ['Red', 'Blue', 'Green', 'Red'])
    goal_state = (['Red', 'Red', 'Red', 'Red'], ['Green', 'Green', 'Green', 'Green'], ['Blue', 'Blue', 'Blue', 'Blue'])
    num_tubes = 3

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = []
    # No actions taken in the initial state
    heapq.heappush(queue, (0, 0, [], initial_state))

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If the state is the goal state, return the actions taken
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving a ball from one tube to another
        for from_tube in range(num_tubes):
            for to_tube in range(num_tubes):
                if from_tube != to_tube:
                    new_state = [list(tube) for tube in state]
                    if new_state[from_tube]:
                        ball = new_state[from_tube].pop(0)
                        if len(new_state[to_tube]) < 7:
                            new_state[to_tube].insert(0, ball)
                            new_state = tuple(tuple(tube) for tube in new_state)
                            new_cost = g + 1

                            if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                                visited_costs[new_state] = new_cost
                                heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [(from_tube, to_tube)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the number of balls in each tube that are not in the correct position
    # The heuristic relaxes the constraint that only one ball can be moved at a time and presumes we can move multiple balls to their correct positions in one action
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of moving a ball to the correct position is always 1, which is exactly the decrease in the number of balls not in the correct position
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != goal[i][j]:
                h += 1
    return h


print(a_star())
