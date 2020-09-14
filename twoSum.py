# -*- coding: utf-8 -*-

"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。


示例:
    给定 nums = [2, 7, 11, 15], target = 9

    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]


链接：https://leetcode-cn.com/problems/two-sum
"""


class Solution(object):
    @staticmethod
    def two_sum(nums, target):
        """
        Args:
            nums: 数组列表
            target: 目标和
        """

        nums_map = {val: idx for idx, val in enumerate(nums)}

        for idx, val in enumerate(nums):
            val_ext = target - val

            val_ext_idx = nums_map.get(val_ext)
            if val_ext_idx and idx != val_ext_idx:
                return [idx, val_ext_idx]


def test():
    nums = [2, 7, 11, 15]

    assert Solution.two_sum(nums, 9) == [0, 1]
    assert Solution.two_sum(nums, 18) == [1, 2]
    assert Solution.two_sum(nums, 26) == [2, 3]
    assert Solution.two_sum(nums, 2) is None
    assert Solution.two_sum(nums, 20) is None
    assert Solution.two_sum(nums, 99) is None
    assert Solution.two_sum(nums, 4) is None

    assert Solution.two_sum([], 0) is None


if __name__ == '__main__':
    test()
