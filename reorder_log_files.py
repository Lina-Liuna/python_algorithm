#you have an array of logs. Each log is a space delimited string of words.
#For each log, the first word in each log is an alphanumeric identifier.
#THen, either: each word after the identifier will consist only of lowercase letters, or;
#each word after the ientifier will consist only digits.
#we will call these two varieties of logs letter-logs and digit-logs. It is guaranteed that each log has at least one word after its identifier

#Reorder the logs so that all of the letter-logs come before any digit-log.
#The letter-logs are ordered lexicographicallu ignoring identifier, with the identifier used in case of ties.
#The digit-logs should be put in their original order.
#Return the final order of the logs.

#Example:
#Input: ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
#Output:["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]

strings = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]

class Solution(object):
    def reorderLogFiles(self, logs):
        def f(log):
            id_, rest = log.split(" ", 1)
            if rest[0].isalpha():
                return (0, rest, id_)
            else:
                return (1,)

        return sorted(logs, key = f)

outputStrings = Solution.reorderLogFiles(Solution, strings)

for st in outputStrings:
    print(st)
