def getString(d):
    if d == 2:
        return "abc"
    if d == 3:
        return "def"
    if d == 4:
        return "ghi"
    if d == 5:
        return "jkl"
    if d == 6:
        return "mno"
    if d == 7:
        return "pqrs"
    if d == 8:
        return "tuv"
    if d == 9:
        return "wxyz"
    return " "


def keypad(n):
    if n == 0:
        arr = [" "]
        return arr
    n1 = n // 10
    rem = n % 10
    ans = keypad(n1)
    str1 = getString(rem)
    final_str = []
    for i in ans:
        for j in str1:
            optn = j + i
            final_str.append(optn)

    return final_str


n = int(input())
ans = keypad(n)
for s in ans:
    print(s)
