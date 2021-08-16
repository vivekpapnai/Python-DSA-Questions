"""Given a string, find and return all the possible permutations of the input string.
Note : The order of permutations are not important.
Sample Input :
abc
Sample Output :
abc
acb
bac
bca
cab
cba"""


def permutations(string, i, n):
    # Implement Your Code Here
    if i == n - 1:
        return ["" + string]
    newString = string[0:i] + string[i + 1:]
    output = permutations(newString, i + 1, n)
    rslt = []
    for j in output:
        temp = str(string[i]) + str(j)
        rslt.append(temp)
    for j in range(len(output) - 1, -1, -1):
        temp = str(string[i]) + str(string[j])
        rslt.append(temp)
    return rslt


string = input()
ans = permutations(string, 0, len(string))
for s in ans:
    print(s)
