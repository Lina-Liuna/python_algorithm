#Your friend is typing his name into a keyboard.
#sometimes, when typing a character c, the key might get long pressed, and the character will be typed1 or more times.

#Return True if it is possible that it was your friends name, with some characters being long pressed.
import itertools

class Solution(object):
    def isLongPressedName(self, name, typed):
        g1 = [(k, len(list(grp))) for k, grp in itertools.groupby(name)]
        g2 = [(k, len(list(grp))) for k, grp in itertools.groupby(typed)]
        print(g1)
        print(g2)
        print(len(g1))
        print(len(g2))
        if len(g1) != len(g2):
            return False

        return all(k1 == k2 and v1 < v2 for (k1, v1), (k2, v2) in zip(g1, g2))

print(str(Solution.isLongPressedName(Solution, "alex", "aaaaallllllexxxxxxx")))
print(str(Solution.isLongPressedName(Solution,"abc","abcd")))
print(str(Solution.isLongPressedName(Solution,"abcde","abcd")))
