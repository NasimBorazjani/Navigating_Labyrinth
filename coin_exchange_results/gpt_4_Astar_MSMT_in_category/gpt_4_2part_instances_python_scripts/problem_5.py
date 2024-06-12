
import heapq

def initialize():
    initial_state = (0, 0, 0, 0)
    goal_sum = 239
    coins = [20, 10, 16, 21, 15, 21, 13, 6, 19, 9, 7, 5, 2, 6, 9, 22, 4, 13, 3, 16, 22, 18, 6, 5, 14, 7, 7, 2, 17, 9, 8, 83, 14]
    taxes = {22: 18, 21: 1, 14: 12, 10: 8, 8: 6, 17: 9, 6: 4, 7: 6, 9: 3, 20: 13, 19: 12, 5: 3, 13: 8, 4: 3, 83: 14, 3: 2, 18: 1, 2: 1, 16: 2, 15: 3}
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
