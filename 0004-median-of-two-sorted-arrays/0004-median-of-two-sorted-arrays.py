class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        left = 0
        right = m
        while left <= right:
            mid1 = (left + right) // 2
            mid2 = (m + n + 1) // 2 - mid1

            a = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
            b = float('inf') if mid1 == m else nums1[mid1]

            c = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
            d = float('inf') if mid2 == n else nums2[mid2]

            if a <= d and c <= b:

                if (m + n) % 2 == 0:
                    return (max(a, c) + min(b, d)) / 2

                return max(a, c)

            elif a > d:
                right = mid1 - 1

            else:
                left = mid1 + 1