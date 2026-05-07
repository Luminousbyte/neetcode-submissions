class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst = []
        for i in range(len(nums1)):
            found = False
            print(f"nums1 id i:", nums1[i])
            for j in range(nums2.index(nums1[i]), len(nums2)):
                print(f"------- nums2 id j:", nums2[j], "-------")
                if nums2[j] > nums1[i]:
                    print(f"      >>>>>>>>",(nums2[j], nums1[i]))
                    found = True
                    lst.append(nums2[j])
                    break
            if not found:
                lst.append(-1)
                
        return lst