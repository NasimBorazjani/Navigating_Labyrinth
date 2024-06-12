
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

stacks = [[], ['Black', 'Green', 'White', 'Pink', 'Yellow', 'Blue', 'Red'], [], ['Green', 'Red', 'Red', 'Red', 'White', 'Black', 'Black'], [], ['Blue', 'Blue', 'Pink', 'Yellow', 'Pink', 'Green', 'Red'], ['Blue', 'Black', 'White', 'Green', 'White', 'Yellow', 'Yellow'], ['White', 'Blue', 'Pink', 'Green', 'Yellow', 'Green', 'Pink'], [], ['Yellow', 'Black', 'White', 'Red', 'Blue', 'Black', 'Pink'], [], []]
costs = {0: 10, 1: 8, 2: 12, 3: 3, 4: 5, 5: 11, 6: 5, 7: 12, 8: 3, 9: 3, 10: 11, 11: 6}

print(restricted_sorting(stacks, costs))
