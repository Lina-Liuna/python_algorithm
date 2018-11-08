#There are two sorted arrays nums1 and nums2 of size m and size n respectively.
#Find the median of the two sorted arrays. The overall run time complexity should be O(log(m+n))

#Example 1:
#nums1 = [1,3]
#nums2 = [2]
#the median is 2.0
INT_MIN = 0
INT_MAX = 65535

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)

        if (n1 < n2):
            print("nums1 shorter than nums2")
            return findMedianSortedArrays(self, nums2, nums1)
        l0 = 0
        hi = n2 * 2
        while (l0 <= hi):
            mid2 = int((l0 + hi) / 2)
            mid1 = int((n1 + n2) - mid2)
            print ("mid1 = " + str(mid1) + "mid2 = " + str(mid2))
            if (mid1 == 0):
                L1 = INT_MIN
            else:
                L1 = nums1[int((mid1 - 1)/2)]
            if (mid2 == 0):
                L2 = INT_MIN
            else:
                L2 = nums2[int((mid2 - 1)/2)]
            if (mid1 == n1 * 2):
                R1 = INT_MAX
            else:
                R1 = nums1[int(mid1 / 2)]
            if (mid2 == n2 * 2):
                R2 = INT_MAX
            else:
                R2 = nums2[int(mid2 / 2)]

            print("L1 = " + str(L1) + "L2 = " + str(L2))
            print("R1 = " + str(R1) + "R2 = " + str(R2))
            print("l0 = " + str(l0) + "hi = " + str(hi))
            if (L1 > R2):
                print("L1 > R2")
                l0 = int(mid2 + 1)
                print("l0 = " + str(l0))
            elif (L2 > R1):
                print("L2 > R1")
                hi = int(mid2 - 1)
                print("hi = " + str(hi))
            else:
                print("return")
                return (max(L1, L2) + min(R1, R2)) / 2
        return - 1

nums2 = [1,2,9]
nums1 = [4, 9,10, 12,16]

medianNum = Solution.findMedianSortedArrays(Solution, nums1, nums2)
print("Find the median is: " + str(medianNum))



