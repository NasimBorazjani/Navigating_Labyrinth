
import heapq


def a_star():
    # Define the initial state of the tubes
    initial_state = [['Blue', 'Green', 'Blue', 'Red'], ['Red', 'Green', 'Blue', 'Red'], ['Green', 'Red', 'Green', 'Blue']]
    goal_state = [['Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Red']]
    num_tubes = 3
    tube_capacity = 7

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        if state == goal_state:
            return actions

        for i in range(num_tubes):
            for j in range(num_tubes):
                if i != j:
                    new_state = [list(tube) for tube in state]
                    if new_state[i] and len(new_state[j]) < tube_capacity:
                        ball = new_state[i].pop(0)
                        new_state[j].insert(0, ball)
                        new_state_str = str(new_state)
                        new_cost = g + 1

                        if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                            visited_costs[new_state_str] = new_cost
                            heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [(i, j)], new_state))

    return None


def heuristic(state, goal):
    # The heuristic is the sum of the number of balls in the wrong position in each tube
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != goal[i][j]:
                h += 1
    return h


print(a_star())
