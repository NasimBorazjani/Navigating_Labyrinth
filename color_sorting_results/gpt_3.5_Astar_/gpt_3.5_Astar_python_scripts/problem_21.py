
import heapq


def a_star():
    # Define the initial state of the tubes
    initial_state = [['Green', 'Red', 'Blue', 'Green'], ['Red', 'Blue', 'Red', 'Blue'], ['Red', 'Blue', 'Green', 'Green']]
    goal_state = [['Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Red'], ['Blue', 'Blue', 'Blue', 'Blue']]
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
                if i != j:
                    # Check if moving a ball from tube i to tube j is valid
                    if state[i] and len(state[j]) < 6 and (not state[j] or state[i][-1] == state[j][-1]):
                        new_state = [list(tube) for tube in state]
                        new_state[j].append(new_state[i].pop())
                        new_state_str = str(new_state)
                        new_cost = g + 1

                        if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                            visited_costs[new_state_str] = new_cost
                            heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [(i, j)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the number of balls not in the correct position
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != goal[i][j]:
                h += 1
    return h


print(a_star())
