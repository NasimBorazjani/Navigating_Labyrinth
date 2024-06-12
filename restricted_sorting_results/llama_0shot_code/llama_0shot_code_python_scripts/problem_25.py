
import heapq

def restricted_sorting(stacks, costs):
    # Helper function to get the most unsorted stack
    def get_most_unsorted_stack(unsorted_stacks):
        max_unsorted_stack = None
        max_unsorted_value = float('-inf')
        for stack in unsorted_stacks:
            colors = set(stack)
            if len(colors) > 1 or len(stack) > 3:
                unsorted_value = len(colors) * len(stack)
                if unsorted_value > max_unsorted_value:
                    max_unsorted_value = unsorted_value
                    max_unsorted_stack = stack
        return max_unsorted_stack

    # Helper function to get the destination stack for a block
    def get_destination_stack(block_color, stacks, costs):
        for i, stack in enumerate(stacks):
            if not stack or stack[-1] == block_color:
                return i
        return len(stacks)

    # Initialize the unsorted stacks
    unsorted_stacks = [stack for stack in stacks if stack]

    # Initialize the result
    result = []

    # While there are still blocks that need to be sorted
    while unsorted_stacks:
        # Get the most unsorted stack
        sorted_stack = get_most_unsorted_stack(unsorted_stacks)
        # Get the destination stack for the block that needs to be moved
        destination_stack = get_destination_stack(sorted_stack[-1], stacks, costs)
        # Move the block from the sorted stack to the destination stack
        result.append((unsorted_stacks.index(sorted_stack), destination_stack))
        heapq.heapify(stacks)
        # If the sorted stack is now sorted, then remove it from the set of unsorted stacks
        if len(set(sorted_stack)) <= 1 and len(sorted_stack) <= 3:
            unsorted_stacks.remove(sorted_stack)

    return result

stacks = [[], ['Green', 'Blue', 'Yellow', 'Green'], ['Yellow', 'Red', 'Red', 'Blue'], [], ['Blue', 'Green', 'Yellow', 'Red'], []]
costs = [4, 3, 2, 4, 2, 5]
print(restricted_sorting(stacks, costs))
