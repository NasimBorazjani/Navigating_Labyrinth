
import heapq

def initialize():
    coins = [40, 28, 46, 16, 13, 15, 38, 39, 3, 8, 40, 41, 18, 48, 16, 25, 39, 14, 47, 46, 31, 16, 41, 45, 9, 26, 33, 46, 17, 23, 6, 46, 7, 43, 10, 28, 47, 15, 35, 20, 32, 4, 32, 9, 48, 7, 34, 46, 10, 39, 44]
    tax_values = {44: 6, 39: 15, 4: 2, 23: 11, 7: 2, 40: 10, 13: 10, 34: 8, 45: 9, 10: 3, 35: 18, 14: 2, 28: 5, 46: 12, 25: 3, 26: 18, 15: 11, 31: 2, 20: 15, 9: 7, 41: 13, 18: 16, 32: 11, 3: 3, 48: 20, 38: 4, 43: 6, 33: 9, 16: 13, 8: 4, 17: 1, 47: 17, 6: 5}
    target_sum = 485
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
