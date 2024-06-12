
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

        if is_sorted(stacks):
            return path

        for i in range(8):
            if not stacks[i]:
                continue
            for j in range(8):
                if i != j and (not stacks[j] or stacks[j][-1] == stacks[i][-1]) and len(stacks[j]) < 5:
                    new_stacks = [list(stack) for stack in stacks]
                    block = new_stacks[i].pop()
                    new_stacks[j].append(block)
                    new_cost = cost + costs[j]
                    new_path = path + [(i, j)]
                    heapq.heappush(heap, (new_cost, new_stacks, new_path))

    return []

def is_sorted(stacks):
    for stack in stacks:
        if len(set(stack)) > 1:
            return False
    return True

stacks = [[], ['Green', 'Yellow', 'Blue', 'Yellow', 'Green'], ['Black', 'Yellow', 'Blue', 'Green', 'Red'], ['Red', 'Black', 'Blue', 'Red', 'Black'], [], ['Red', 'Green', 'Yellow', 'Black', 'Blue'], [], []]
costs = {0: 8, 1: 8, 2: 2, 3: 7, 4: 9, 5: 5, 6: 2, 7: 7}
print(restricted_sorting(stacks, costs))
