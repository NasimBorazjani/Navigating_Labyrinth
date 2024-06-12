
import heapq

def initialize():
    initial_state = (('Red', 'Red', 'Blue', 'Green'), ('Blue', 'Red', 'Blue', 'Green'), ('Blue', 'Green', 'Red', 'Green'))
    goal_state = (('Red', 'Red', 'Red', 'Red'), ('Blue', 'Blue', 'Blue', 'Blue'), ('Green', 'Green', 'Green', 'Green'))
    num_tubes = 3
    tube_capacity = 6
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [], initial_state)]
    return (initial_state, goal_state, num_tubes, tube_capacity, visited_costs, queue)

def a_star():
    (initial_state, goal_state, num_tubes, tube_capacity, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        if (state == goal_state):
            return actions
        for from_tube in range(num_tubes):
            for to_tube in range(num_tubes):
                if (state[from_tube] and (len(state[to_tube]) < tube_capacity)):
                    new_state = [list(tube[:]) for tube in state]
                    ball_to_be_moved = new_state[from_tube].pop(0)
                    new_state[to_tube].insert(0, ball_to_be_moved)
                    new_state = tuple((tuple(tube) for tube in new_state))
                    new_cost = (g + 1)
                    if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, ((g + heuristic(new_state, goal_state)), new_cost, (actions + [(from_tube, to_tube)]), new_state))
    return None

def heuristic(state, goal):
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if (state[i][j] != '_'):
                h += sum((1 for ball in state[i] if (ball != goal[i][0])))
    return h
print(a_star())
