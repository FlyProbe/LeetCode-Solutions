class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        try:
            pre = strs[0]
        except Exception:
            return ""
        
        for item in strs:
            pre = pre[:min(len(item), len(pre))]
            for i in range(len(pre)):
                if item[i] != pre[i]:
                    pre = pre[:i]
                    if pre  == "":
                        return ""
                    break

        return pre
                    
