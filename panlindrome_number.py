#Determine whether an integer is a palindrome. an integer is a palindrome when it reads the same backward as forwards

def palindromeNum(num):
    chunk = str(num)
    if chunk == chunk[::-1]:
        return "True"
    else:
        return "False"


result = palindromeNum(12100)

print(result)
