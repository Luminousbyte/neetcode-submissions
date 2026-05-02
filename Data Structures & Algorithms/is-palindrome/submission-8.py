class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = []
        for content in s:
            if content.isalnum():
                lst.append(content.lower()) 

        new_lst = lst[::-1]
        print(lst)
        print(new_lst)

        return lst == new_lst