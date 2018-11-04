#Given a string, find the length of the longest substring without repeating characters

class Solution:
    # return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):


            if s[i] in usedChar and start <= usedChar[s[i]]:
                print("s[" + str(i) + "] = " + s[i] + ", start = " + str(start))
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i
            print("usedChar[" + s[i] + "] = " + str(usedChar[s[i]]))

        return maxLength


myStr = "tmmzuxta"
len = Solution.lengthOfLongestSubstring(Solution, myStr)
print(len)

# why do we need start <= usedChar[s[i]]
# This is because once we need update start that means we want to make sure that there is no repeated char
# between the s[start] and the s[i],
# So if we try to judge if adding a new coming char s[i] will incur the change of start,
# We should judge that if s[i] is already existed in the usedChar
# and that s[i] exisited after s[start].