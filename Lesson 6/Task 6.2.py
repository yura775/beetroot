stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
def stock_prices(stock, prices):
    d=dict()
    for i in stock:
        if i in prices:
            d[i] = stock[i]*prices[i]
    return d
print(stock_prices(stock, prices))
