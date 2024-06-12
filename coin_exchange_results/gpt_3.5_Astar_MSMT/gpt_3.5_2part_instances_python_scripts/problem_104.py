
import heapq

def initialize():
    coins = [18, 23, 23, 36, 27, 10, 25, 14, 6, 43, 6, 31, 5, 43, 3, 13, 16, 8, 11, 6, 39, 44, 41, 28, 12, 8, 1, 14, 22, 23, 11, 24, 37, 9, 2, 31, 27, 10, 9, 38, 37, 4, 4, 17, 18, 36, 18, 32, 3, 12, 4, 42, 8, 4, 4, 16, 30, 40, 13, 41]
    tax_values = {6: 4, 18: 3, 38: 1, 23: 2, 16: 8, 12: 2, 4: 2, 24: 13, 28: 17, 30: 17, 1: 1, 9: 9, 27: 8, 11: 4, 37: 16, 41: 19, 13: 3, 31: 8, 44: 8, 22: 7, 43: 13, 10: 3, 17: 8, 36: 7, 39: 3, 25: 17, 40: 10, 8: 6, 32: 16, 14: 4, 2: 1, 42: 3, 3: 2, 5: 2}
    target_sum = 441
    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0
    queue = [(0, 0, [], (0, 0, 0))]
    return (coins, tax_values, target_sum, visited_costs, queue)

def a_star():
    (coins, tax_values, target_sum, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        (total_value, prev_coin, total_tax) = state
        if (total_value == target_sum):
            return actions
        for coin in coins:
            if ((coin not in actions) and ((total_value + coin) <= target_sum)):
                if (((coin < prev_coin) and ((coin % 2) == 0)) or ((coin >= prev_coin) and ((coin % 2) != 0))):
                    coin_tax = tax_values[coin]
                    new_total_tax = (total_tax + coin_tax)
                    new_state = ((total_value + coin), coin, new_total_tax)
                    new_cost = (g + coin_tax)
                    if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, ((g + new_total_tax), new_cost, (actions + [coin]), new_state))
    return None
print(a_star())
