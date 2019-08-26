class Solution:
    def threeSumClosest(self, nums, target):
        l = len(nums)
 
        dis = 999999
        res = nums[0] + nums[1] + nums[2]
        nums.sort()
        pre = None
        
        for i in range(l-2):
            
            if nums[i] == pre: # 跳过重复的固定数字
                continue
            pre = nums[i]
            
            j = i+1
            k = l-1
            temp_pre = nums[i] + nums[j] + nums[k] - target
            
            while j < k:
                temp = nums[i] + nums[j] + nums[k] - target
                

                dis = min(dis, abs(temp), abs(temp_pre))
                if dis == abs(temp):
                    res = temp + target
                elif dis == abs(temp_pre):
                    res = temp_pre + target

                    
                if temp < 0:
                    j += 1
                elif temp > 0:
                    k -= 1
                else:
                    return target
            if not j < k:
                dis = min(dis, abs(temp))
                if dis == abs(temp):
                    res = temp + target
                
        return res
