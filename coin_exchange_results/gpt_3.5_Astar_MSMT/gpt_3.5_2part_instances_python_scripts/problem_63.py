
import heapq

def initialize():
    coins = [12, 12, 5, 32, 25, 3, 23, 49, 31, 6, 12, 23, 20, 14, 34, 17, 16, 16, 21, 18, 7, 30, 7, 27, 29, 14, 5, 9, 48, 33, 5, 18, 15, 29, 2, 28, 29, 25, 26, 6, 4, 4, 6, 8, 16, 5, 4, 4, 20, 25, 10, 6, 3, 24, 19]
    tax_values = {20: 18, 16: 6, 19: 2, 27: 12, 25: 2, 6: 2, 26: 16, 23: 9, 28: 12, 49: 16, 33: 13, 30: 12, 8: 6, 21: 18, 31: 16, 48: 5, 15: 5, 10: 2, 3: 1, 29: 14, 32: 15, 5: 3, 4: 4, 34: 3, 17: 14, 12: 11, 7: 3, 9: 9, 14: 7, 24: 14, 18: 15, 2: 1}
    target_sum = 348
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
