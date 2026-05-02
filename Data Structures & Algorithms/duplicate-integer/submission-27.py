class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for val in nums:
            dic[val] = dic.get(val, 0) + 1
            
        
        print(dic)

        for val in dic.values():
            if val > 1:
                return True
        return False
