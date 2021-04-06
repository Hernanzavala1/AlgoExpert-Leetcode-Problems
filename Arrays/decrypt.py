def encrypt(word):
    letterCodes = [ord(i)  for i in word]
    letterCodes[0] += 1
    for i in range(1, len(letterCodes)):
        letterCodes[i]  += letterCodes[i -1] 
    for i in range(len(letterCodes)):
        while (letterCodes[i] not in range(ord('a'), (ord('z') + 1))):
            letterCodes[i] -= 26
    result = [chr(i) for i in letterCodes]
    return ''.join(result)
def decrypt(word):
    letterCodes  = [ord(i) for i in word]
    previous = letterCodes[0]
    letterCodes[0] -= 1
    letterCodes[0] = bringIntoRange(letterCodes[0])
    for i in range(1, len(letterCodes)):
        temp = letterCodes[i]
        letterCodes[i] -= previous
        letterCodes[i] = bringIntoRange(letterCodes[i])
        previous =  temp
    result = [chr(i) for i in letterCodes]
    return ''.join(result)
def bringIntoRange(code):
    while(not(code >= 97 and code <= 122)):
        code += 26
    return code
print(decrypt("dnotq"))