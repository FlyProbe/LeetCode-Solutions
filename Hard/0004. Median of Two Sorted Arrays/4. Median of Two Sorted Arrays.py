class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:

        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, int((m + n + 1) / 2)
        while imin <= imax:
            i = int((imin + imax) / 2)
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])
                    
                # 这里非常巧妙的避开了A=[], B=[1]的判空问题，如果把奇偶放在一起return，下面会报列表越界
                # A=[], B=[1]时， imin = 0, imax = 0, half = 1, i = 0, j = 1, 这是i==m True, B[1]越界。
                if (m + n) % 2 == 1:
                    return max_of_left  

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0
