

#     O(N) || O(N) 61ms 72.55%
def numUniqueEmails( emails):
    if not emails:
        return 0
    
    seen = set()
    
    for email in emails:
        name, domain = email.split('@')
        local = name.split('+')[0].replace('.', '')
        seen.add(local + '@' + domain)
    return len(seen)

print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))