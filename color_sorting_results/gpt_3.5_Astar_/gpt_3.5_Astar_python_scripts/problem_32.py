
import heapq


def a_star():
    # Define the initial state of the tubes
    initial_state = [['Green', 'Red', 'Blue', 'Green'], ['Blue', 'Blue', 'Red', 'Blue'], ['Red', 'Red', 'Green', 'Green']]
    goal_state = [['Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Red'], ['Blue', 'Blue', 'Blue', 'Blue']]
    num_tubes = 3

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

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
                    # Check if the move is valid, i.e. the from_tube is not empty and the to_tube is not full
                    if state[from_tube] and len(state[to_tube]) < 7:
                        new_state = [list(tube) for tube in state]
                        ball = new_state[from_tube].pop(0)
                        new_state[to_tube].insert(0, ball)
                        new_state_str = str(new_state)
                        new_cost = g + 1

                        if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                            visited_costs[new_state_str] = new_cost
                            heapq.heappush(queue, (g + 1, new_cost, actions + [(from_tube, to_tube)], new_state))

    return None


print(a_star())
