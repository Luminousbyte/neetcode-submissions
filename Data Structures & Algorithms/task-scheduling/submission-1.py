class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = defaultdict(int)
        for task in tasks:
            hashmap[task] += 1

        max_freq = max(hashmap.values())

        count = 0
        for freq in hashmap.values():
            if freq == max_freq:
                count += 1
            
        ans = (max_freq - 1) * (n+1) + count

        return max(ans, len(tasks))
