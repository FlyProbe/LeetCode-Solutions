class Solution:
    def intToRoman(self, num: int) -> str:
        all_dict = {
            0 : {1 : 'I', 4 : 'IV', 5 : 'V', 9 : 'IX'},
            1 : {1 : 'X', 4 : 'XL', 5 : 'L', 9 : 'XC'},
            2 : {1 : 'C', 4 : 'CD', 5 : 'D', 9 : 'CM'},
            3 : {1 : 'M'}
        }
        length = len(str(num))
        res = ''
        for i in range(length-1, -1, -1):
            now = num // (10 ** i)
            if now == 9:
                res += all_dict[i][now]
            elif now < 9 and now >= 5:
                res += all_dict[i][5]
                res += all_dict[i][1] * (now-5)
            elif now == 4:
                res += all_dict[i][4]
            else:
                res += all_dict[i][1] * now
            num = num % (10**i)
        return res
        
