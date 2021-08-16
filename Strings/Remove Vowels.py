def removeVowels(inputString):
    # Write your code here.
    resultString = ""
    for i in inputString:
        if i != 'a' or i != 'e' or i != 'i' or i != 'o' or i != 'u':
            resultString += i
        elif i != 'A' or i != 'E' or i != 'I' or i != 'O' or i != 'U':
            resultString += i


    return resultString


str1 = input()
print(removeVowels(str1))
