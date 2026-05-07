class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        # print(countText)
        balloon = Counter("balloon")
        print(balloon)
        res = len(text)
        lst = []
        for c in balloon:
            # print(c)
            lst.append((countText[c],balloon[c]))
            x = countText[c]//balloon[c]
            print(x)
            res = min(res, x)
        print(lst)
        return res