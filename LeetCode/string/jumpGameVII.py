


def jumpGameVII(string, minJump, maxJump):
    if string[0] != '0':
        return False

    for i in string:
        if minJump == 0:
            minJump = maxJump
            
                    