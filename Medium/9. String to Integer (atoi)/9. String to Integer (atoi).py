class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip().split(" ")[0]
        nums = '1234567890'
        flag = 1
        int_max = 2**31-1
        int_min = -2**31
        if len(str) == 1:
            try:
                return(eval(str))
            except Exception as e:
                return(0)
        if str.startswith('+') or str.startswith('-'):
            if str[1] not in nums:
                return 0
            if str.startswith('-'):
                flag = -1
            str = str[1:]
        for i in range(len(str)):
            if str[i] not in nums:
                str = str[:i]
                break
        while str.startswith('0') and len(str) > 0:
            str = str[1:]
        try:
            res = eval(str)*flag
        except Exception as e:
            return 0
        if res > int_max:
            return int_max
        elif res < int_min:
            return int_min
        else:
            return res
        
