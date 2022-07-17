



class StockSpanner:

    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        res = 1
        while self.stocks and self.stocks[-1][0] <= price:
            res += self.stocks.pop()[1]
        self.stocks.append([price, res])

        return res


obj = StockSpanner()
l = [100, 80, 60, 70, 60, 75, 85]

for i in l:
    print(obj.next(i))

