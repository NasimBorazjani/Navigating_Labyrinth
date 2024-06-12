
import heapq

def initialize():
    coins = [41, 4, 22, 8, 5, 5, 20, 4, 3, 19, 4, 13, 3, 18, 20, 9, 15, 3, 3, 14, 3, 14, 9, 4, 15, 19, 6, 15, 22, 19, 3, 3, 20, 9, 20, 11, 22, 15, 20]
    tax_values = {20: 11, 15: 13, 9: 7, 8: 3, 3: 1, 6: 3, 5: 2, 13: 11, 4: 4, 22: 11, 19: 19, 11: 1, 14: 2, 41: 16, 18: 18}
    target_sum = 220
    num_coins = len(coins)
    visited_costs = {}
    visited_costs[()] = 0
    queue = [(0, 0, [], ())]
    return (coins, tax_values, target_sum, num_coins, visited_costs, queue)

def a_star():
    (coins, tax_values, target_sum, num_coins, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        if (sum(state) == target_sum):
            return actions
        for coin_ind in range(num_coins):
            if ((coin_ind not in state) and ((not state) or (((coins[coin_ind] % 2) == 0) and (state[(- 1)] < coins[coin_ind])) or (((coins[coin_ind] % 2) == 1) and (state[(- 1)] >= coins[coin_ind])))):
                new_state = (state + (coin_ind,))
                new_cost = (g + tax_values[coins[coin_ind]])
                if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, target_sum, coins, tax_values)
                    heapq.heappush(queue, ((new_cost + h), new_cost, (actions + [coins[coin_ind]]), new_state))
    return None

def heuristic(state, target_sum, coins, tax_values):
    h = 0
    coins = sorted(coins, reverse=True)
    for coin_ind in state:
        if ((sum(state) + coins[coin_ind]) <= target_sum):
            h += tax_values[coins[coin_ind]]
    return h
print(a_star())
