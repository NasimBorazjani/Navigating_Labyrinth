
import heapq

def initialize():
    jugs = [76, 135, 134, 19, 10, 30]
    buckets = [390, 420, 439]
    num_jugs = len(jugs)
    num_buckets = len(buckets)
    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0
    queue = [(0, 0, [], (0, 0, 0))]
    return (jugs, buckets, num_jugs, num_buckets, visited_costs, queue)

def a_star():
    (jugs, buckets, num_buckets, num_jugs, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        if (state[:num_buckets] == tuple(buckets)):
            return actions
        for i in range(num_jugs):
            for j in range(num_buckets):
                new_state = list(state)
                new_state[j] = min(buckets[j], (new_state[j] + jugs[i]))
                if all(((new_state[k] <= new_state[(k + 1)]) for k in range((num_buckets - 1)))):
                    new_state = tuple(new_state)
                    new_cost = (g + jugs[i])
                    if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, ((g + 1), new_cost, (actions + [('+', jugs[i], (j + 1))]), new_state))
                new_state = list(state)
                new_state[j] = 0
                if all(((new_state[k] <= new_state[(k + 1)]) for k in range((num_buckets - 1)))):
                    new_state = tuple(new_state)
                    new_cost = (g + jugs[i])
                    if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, ((g + 1), new_cost, (actions + [('-', jugs[i], (j + 1))]), new_state))
    return None
print(a_star())
