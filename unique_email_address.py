#every email consists of a local name and a domain name, separated by the @sign.

#besides the lowercase letters, these emails may contain '.'s or '+'s.
#if you add period ('.') between some characters in the local name part of an email address,
#mail sent will be forward to the same address without dots in the local name.
#"alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
#if you add a plus('+') in the local name, everything after the first plus sign will be ignored.
#m.y+name@email.com will be forward to my@email.com

#Given a list of emails, we send one email to each address in the list.
#How many different addresses actually receive mails

EmailAddr = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com","testemail+davide@lee.tcode.com"]
EmailAddr2 = ["leetcode.com@leetcode.com", "test.e.mail+bob.cathy@leetcode.com","testemail+davide@lee.tcode.com"]


class Solution:
    def numUniqueEmails(selfs, emails):
        results = set()
        for email in emails:
            local_name, domain_name = email.split("@", 1)
            newlocal_name = local_name.replace(".","")
            if "+" in newlocal_name:
                newlocal_name, rest = newlocal_name.split("+", 1)
            email = email.replace(local_name, newlocal_name,1)
            results.add(email)
        return len(results)

print(Solution.numUniqueEmails(Solution, EmailAddr))
print(Solution.numUniqueEmails(Solution, EmailAddr2))
