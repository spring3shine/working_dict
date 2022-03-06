#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param A int整型一维数组 非空整数数组，已从小到大排过序
# @param B int整型一维数组 非空整数数组，已从小到大排过序
# @param c int整型 整数
# @return int整型一维数组
#
class Solution:
    def findNearestSum(self, A: List[int], B: List[int], c: int) -> List[int]:
        # write code here
        import bisect
        n, m = len(A), len(B)
        _min_abs = abs(A[0]+B[0]-c)
        ret = [A[0],B[0]]
        for x in A:
            bid = bisect.bisect_left(B, c-x)
            if bid == 0:
                Bx = B[bid]
            elif bid == m:
                Bx = B[bid-1]
            else:
                Bx = B[bid] if abs(B[bid]+x-c) < abs(B[bid-1]+x-c) else B[bid-1]

            if _min_abs > abs(x+Bx-c):
                _min_abs = abs(x+Bx-c)
                ret = [x,Bx]
        return ret
import numpy
numpy.dot()