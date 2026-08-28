class Solution:

    def encode(self, strs: List[str]) -> str:
        strs_x = ""
        for i in strs:
            strs_x += "*#"+i
        print(strs_x)
        return strs_x
    def decode(self, s: str) -> List[str]:
        lst = []
        for word in s.split("*#"):
            lst.append(word)
        lst.remove("")

        return lst