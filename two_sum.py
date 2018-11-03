class Solution:
    def two_sum(self, nums, target):
        lut = {}
        for i in range(len(nums)):
            if nums[i] in lut:
                return [i, lut[nums[i]]]
            else:
                lut[target-nums[i]] = i



S1 = Solution()
Num_Arr = [2,7,11,15]
Target = 9

Found = S1.two_sum(Num_Arr, Target)

print("Found dices: " + str(Num_Arr[Found[0]]) + "+" + str(Num_Arr[Found[1]]) + "=" + str(Target))
