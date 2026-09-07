class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        r = l + k
        res = 0
        while r <= len(arr):
            avg = sum(arr[l:r])//(r-l)
            print(avg)
            if avg >= threshold:
                res += 1
            l += 1
            r += 1
        return res