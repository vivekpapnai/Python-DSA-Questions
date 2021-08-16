def isCorrect(tag):
    if len(tag)<=3:
        return False
    if tag[:2] == '</' and tag[-1] == '>':
        for i in tag[2:len(tag) - 1]:
            if 'a' <= i <= 'z' or '0' <= i <= '9':
                continue
            else:
                return False
        return True
    else:
        return False

t = int(input())
while t > 0:
    tag = input()
    if isCorrect(tag):
        print('sucess')
    else:
        print('error')
    t -= 1
