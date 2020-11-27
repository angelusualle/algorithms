# O(N) time and O(1) space where N is number of days to analyze
def get_buy_sell_dates(prices):
    buy_date = 0
    sell_date = 0
    best_sell_buy_date = 0
    best_profit = float('-inf')
    for i,price in enumerate(prices[1:]):
        if prices[buy_date] > price:
            buy_date = i
        if best_profit < (prices[i] - prices[buy_date]):
            best_profit = (prices[i] - prices[buy_date])
            sell_date = i
            best_sell_buy_date = buy_date
    return best_profit, best_sell_buy_date, sell_date
