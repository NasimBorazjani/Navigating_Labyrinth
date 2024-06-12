
import heapq

def initialize():
    coins = [22, 25, 37, 5, 46, 10, 23, 23, 3, 6, 34, 32, 34, 2, 3, 8, 4, 28, 32, 24, 15, 38, 17, 35, 9, 12, 12, 22, 34, 48, 39, 30, 7, 18, 10, 46, 30, 36, 49, 27, 22, 19, 9, 24, 43, 15]
    tax_values = {18: 11, 17: 7, 7: 6, 43: 2, 22: 3, 24: 11, 9: 3, 36: 10, 46: 4, 10: 3, 39: 5, 5: 5, 35: 15, 28: 8, 15: 2, 34: 6, 27: 3, 38: 11, 30: 20, 23: 18, 25: 10, 12: 1, 4: 1, 49: 16, 37: 6, 48: 17, 2: 2, 8: 4, 3: 1, 6: 3, 19: 10, 32: 19}
    target_sum = 463
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
