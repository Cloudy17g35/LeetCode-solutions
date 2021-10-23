

def maximal_profit(prices) -> int:

    """this function takes the prices of the stocks,
    returns the biggest profit you can achieve by buying the stock in one day
    selling it in in'th day in future, if it's no possibility to get any profit returns 0
    arguments: prices: list of int type
    returns: maximal profit"""

    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit






