def subSequence(str):
    if len(str) == 0:
        return [""]
    ans = subSequence(str[1:])
    x = str[0]
    final_ans = []
    for i in ans:
        final_ans.append(i)
    for i in range(len(ans)):
        rslt = x + ans[i]
        final_ans.append(rslt)
    return final_ans


n = input()
ans = subSequence(n)
print(ans)
