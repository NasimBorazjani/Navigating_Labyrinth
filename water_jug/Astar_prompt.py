from heapq import heappush, heappop

def a_star():
    # Define the capacities of the jugs, the goal state, and initial state, with states having an unmutable data type
    jugs = [37, 133, 38, 72, 41, 23, 122]
    goal_state = (195, 224, 268)
    initial_state = (0, 0, 0)
    num_buckets = 3

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = []
    # No actions taken in the initial state
    heappush(queue, (0, 0, [], initial_state))

    while queue:
        _, g, actions, state = heappop(queue)

        # If the amount of water in the buckets in the current state euqal the goal amounts, return the actions taken 
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes adding or subtracting water using any of the 6 jugs to any of the 3 buckets
        # Iterating though capcities of jugs and index of buckets as the action tuples must include the operation ('+' or '-'), capacity of the jug used, and the index of the bucket affected
        for jug in jugs:
            for bucket_ind in range(num_buckets):
                # Check if adding water using the current jug results in a valid state, ie the addition must not result in overflowing any of the buckets
                if (state[bucket_ind] + jug <= goal_state[bucket_ind]):
                    temp_state = list(state)[:]
                    temp_state[bucket_ind] += jug
                    # And the new state must maintain the constraint on the relative amount of water in the buckets based on their order
                    if all(temp_state[i] <= temp_state[i + 1] for i in range(len(temp_state) - 1)):
                        # Generate the new state
                        new_state = tuple(temp_state)
                        # The cost so far is the number of actions taken, as the task is to minimize the number of actions required  to fill the buckets with the designated amount of weater
                        new_cost = g + 1

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            h = heuristic(state, goal_state, jugs)
                            # In the problme statement the buckets are indexed starting from 1, thus must add 1 to the bucket_ind 
                            heappush(queue, (g + h, g + 1,  actions + [('+', jug, bucket_ind+1)], new_state))
                
                # Check if removing water from the bucket results in a valid state. The buckest cannot have a negative amount of water
                if state[bucket_ind] - jug >= 0:
                    temp_state = list(state)[:]
                    temp_state[bucket_ind] -= jug
                    # The constraint on the relative amount of water in the buckets based on their order must hold after this action
                    if all(temp_state[i] <= temp_state[i + 1] for i in range(len(temp_state) - 1)):
                        new_state = tuple(temp_state)
                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            h = heuristic(state, goal_state, jugs)
                            heappush(queue, (g + h, g + 1, actions + [('-', jug, bucket_ind+1)], new_state))
    return None


def heuristic(buckets_state, buckets_goal, jugs):
    # The heuristic function can be a simulation of filling buckets greedily, using the next largest jug repeatedly as long as the amount of water in the bucket does not exceed the goal amount
    # This heuristic is admissible because it is greedy, always opting for the action that fills the buckets the most, ensuring it never overestimates the cost to reach the goal
    # The heuristic is consistent as the estimated cost of the next node is higher if water is removed from a bucket, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount of water that can be added to the bucket is by using the largest jug that won't cause an overflow, which is exactly the jug used to fill the bucket in the heuristic. Thus h(s) is never greater than c(s, n)(equal to 1) + h(n)
    h = 0
    # Sort the jugs by decreasing capacity
    jugs = sorted(jugs, reverse=True)
    # Iterate through the buckets
    for i in range(len(buckets_state)):
        bucket_fill = buckets_state[i]
        goal = buckets_goal[i]
        # Fill the bucket using the next largest jug as long as the bucket does not overflows
        for jug in jugs:
            while bucket_fill + jug < goal:
                bucket_fill += jug
                # Increment the estimated cost to the goal by 1 actions
                h += 1 
    return h

print(a_star())