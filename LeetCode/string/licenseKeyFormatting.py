

# O(n) || O(n)
def licenseKeyFormatting(string, k):
    newString = string.upper().replace('-', '')[::-1]
    group = []
    for i in range(0, len(newString), k):
        group.append(newString[i:i+k])

    return '-'.join(group)[::-1]

# print(licenseKeyFormatting("5F3Z-2e-9-w", 4))
print(licenseKeyFormatting("2-5g-3-J", 2))