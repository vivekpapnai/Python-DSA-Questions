def getString(n):
    if n == 2:
        return "abc"
    if n == 3:
        return "def"
    if n == 4:
        return "ghi"
    if n == 5:
        return "jkl"
    if n == 6:
        return "mno"
    if n == 7:
        return "pqrs"
    if n == 8:
        return "tuv"
    if n == 9:
        return "wxyz"

    return " "


def printKeypadCombinations(input1, output):
    if input1 == 0:
        print(output)
        return
    rem = input1 % 10
    smallNumber = input1 // 10
    rem_String = getString(rem)
    for i in rem_String:
        printKeypadCombinations(smallNumber, output+i)


n = int(input())
printKeypadCombinations(n, "")
