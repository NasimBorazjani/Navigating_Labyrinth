
import heapq


def a_star():
    # Define the initial state of the tubes
    initial_state = [['Blue', 'Red', 'Red', 'Red'], ['Green', 'Blue', 'Green', 'Green'], ['Blue', 'Blue', 'Green', 'Red']]
    goal_state = [['Red', 'Red', 'Red', 'Red'], ['Green', 'Green', 'Green', 'Green'], ['Blue', 'Blue', 'Blue', 'Blue']]
    num_tubes = 3

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_state))

    while queue:
        _, g, actions, state = heappop(queue)

        # If the state is the goal state, return the actions taken
        if state == goal_state:
            return actions

        # Generate all valid actions from the current state, which includes moving a ball from one tube to another
        for from_tube in range(num_tubes):
            for to_tube in range(num_tubes):
                if from_tube != to_tube:
                    new_state = [list(tube) for tube in state]
                    if new_state[from_tube]:
                        ball = new_state[from_tube].pop(0)
                        if len(new_state[to_tube]) < 7:
                            new_state[to_tube].insert(0, ball)
                            new_state_str = str(new_state)
                            new_cost = g + 1

                            if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                                visited_costs[new_state_str] = new_cost
                                heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [(from_tube, to_tube)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of balls that are not in the correct position
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != goal[i][j]:
                h += 1
    return h


print(a_star())
