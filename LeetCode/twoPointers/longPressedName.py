

def longPressedName(name, typed):
    if len(name) > len(typed):
        return False
    
    i = 0
    for left in range(len(typed)):
        if i < len(name) and name[i] == typed[left]:
            i += 1
        elif left == 0 or typed[left] != typed[left-1]:
            return False
        
    return i == len(name)

print(longPressedName('alex', 'aaleex'))
# print(longPressedName('saeed', 'ssaaedd'))
# print(longPressedName("xnhtq", "xhhttqq"))
