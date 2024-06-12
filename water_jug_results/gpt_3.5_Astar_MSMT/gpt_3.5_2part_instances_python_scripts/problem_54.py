
import heapq

def initialize():
    jugs = [45, 67, 134, 133, 86, 66, 107, 94, 124, 122]
    buckets = [229, 303, 307]
    num_buckets = len(buckets)
    num_jugs = len(jugs)
    visited_costs = {}
    visited_costs[(('47', 'x', 'x', '32'), ('x', 'x', 'x', '49'), ('x', '31', '50', 'x'), ('x', 'x', '52', '30'))] = 0
    queue = [(0, 0, [], (('47', 'x', 'x', '32'), ('x', 'x', 'x', '49'), ('x', '31', '50', 'x'), ('x', 'x', '52', '30')))]
    return (jugs, buckets, num_buckets, num_jugs, visited_costs, queue)

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