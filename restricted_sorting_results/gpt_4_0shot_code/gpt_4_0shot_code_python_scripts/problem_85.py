
import heapq

def restricted_sorting(stacks, costs):
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

stacks = [
    ['Pink', 'Red', 'Black', 'Green', 'Yellow', 'Yellow', 'Pink'],
    [],
    [],
    ['Pink', 'White', 'Yellow', 'Blue', 'Green', 'Blue', 'Black'],
    ['Black', 'Blue', 'Red', 'Pink', 'Yellow', 'Yellow', 'Blue'],
    [],
    ['White', 'Black', 'Yellow', 'Green', 'Red', 'Green', 'Green'],
    [],
    [],
    ['Pink', 'Red', 'Black', 'White', 'White', 'Red', 'White'],
    ['Blue', 'Green', 'Pink', 'Blue', 'White', 'Red', 'Black'],
    []
]
costs = {0: 8, 1: 5, 2: 4, 3: 12, 4: 9, 5: 9, 6: 3, 7: 2, 8: 11, 9: 9, 10: 3, 11: 2}

print(restricted_sorting(stacks, costs))
