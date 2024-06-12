
import heapq

def initialize():
    coins = [25, 29, 8, 11, 8, 25, 20, 16, 6, 4, 98, 7, 28, 24, 27, 16, 23, 26, 26, 99, 2, 7, 22, 7, 5, 24, 2]
    tax_values = {24: 5, 26: 16, 28: 20, 2: 1, 22: 16, 25: 11, 27: 7, 11: 4, 6: 3, 99: 17, 8: 5, 7: 5, 5: 3, 23: 5, 4: 4, 98: 16, 16: 3, 29: 5, 20: 19}
    target_sum = 305
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
