


def goalParserInterpretation(command):
    newString = []
    for idx, val in enumerate(command):
        if val == '(' and command[idx+1] == ')':
            newString.append('o')
            continue
        elif val == '(' and command[idx+1] != ')' or val == ')':
            continue
        newString.append(val)
    
    return ''.join(newString)

command = "G()()()()(al)"
print(goalParserInterpretation(command))