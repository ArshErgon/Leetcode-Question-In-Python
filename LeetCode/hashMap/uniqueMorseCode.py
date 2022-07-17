

# O(n*m) || O(n) \\ could be O(1) only if I dont use a set

def uniqueMorseCode(codes):
    # morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    # hashMap = {}
    # for i in range(97, 123):
    #     hashMap[chr(i)] = morse[i - 97]

    hashMap = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}

    seen = set()
    for code in codes:
        newList = []
        for i in code:
            newList.append(hashMap[i])
        seen.add(''.join(newList))

    return len(seen)
    


print(uniqueMorseCode(["gin","zen","gig","msg"]))
