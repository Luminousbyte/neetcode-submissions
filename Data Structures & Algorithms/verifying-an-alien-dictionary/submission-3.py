class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = defaultdict(int)
        for id, ltr in enumerate(order):
            hashmap[ltr] = id

        def compare(word):
            lst = []
            for c in word:
                # print(c, end = " ")
                lst.append(hashmap[c])
            # print(lst)
            return lst
        
        # print("1",words)
        # print("2",sorted(words))
        print("3",sorted(words, key = compare))
        return words == sorted(words, key=lambda word: compare(word))