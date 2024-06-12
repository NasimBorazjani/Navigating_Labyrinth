
import heapq

def initialize():
    initial_state = (0, 0, 0, 0)
    goal_sum = 216
    coins = [20, 19, 2, 12, 23, 18, 15, 13, 10, 6, 9, 4, 9, 16, 5, 8, 19, 6, 7, 2, 6, 15, 10, 9, 4, 6, 19, 10, 10, 16, 21, 17, 21, 16, 13, 6, 16, 8, 7, 11, 13, 7, 21, 15, 15, 6, 11, 19, 7]
    taxes = {6: 6, 8: 6, 16: 4, 15: 11, 12: 3, 10: 5, 20: 14, 9: 3, 17: 8, 7: 5, 5: 5, 2: 1, 11: 4, 23: 18, 19: 3, 13: 13, 18: 6, 4: 3, 21: 20}
    num_coins = len(coins)
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [], initial_state)]
    return (initial_state, goal_sum, coins, taxes, num_coins, visited_costs, queue)

def a_star():
    (initial_state, goal_sum, coins, taxes, num_coins, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        if (state[1] == goal_sum):
            return actions
        for i in range(state[0], num_coins):
            if ((state[1] + coins[i]) <= goal_sum):
                if (((coins[i] < state[2]) and ((coins[i] % 2) == 0)) or ((coins[i] >= state[2]) and ((coins[i] % 2) == 1))):
                    new_state = ((i + 1), (state[1] + coins[i]), coins[i], (state[3] + taxes[coins[i]]))
                    new_cost = (g + taxes[coins[i]])
                    if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                        visited_costs[new_state] = new_cost
                        h = heuristic(new_state, goal_sum, coins, taxes)
                        heapq.heappush(queue, ((new_cost + h), new_cost, (actions + [coins[i]]), new_state))
    return None

def heuristic(state, goal_sum, coins, taxes):
    h = 0
    remaining_coins = sorted(coins[state[0]:], key=(lambda x: taxes[x]))
    for coin in remaining_coins:
        if ((state[1] + coin) <= goal_sum):
            h += taxes[coin]
    return h
print(a_star())
