# You are given two non-empty linked lists representing two non-negative integers.
#The digits are stored in reverse order and each of their node contain a single digit.
#Add the two numbers and return it as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Example input: (2->4->3) + (5->6->4)
#        output:7->0->8
#Explanation: 342 + 465 = 807
from llist import sllist, sllistnode

def addTwoNumbers(l1, l2):
    
    dummy = sllist()
    carry = 0
    n1 = l1.first
    n2 = l2.first
    sum = dummy.first
    while n1 or n2 or carry:
        if n1:
            carry += n1.value
            n1 = n1.next
        if n2:
            carry += n2.value
            n2 = n2.next
        sum = dummy.append(sllistnode(carry % 10))
        carry //= 10
        sum = sum.next
    return dummy


L1 = sllist([2,4,3])
L2 = sllist([5,6,4])
print("start")
Output = addTwoNumbers(L1, L2)
for val in Output:
    print(val)

