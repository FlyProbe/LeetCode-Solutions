class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }
        res = []
        
    
        def iterater(combination, left_nums):
            if len(left_nums) == 0:
                res.append(combination)
            else:
                for item in phone[left_nums[0]]:
                    iterater(combination + item, left_nums[1:])
        
        if digits:
            iterater("", digits)
        return res
