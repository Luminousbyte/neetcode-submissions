class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = Counter(arr)
        max_k = -1
        for k, v in hashmap.items():
            if k == v:
                max_k = max(max_k, k)
        return max_k