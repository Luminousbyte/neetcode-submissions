class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = defaultdict(int)
        for l in order:
            hashmap[l] = order.index(l)

        def ind(word):
            lst = []
            for w in word:
                lst.append(hashmap[w])
            return lst

        x = []
        for word in words:
            x.append(ind(word))
        print(x)
        print(words)
        return x == sorted(x)