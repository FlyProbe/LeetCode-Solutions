class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        all_dict = {
            'I' : 1, 'V' : 5, 'IV' : 4, 'IX' : 9,
            'X' : 10, 'L' : 50, 'XL' : 40, 'XC' : 90,
            'C' : 100, 'D' : 500, 'CD' : 400, 'CM' : 900,
            'M' : 1000
        }
        l = len(s)
        i = 0
        while i < l:
            temp = all_dict[s[i]]
            try:
                if s[i]+s[i+1] in all_dict:
                    temp = all_dict[s[i:i+2]]
                    i += 2
                else:
                    i += 1
            except Exception as e:
                i += 1
            res += temp
        return res
