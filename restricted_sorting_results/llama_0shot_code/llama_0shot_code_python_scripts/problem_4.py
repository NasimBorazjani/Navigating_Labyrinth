
import heapq

def restricted_sorting(stacks, costs):
    stacks = [list(reversed(stack)) for stack in stacks]
    result = []
    
    while True:
        total_costs = []
        
        for i, stack in enumerate(stacks):
            if stack:
                color = stack[-1]
                min_cost = float('inf')
                dest_stack = None
                
                for j, other_stack in enumerate(stacks):
                    if not other_stack or other_stack[-1] == color:
                        cost = costs[j]
                        if cost < min_cost:
                            min_cost = cost
                            dest_stack = j
                
                if dest_stack is not None:
                    heapq.heappush(total_costs, (min_cost, i, dest_stack))
        
        if not total_costs:
            break
        
        min_cost, src, dest = heapq.heappop(total_costs)
        stacks[dest].append(stacks[src].pop())
        result.append((src, dest))
    
    return result

stacks = [['Red', 'Green', 'Yellow', 'Blue'], [], ['Yellow', 'Green', 'Blue', 'Red'], [], ['Green', 'Red', 'Blue', 'Yellow'], []]
costs = [2, 6, 5, 2, 5, 7]

print(restricted_sorting(stacks, costs))
