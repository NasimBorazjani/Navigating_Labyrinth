
import heapq

def initialize():
    coins = [30, 4, 10, 25, 2, 20, 23, 22, 29, 13, 21, 23, 23, 24, 3, 26, 29, 27, 15, 18, 28, 10, 22, 24, 2, 22, 13, 32, 8, 28, 31, 13, 27, 6, 35, 2, 20, 25, 24, 2, 16, 31, 3, 5, 23, 32, 24, 20, 13, 7, 11, 12]
    tax_values = {10: 8, 32: 8, 25: 5, 7: 2, 30: 9, 18: 3, 5: 2, 35: 14, 2: 1, 15: 10, 12: 6, 29: 14, 23: 12, 31: 14, 11: 3, 8: 7, 21: 5, 13: 3, 28: 3, 6: 1, 3: 2, 4: 2, 22: 5, 16: 9, 24: 4, 27: 16, 26: 6, 20: 20}
    target_sum = 351
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
