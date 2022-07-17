

def maxRepeating(sequence: str, word: str) -> int:
    k  = len(word)
    count = 0
    
    for i in range(len(sequence) - k + 1):
        x = sequence[i:k+i]
        if sequence[i:k+i] == word:
            count += 1
    
    return count



sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
word = "aaaba"

print(maxRepeating(sequence, word))