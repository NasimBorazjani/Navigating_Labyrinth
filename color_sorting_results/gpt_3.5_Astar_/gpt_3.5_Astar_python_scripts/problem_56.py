
import heapq


def a_star():
    # Define the initial state of the tubes
    initial_state = [['Green', 'Red', 'Green', 'Blue', 'Red'], ['Red', 'Green', 'Red', 'Blue', 'Blue'], ['Green', 'Blue', 'Red', 'Green', 'Blue']]
    goal_state = [['Green', 'Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Red', 'Red'], ['Blue', 'Blue', 'Blue', 'Blue', 'Blue']]
    num_tubes = 3

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes moving a ball from one tube to another
        for i in range(num_tubes):
            for j in range(num_tubes):
                if i != j:
                    # Check if moving a ball from tube i to tube j is a valid action
                    if state[i] and len(state[j]) < 8:
                        new_state = [list(tube) for tube in state]
                        ball = new_state[i].pop(0)
                        new_state[j].insert(0, ball)
                        new_state = [tuple(tube) for tube in new_state]
                        new_cost = g + 1

                        if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                            visited_costs[str(new_state)] = new_cost
                            heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [(i, j)], new_state))

    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the number of balls in each tube that are not in the correct position
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != goal[i][j]:
                h += 1
    return h


print(a_star())
