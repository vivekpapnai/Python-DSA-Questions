def uniqueChar(s):
    ans = ''
    di = {}
    for char in s:
        if char not in di:
            ans += char
            di[char] = "True"
    return ans


# Main
s = input()
print(uniqueChar(s))
