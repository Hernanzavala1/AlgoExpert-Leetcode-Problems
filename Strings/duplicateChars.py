
def URLify(str, lenght):
    str = str.replace(" ", "%20")
    return str
def palindromePerm(str):
    pass
# def OneWay(str1, str2):
#     strLengthDif = abs(len(str1) - len(str2))
#       #same length case
#     if(strLengthDif == 0):
#         if(str1 == str2):
#             return True
#         else:
#             # find out what character is different or if more than 1 character
#             difCount=0
#             for i in range(len(str1)):
#                 if(str1[i] != str2[i]):
#                     difCount +=1
#             if(difCount == 1):
#                 return True
#             else:
#                 return False
#     elif(strLengthDif == 1):
#         #find out of remove a character or insert one. The length could be diff by one but have all different chars so we must check that the difference is only one char
#         difCount=0
#         print(min(len(str1), len(str2)))
#         for i in range(min(len(str1),len(str2))):
#             if(str1[i] != str2[i]):
#                 difCount +=1
#         if(difCount >1):
#             return False
#         return True
#     else:
#         return False 
#     #
def strComp(str1):
    currentChar=str1[0]
    count=0
    result = ""
    for i in range(len(str1)):
        if(str1[i] != currentChar):
            result += currentChar + str(count)
            currentChar = str1[i]
            count=0
        count +=1
    result += currentChar + str(count)
    return result

def isPalindrome(str1):
    copy = str1[-1::-1]
    return copy == str1
print(isPalindrome("level"))