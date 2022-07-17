

def buddyString(string, goal):
    left, right = 0, len(string) - 1

    if len(string) != len(goal):
        return False

    if string == goal and len(set(string)) < len(string):
        return True
    

    difference = []

    for i in range(len(string)):
        if string[i] != goal[i]:
            difference.append((string[i], goal[i]))
        
    
    if len(difference) == 2 and difference[0] == difference[-1][::-1]: 
        return True

    
    return False


print(buddyString("aaaaaaabc", "aaaaaaacb"))


