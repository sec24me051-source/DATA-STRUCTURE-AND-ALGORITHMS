class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a=[]
        for i in range(m):
            a.append(nums1[i])
        for i in range(n):
           
            a.append(nums2[i])
        a.sort()
        for i in range(m+n):
            nums1[i]=a[i]
