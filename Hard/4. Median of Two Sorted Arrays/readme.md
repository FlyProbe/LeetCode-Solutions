思路：
1、把所有数分为长度相等的两部分：
x = x1, x2, x3, |i|  x4, x5, x6, x7
y = y1, y2, y3, y4, y5, |j| y6, y7, y8, y9

2、判别条件：如果left_part 的每一个数都比right_part 小，那么中位数只和x3, x4, y5, y6有关。即：
  if (x + y)%2 ==0 : median = (max(x3, y5) + min(x4, y6))\\2
  else : median = max(x3, y5) --->在这种情况下，让左边比右边多一个数

3、如何判别2中条件：只要x3 < y6 and y5 < x4就满足了条件。这时候用binary search去确定i的位置。 ** i 是较短array的指针
(1)  i = x//2
     j = (x + y + 1)//2 - i
     -----> i + j = (x + y + 1) // 2 ----------> 如果x+y是偶数， i+j = x+y-i-j; else i+j = x+y-i-j-1 -->左右一样多或者左边多一个
 
 (2) if x3 > y6: -----> x4>x3>y6>y5
        i左移(binary)
     elif y5 > x4: -----> y6>y5>x4>x3
        i右移
     
     # i左移，j就会右移，分界点周围的y变大，x变小。
     
     else:
        # 如果不是上述两种，说明两个条件都满足了，计算输出
     