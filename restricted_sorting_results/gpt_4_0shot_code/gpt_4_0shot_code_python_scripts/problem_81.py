
import heapq

def solve(stacks, costs):
    moves = []
    heap = [(0, stacks, [])]
    visited = set()

    while heap:
        cost, stacks, path = heapq.heappop(heap)
        state = tuple(tuple(stack) for stack in stacks)

        if state in visited:
            continue
        visited.add(state)

        if all(len(set(stack)) <= 1 for stack in stacks if stack):
            return path

        for i, stack in enumerate(stacks):
            if stack:
                for j, target in enumerate(stacks):
                    if i != j and (not target or target[-1] == stack[-1]) and len(target) < 7:
                        new_stacks = [list(s) for s in stacks]
                        new_stacks[j].append(new_stacks[i].pop())
                        new_path = path + [(i, j)]
                        new_cost = cost + costs[j]
                        heapq.heappush(heap, (new_cost, new_stacks, new_path))

    return []

stacks = [[], ['White', 'Black', 'Yellow', 'Black', 'Green', 'Blue', 'Pink'], ['Black', 'Red', 'Yellow', 'White', 'Yellow', 'Black', 'Green'], ['Yellow', 'White', 'Green', 'White', 'White', 'Black', 'Blue'], ['Blue', 'Pink', 'Red', 'Pink', 'Green', 'Yellow', 'Black'], ['White', 'Red', 'Pink', 'Blue', 'Blue', 'Pink', 'Green'], [], [], [], ['Red', 'Pink', 'Red', 'Blue', 'Red', 'Green', 'Yellow'], [], []]
costs = {0: 5, 1: 3, 2: 3, 3: 4, 4: 2, 5: 2, 6: 12, 7: 9, 8: 5, 9: 11, 10: 11, 11: 10}

print(solve(stacks, costs))
