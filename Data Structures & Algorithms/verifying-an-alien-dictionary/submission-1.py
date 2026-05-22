class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {}
        for id, l in enumerate(order):
            order_index[l] = id
        print(order_index)

        def compare(word):
            lst = []
            for c in word:
                lst.append(order_index[c])
            return lst

        return words == sorted(words, key = compare)