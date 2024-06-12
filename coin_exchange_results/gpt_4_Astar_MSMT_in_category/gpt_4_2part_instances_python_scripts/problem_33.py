
import heapq

def initialize():
    initial_state = (0, 0, 0, 0)
    goal_sum = 296
    coins = [9, 11, 7, 9, 12, 19, 29, 21, 11, 10, 26, 22, 18, 29, 19, 11, 18, 23, 26, 16, 18, 4, 22, 25, 17, 18, 12, 23, 3, 17, 17, 15, 22, 25, 27, 2, 26, 22, 21, 28, 10, 23, 15]
    taxes = {28: 16, 10: 8, 21: 8, 18: 12, 27: 6, 7: 7, 2: 2, 19: 4, 17: 13, 26: 11, 12: 1, 9: 5, 25: 15, 29: 20, 11: 2, 15: 8, 22: 1, 16: 13, 4: 4, 3: 3, 23: 18}
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
