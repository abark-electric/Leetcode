class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        elif x>0:
            new_num = int(str(x)[::-1])
            if new_num>= -2**31 and new_num<(2**31)-1:
                return new_num
            else:
                return 0
        else:
            num = str(x)[1:]
            new_num = -int(num[::-1])
            if new_num>= -2**31 and new_num<(2**31)-1:
                return new_num
            else:
                return 0
