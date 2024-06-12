
import heapq

def solve(stacks):
    costs = {0: 11, 1: 5, 2: 9, 3: 5, 4: 2, 5: 2, 6: 6, 7: 6, 8: 6, 9: 2}
    moves = {tuple(map(tuple, stacks)): (0, [])}
    queue = [(0, stacks)]

    while queue:
        cost, stacks = heapq.heappop(queue)
        if all(len(set(stack)) <= 1 for stack in stacks):
            return moves[tuple(map(tuple, stacks))][1]
        for i, stack in enumerate(stacks):
            if stack:
                for j, target in enumerate(stacks):
                    if i != j and (not target or target[-1] == stack[-1]) and len(target) < 6:
                        new_stacks = [list(s) for s in stacks]
                        new_stacks[j].append(new_stacks[i].pop())
                        new_cost = cost + costs[j]
                        if tuple(map(tuple, new_stacks)) not in moves or moves[tuple(map(tuple, new_stacks))][0] > new_cost:
                            moves[tuple(map(tuple, new_stacks))] = (new_cost, moves[tuple(map(tuple, stacks))][1] + [(i, j)])
                            heapq.heappush(queue, (new_cost, new_stacks))
    return None
