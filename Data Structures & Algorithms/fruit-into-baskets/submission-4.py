class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hashmap = {}
        l = 0
        res = 0

        for i in range(len(fruits)):
            hashmap[fruits[i]] = hashmap.get(fruits[i], 0) + 1

            while len(hashmap) > 2:
                hashmap[fruits[l]] -= 1

                if hashmap[fruits[l]] == 0:
                    del hashmap[fruits[l]]

                l += 1

            res = max(res, i - l + 1)

        return res