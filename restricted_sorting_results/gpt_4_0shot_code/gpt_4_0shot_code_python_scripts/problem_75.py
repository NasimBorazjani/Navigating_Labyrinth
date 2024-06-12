
import heapq

def solve(stacks, costs):
    start = tuple(tuple(stack) for stack in stacks)
    goal = tuple(sorted(stack) for stack in start if stack)
    visited = set()
    queue = [(0, start, [])]
    while queue:
        cost, state, moves = heapq.heappop(queue)
        if state == goal:
            return moves
        if state in visited:
            continue
        visited.add(state)
        for i, stack in enumerate(state):
            if not stack:
                continue
            for j, dest in enumerate(state):
                if i == j or (dest and dest[0] != stack[0]):
                    continue
                new_state = list(state)
                new_state[i] = tuple(stack[1:])
                if dest:
                    new_state[j] = (stack[0],) + dest
                else:
                    new_state[j] = (stack[0],)
                new_state = tuple(new_state)
                new_moves = moves + [(i, j)]
                new_cost = cost + costs[j]
                heapq.heappush(queue, (new_cost, new_state, new_moves))

stacks = [['White', 'Green', 'Red', 'Blue', 'Red', 'Yellow'], ['Black', 'Black', 'White', 'Blue', 'Green', 'Green'], ['White', 'Blue', 'White', 'Yellow', 'Black', 'Green'], [], [], [], [], ['Green', 'Yellow', 'Red', 'White', 'Blue', 'Black'], ['Yellow', 'Red', 'Blue', 'Red', 'Black', 'Yellow'], []]
costs = {0: 8, 1: 8, 2: 10, 3: 6, 4: 8, 5: 4, 6: 3, 7: 7, 8: 11, 9: 9}
print(solve(stacks, costs))
