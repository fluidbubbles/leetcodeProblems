class Solution:
    def defangIPaddr(self, address: str) -> str:
        defang_ad = ""
        for i in address:
            if i != ".":
                defang_ad += i
            else:
                defang_ad += "[.]"
        return defang_ad