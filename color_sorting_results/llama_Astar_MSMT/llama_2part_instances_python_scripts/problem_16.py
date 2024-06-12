
import heapq

def initialize():
    initial_state = (('Red', 'Green', 'Green', 'Blue'), ('Red', 'Green', 'Red', 'Blue'), ('Blue', 'Red', 'Green', 'Blue'))
    num_tubes = 3
    capacity = 6
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [], initial_state)]
    return (initial_state, num_tubes, capacity, visited_costs, queue)

def a_star():
    (initial_state, num_tubes, max_capacity, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        if all(((len(set(tube)) == 1) for tube in state)):
            return actions
        for from_tube in range(num_tubes):
            for to_tube in range(num_tubes):
                if ((from_tube != to_tube) and (len(state[from_tube]) > 0) and (len(state[to_tube]) < max_capacity)):
                    new_state = [list(tube[:]) for tube in state]
                    new_state[to_tube].append(new_state[from_tube].pop())
                    new_state = tuple((tuple(tube) for tube in new_state))
                    new_cost = (g + 1)
                    if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state)
                        heapq.heappush(queue, ((new_cost + h), new_cost, (actions + [(from_tube, to_tube)]), new_state))
    return None

def heuristic(state):
    return sum((len(tube) for tube in state if (len(set(tube)) != 1)))
print(a_star())
