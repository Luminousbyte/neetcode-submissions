class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        r = l+k-1
        res = len(blocks)
        while r<len(blocks):
            count = 0
            for i in range(l, l+k):
                if blocks[i] == "W":
                    count += 1
            res = min(count, res)
            l += 1
            r += 1
        return res