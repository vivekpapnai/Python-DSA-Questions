"""
You are given a string 'STR'. You have to convert the first alphabet of each word in a string to UPPER CASE.
"""
"""
https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118626/offering/1377975
"""


def convertString(str):
    # Write your code here
    flag = True
    str1 = ""
    for i in range(len(str)):
        if flag:
            str1 += str[i].upper()
            flag = False

        elif str[i] == " ":
            str1 += str[i]
            flag = True

        else:
            str1 += str[i]

    return str1


str = input()
print(convertString(str))