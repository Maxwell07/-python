import heapq
grad = [32,43,654,34,666,55]

print(heapq.nlargest(3,grad))


stocks = [
    {'ticker':'AAPL','price':201},
    {'ticker':'GOOG','price':800},
    {'ticker':'FB','price':54},
    {'ticker':'MSFT','price':68}
]

print(heapq.nsmallest(2,stocks,key = lambda stocks:stocks['price']))
