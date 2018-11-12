#Given a strings, find the longest palindromic substring ins.
#You may assume that the maximum length ofs is 1000
#Example 1:
#Input: " babad "Output: "bab, "aba" is also the valid answer

def palindromes(text):
    text = text.lower()
    results = []
    resultstring = ""

    for i in range(len(text)):
        for j in range(0, i):
            chunk = text[j:i + 1]

            if chunk == chunk[::-1]:
                if (len(resultstring) < len(chunk)):
                    resultstring = chunk
                results.append(chunk)
    print(results)
    return resultstring

output = palindromes("abbacde")
print(output)