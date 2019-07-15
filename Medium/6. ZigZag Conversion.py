class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = []
        for i in range(numRows):
            res.append("")
        now = 0
        x = 1
        for i in s:
            res[now]+=i
            now += x
            if now == numRows-1:
                x = -1
            if now == 0:
                x = 1
        res = ''.join(res)
        return res
