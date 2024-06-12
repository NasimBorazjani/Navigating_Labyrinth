
import heapq

def initialize():
    initial_state = [['Red', 'Green', 'Red', 'Blue', 'Green'], ['Red', 'Blue', 'Green', 'Blue', 'Blue'], ['Green', 'Red', 'Red', 'Green', 'Blue']]
    num_tubes = 3
    visited_costs = {}
    visited_costs[str(initial_state)] = 0
    queue = [(0, 0, [], initial_state)]
    return (initial_state, num_tubes, visited_costs, queue)

def a_star():
    (initial_state, num_tubes, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        if all(((len(set(tube)) == 1) for tube in state)):
            return actions
        for i in range(num_tubes):
            for j in range(num_tubes):
                if ((i != j) and (len(state[j]) < 6) and state[i]):
                    new_state = [list(tube) for tube in state]
                    new_state[j].append(new_state[i].pop())
                    new_state = [tuple(tube) for tube in new_state]
                    new_state_key = str(new_state)
                    new_cost = (g + 1)
                    if ((new_state_key not in visited_costs) or (new_cost < visited_costs[new_state_key])):
                        visited_costs[new_state_key] = new_cost
                        h = heuristic(new_state)
                        heapq.heappush(queue, ((g + h), new_cost, (actions + [(i, j)]), new_state))
    return None

def heuristic(state):
    h = 0
    for tube in state:
        for i in range((len(tube) - 1)):
            if (tube[i] != tube[(i + 1)]):
                h += 1
    return h
print(a_star())
