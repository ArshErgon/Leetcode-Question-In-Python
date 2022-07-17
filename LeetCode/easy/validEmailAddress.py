


def numUniqueEmails(emails):
    seen = set()
    for email in emails:
        name, domain = email.split('@') 
        # local = name.split('+')[0].replace('.', '')
        local = name.split('+')[0]
        seen.add(local + '@' + domain)
    return len(seen)


print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))