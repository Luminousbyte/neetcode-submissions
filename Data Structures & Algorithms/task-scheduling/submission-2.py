class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = defaultdict(int)
        for task in tasks:
            hashmap[task] += 1

        max_freq = max(hashmap.values())

        count = 0
        for values in hashmap.values():
            if values == max_freq:
                count += 1

        length = (n+1) * (max_freq - 1) + count
        return max(length, len(tasks))