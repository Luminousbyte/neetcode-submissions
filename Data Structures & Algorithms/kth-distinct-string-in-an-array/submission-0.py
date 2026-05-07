class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashmap = defaultdict(int)
        for s in arr:
            hashmap[s] += 1
        lst = []
        for key, v in hashmap.items():
            if v == 1:
                lst.append(key)
        return lst[k-1] if len(lst) >= k else ""