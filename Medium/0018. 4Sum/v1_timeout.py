class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        l = len(nums)
        res = set()
        nums.sort()
        pre_i = None
        for i in range(l-3):
            
        
            if nums[i] == pre_i: # 跳过重复的固定数字
                continue
            pre_i = nums[i]
            
            pre_j = None
            for j in range(i+1, l-2):
                if nums[j] == pre_j:
                    continue
                pre_j = nums[j]
                
                m = j+1
                n = l-1

                while m < n:
                    if nums[i] + nums[j] + nums[m] + nums[n] < target:
                        m += 1
                    elif nums[i] + nums[j] + nums[m] + nums[n] > target:
                        n -= 1
                    else:
                        res.add((nums[i], nums[j], nums[m], nums[n]))
                        m += 1
                        n -= 1
        sol = []
        for item in res:
            sol.append(list(item))
        return sol
