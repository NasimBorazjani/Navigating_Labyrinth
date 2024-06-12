
import heapq


def a_star():
    # Define the initial state of the tubes
    initial_state = [['Blue', 'Red', 'Red', 'Blue'], ['Green', 'Green', 'Red', 'Red'], ['Green', 'Green', 'Blue', 'Blue']]
    goal_state = [['Blue', 'Blue', 'Blue', 'Blue'], ['Red', 'Red', 'Red', 'Red'], ['Green', 'Green', 'Green', 'Green']]
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
        for i in range(num_tubes):
            for j in range(num_tubes):
                if i != j and state[i] and len(state[j]) < 6:
                    new_state = [list(tube) for tube in state]
                    new_state[j].append(new_state[i].pop())
                    new_state_str = str(new_state)
                    new_cost = g + 1

                    if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                        visited_costs[new_state_str] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [(i, j)], new_state))

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
