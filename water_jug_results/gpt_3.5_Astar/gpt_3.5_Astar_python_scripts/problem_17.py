
import heapq


def a_star():
    # Define the initial state of the problem, where all buckets are empty
    initial_state = (0, 0, 0)
    # Define the goal state where the buckets are filled with 398, 440, 440 liters of water respectively
    goal_state = (398, 440, 440)
    # Define the capacities of the water jugs
    jugs = [143, 117, 116, 103, 84, 87]
    
    visited_costs = {}
    visited_costs[initial_state] = 0
    
    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    queue = [(0, 0, [], initial_state)]
    
    while queue:
        _, g, actions, state = heapq.heappop(queue)
        
        # Check if the current state is the goal state
        if state == goal_state:
            return actions
        
        # Generate all possible actions from the current state, which includes filling and emptying the unlabeled buckets using the water jugs
        for jug in jugs:
            for i in range(3):
                new_state = list(state)
                # Fill the ith bucket with the jug
                if actions and actions[-1][2] == i:
                    continue
                if actions and actions[-1][0] == '+' and actions[-1][1] == jug:
                    continue
                if actions and actions[-1][0] == '-' and actions[-1][1] == jug:
                    continue
                if new_state[i] + jug <= goal_state[i] and new_state[i] + jug <= new_state[i+1]:
                    new_state[i] += jug
                    new_state = tuple(new_state)
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + 1, new_cost, actions + [('+', jug, i)], new_state))
                
                # Empty the ith bucket using the jug
                if new_state[i] - jug >= 0 and new_state[i] - jug <= new_state[i+1]:
                    new_state[i] -= jug
                    new_state = tuple(new_state)
                    new_cost = g + 1
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + 1, new_cost, actions + [('-', jug, i)], new_state))
    
    return None


print(a_star())
