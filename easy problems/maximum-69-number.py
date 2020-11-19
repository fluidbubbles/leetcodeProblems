class Solution:
    def maximum69Number(self, num: int) -> int:
        num = str(num)
        change = True
        new_num = ""
        for i in num:
            if i == '9':
                new_num += i
            elif change:
                change = False
                new_num += '9'
            else:
                new_num += i
        return new_num

