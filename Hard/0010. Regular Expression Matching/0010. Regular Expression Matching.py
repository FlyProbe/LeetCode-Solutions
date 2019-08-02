class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 最后一位匹配：self.isMatch(s[:-1], p[:-1])
        # 最后一位不匹配:
        #       不是*：False
        #       是*：<1> s[-1]和p[-2]不匹配：self.isMatch(s, p[:-2])
        #            <2> s[-1]和p[-2]匹配：self.isMatch(s[:-1], p) or self.isMatch(s, p[:-2])
        
        lp = len(p)
        ls = len(s)
        
        if lp == 0 and ls == 0:
            return True
        elif lp == 0 and ls != 0:
            return False
        elif ls == 0: 
            if lp%2 != 0:
                return False
            else:
                for i in range(1,lp,2):
                    if p[i]!='*':
                        return False
                return True
        else:
            if s[-1] == p[-1] or p[-1] == '.':
                return self.isMatch(s[:-1], p[:-1])
            elif p[-1] != '*':
                return False
            else:
                if s[-1]!=p[-2] and p[-2]!='.':
                    return self.isMatch(s, p[:-2])
                else:
                    return self.isMatch(s[:-1], p) or self.isMatch(s, p[:-2])
