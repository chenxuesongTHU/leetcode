#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File        :   _4  
@Time        :   2021/3/12 8:58 下午
@Author      :   Xuesong Chen
@Description :   寻找两个正序数组的中位数
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_start_idx = 0
        nums1_end_idx = len(nums1)-1
        nums2_start_idx = 0
        nums2_end_idx = len(nums2)-1
        if len(nums2) == 0 or len(nums1) == 0:
            return self.direct_get_median(nums1, nums2)

        for iter_n in range(int((nums2_end_idx+nums1_end_idx+1)/2)):



            if nums1[0] <= nums2[0]:
                nums1.pop(0)
            else:
                nums2.pop(0)
            if len(nums1) == 0:
                nums2.pop()
                return self.direct_get_median(nums1, nums2)
            if len(nums2) == 0:
                nums1.pop()
                return self.direct_get_median(nums1, nums2)

            if nums1[-1] >= nums2[-1]:
                nums1.pop()
            else:
                nums2.pop()

            if len(nums2) == 0 or len(nums1) == 0:
                return self.direct_get_median(nums1, nums2)

        nums1.extend(nums2)
        return sum(nums1) / len(nums1)

    def direct_get_median(self, nums1, nums2):

        if len(nums1) == 0:
            median_idx = int(len(nums2) / 2)
            if len(nums2) % 2 == 1:
                return nums2[median_idx]
            else:
                return (nums2[median_idx - 1] + nums2[median_idx])/2

        if len(nums2) == 0:
            median_idx = int(len(nums1) / 2)
            if len(nums1) % 2 == 1:
                return nums1[median_idx]
            else:
                return (nums1[median_idx - 1] + nums1[median_idx])/2


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.findMedianSortedArrays([1,3,4,5,6], [2]),
        solution.findMedianSortedArrays([1,2], [3, 4]),
        solution.findMedianSortedArrays([0, 0], [0, 0]),
        solution.findMedianSortedArrays([], [1]),
        solution.findMedianSortedArrays([2], []),
        sep='\n',
    )