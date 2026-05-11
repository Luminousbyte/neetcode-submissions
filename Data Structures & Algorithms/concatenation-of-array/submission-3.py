class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = 2
        lst = []
        while n:
            for i in nums:
                lst.append(i)
            n -= 1
        return lst