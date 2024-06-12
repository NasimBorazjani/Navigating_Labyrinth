
import heapq

def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (0, 0, 0, 0)
    goal_state = (209, 293, 326, 379)
    jug_capacities = [56, 92, 66, 85, 65, 136]
    num_buckets = 4

    # Initialize a dictionary to store the cost of reaching each visited state
    visited_costs = {}
    visited_costs[initial_state] = 0

    # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
    # Record the actions required to get to each state in a list; no actions performed to reach the initial state
    queue = [(0, 0, [], initial_state)]

    # While there are un-visited states
    while queue:
        # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
        _, g, actions, state = heapq.heappop(queue)

        # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
        if state == goal_state:
            return actions

        # Generate all possible actions from the current state, which includes filling any of the 4 buckets with any of the 6 jugs
        for jug in jug_capacities:
            for bucket in range(num_buckets):
                # Check if the new state would be valid, ie if the bucket can be filled with the jug without overfilling it or violating the constraint that the amount of water in each bucket cannot exceed the amount of water in the bucket placed after it
                if state[bucket] + jug <= goal_state[bucket] and all(state[bucket] + jug >= state[i] for i in range(bucket + 1, num_buckets)):
                    # Generate the new state
                    new_state = list(state)
                    new_state[bucket] += jug
                    new_state = tuple(new_state)
                    # The cost so far is the number of actions performed, as our objective is to minimize the number of actions required to reach the goal state
                    new_cost = g + 1

                    # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('+', jug, bucket + 1)], new_state))

                # Similarly, generate all possible actions of emptying any of the 4 buckets
                if state[bucket] >= jug and all(state[bucket] - jug <= state[i] for i in range(bucket + 1, num_buckets)):
                    new_state = list(state)
                    new_state[bucket] -= jug
                    new_state = tuple(new_state)
                    new_cost = g + 1

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [('-', jug, bucket + 1)], new_state))

    return None

def heuristic(state, goal):
    # An admissible and consistent heuristic is the sum of the remaining amounts of water needed to fill each bucket to its goal amount
    # The heuristic relaxes the constraint that the buckets can only be filled with the jugs and presumes we can add the exact amount of water needed to fill each bucket to its goal amount
    # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
    # The heuristic is consistent because the cost of filling a bucket with a jug is always 1, which is exactly the decrease in the remaining amount of water needed to fill the bucket, if the jug is used to fill the bucket, otherwise the estimated cost of the successor node is the same or higher, and the heuristic estimate for the goal state is 0, as the remaining amount of water needed to fill each bucket would be 0 in the goal state.
    return sum(goal[i] - state[i] for i in range(len(state)))

print(a_star())
