# 固定数字+双指针。由于预先排序，1、固定数字最小，大于0即可停止循环；2、重复的固定数字没有意义，可以跳过
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        res = {}
        nums.sort()
        pre = None
        for i in range(l-2):
            
            if nums[i] > 0: # 最小数字大于0，停止
                break
        
            if nums[i] == pre: # 跳过重复的固定数字
                continue
            pre = nums[i]
            
            j = i+1
            k = l-1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    res[(nums[i], nums[j], nums[k])] = 1
                    j += 1
        sol = []
        for keys in res:
            sol.append(list(keys))
        return sol
    
