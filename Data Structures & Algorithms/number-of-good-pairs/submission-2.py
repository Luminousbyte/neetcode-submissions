class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        print(hashmap)
        p = []
        for v in hashmap.values():
            if v > 1:
                perm = math.factorial(v)//(2 * math.factorial(v - 2))
                p.append(perm)
        return sum(p)