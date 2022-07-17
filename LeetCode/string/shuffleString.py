


def shuffleString(string, indices):
    newString = [0] * len(indices)
    for val, idx in zip(string, indices):
        newString[idx % len(string)] = val

    return ''.join(newString)

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

print(shuffleString(s, indices))
