# coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
from math import inf
from typing import List


# 给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。
# 示例 1 :
# 输入: 2736
# 输出: 7236
# 解释: 交换数字2和数字7。
#
# 示例 2 :
# 输入: 9973
# 输出: 9973
# 解释: 不需要交换。
#
# 注意:
# 给定数字的范围是 [0, 10^8]
#
# class Solution:     def maximumSwap(self, num: int) -> int:
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)

        right = [-1] * n
        r = -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                r = i
            right[i] = r

        left = [-1] * n
        l = -1
        preSum = [0] * n
        for i in range(n):
            if i > 0:
                preSum[i] = preSum[i-1]
            if s[i] == '*':
                preSum[i] += 1
            if s[i] == '|':
                l = i
            left[i] = l

        ret = []
        for (l, r) in queries:
            _l = right[l]
            _r = left[r]
            count = preSum[_r] - preSum[_l] if _l < _r  else 0
            ret.append(count)
        return ret


if __name__ == '__main__':
    # print(Solution().platesBetweenCandles("**|**|***|", [[2, 5], [5, 9]]))
    print(Solution().platesBetweenCandles("***|**|*****|**||**|*", [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]))
    # print(Solution().maximumSwap(2736))
    # print(Solution().maximumSwap(1259))
    # print(Solution().maximumSwap(9973))
    # print(Solution().maximumSwap(98863))
    # print(Solution().maximumSwap(1))
