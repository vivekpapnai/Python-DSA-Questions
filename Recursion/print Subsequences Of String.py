def printSubsequence(input1, output):
    if len(input1) == 0:
        print(output)
        return
    printSubsequence(input1[1:], output)
    output += input1[0]
    printSubsequence(input1[1:], output)


str = input()
printSubsequence(str,"")