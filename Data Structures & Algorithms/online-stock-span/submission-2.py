class StockSpanner:

    def __init__(self):
        self.lst = []

    def next(self, price: int) -> int:
        self.lst.append(price)
        i = len(self.lst) - 2
        while i>=0 and self.lst[i] <= price:
            i -= 1
        return len(self.lst) - i - 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)