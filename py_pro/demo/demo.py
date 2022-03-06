# coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
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
    def maximumSwap(self, num: int) -> int:
        l_num = []
        while num:
            l_num.append(num % 10)
            num = num // 10
        l_num.reverse()

        for i,v in enumerate(l_num):
            _max = v
            _max_id = i
            for j in range(i + 1, len(l_num)):
                if l_num[j] > _max:
                    _max = l_num[j]
                    _max_id = j
            if l_num[i] < _max:
                l_num[i], l_num[_max_id] = l_num[_max_id], l_num[i]
                break

        return int(''.join(map(str, l_num)))
        #
        #
        # # return l_num
        # ret = 0
        # _u = 1
        # for i in range(len(l_num)-1,-1,-1):
        #     ret += l_num[i] * _u
        #     _u *= 10
        # return ret




if __name__ == '__main__':
    assert Solution().maximumSwap(2736) == 7236
    assert Solution().maximumSwap(1259) == 9251
    assert Solution().maximumSwap(9973) == 9973
    assert Solution().maximumSwap(98368) == 98863
    assert Solution().maximumSwap(1) == 1
    assert Solution().maximumSwap(11) == 11
    assert Solution().maximumSwap(12) == 21
    # print(Solution().maximumSwap(2736))
    # print(Solution().maximumSwap(1259))
    # print(Solution().maximumSwap(9973))
    # print(Solution().maximumSwap(98863))
    # print(Solution().maximumSwap(1))
