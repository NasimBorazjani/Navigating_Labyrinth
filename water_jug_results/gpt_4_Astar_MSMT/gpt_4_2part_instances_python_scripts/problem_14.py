
import heapq

def initialize():
    initial_state = (0, 0, 0)
    goal_state = (236, 333, 386)
    jug_capacities = [144, 37, 73, 79, 75, 74]
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [], initial_state)]
    return (initial_state, goal_state, jug_capacities, visited_costs, queue)

def a_star():
    (initial_state, goal_state, jug_capacities, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        if (state == goal_state):
            return actions
        for i in range(len(jug_capacities)):
            for j in range(len(state)):
                if (((state[j] + jug_capacities[i]) <= goal_state[j]) and ((j == (len(state) - 1)) or ((state[j] + jug_capacities[i]) <= state[(j + 1)]))):
                    new_state = list(state)
                    new_state[j] += jug_capacities[i]
                    new_state = tuple(new_state)
                    new_cost = (g + 1)
                    if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, ((g + heuristic(new_state, goal_state)), new_cost, (actions + [('+', jug_capacities[i], (j + 1))]), new_state))
                if (((state[j] - jug_capacities[i]) >= 0) and ((j == 0) or ((state[j] - jug_capacities[i]) >= state[(j - 1)]))):
                    new_state = list(state)
                    new_state[j] -= jug_capacities[i]
                    new_state = tuple(new_state)
                    new_cost = (g + 1)
                    if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, ((g + heuristic(new_state, goal_state)), new_cost, (actions + [('-', jug_capacities[i], (j + 1))]), new_state))
    return None

def heuristic(state, goal):
    return sum((abs((a - b)) for (a, b) in zip(state, goal)))
print(a_star())
