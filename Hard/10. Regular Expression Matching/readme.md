最后一位匹配：self.isMatch(s[:-1], p[:-1]) <br>
最后一位不匹配:<br>
              不是*：False<br>
              是*：<1> s[-1]和p[-2]不匹配：self.isMatch(s, p[:-2])<br>
                   <2> s[-1]和p[-2]匹配：self.isMatch(s[:-1], p) or self.isMatch(s, p[:-2])<br>
                   
<2>中的情况要特别注意。即便是与带'\*'字符串匹配，也不能确定他是否匹配的恰好是这个带星的位置。<br>
例如：<br>
  s = 'a'<br>
  p = 'aa*'<br>
  此时p中的'a*'应该视为0个a，s的匹配位置是p[0]，返回True，即满足<2>中的后一种情况。所以也需要判断是s删一个字符还是p删2个字符。