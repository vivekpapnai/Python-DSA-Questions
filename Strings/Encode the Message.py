def encode(message):
    # Write your code here.
    ENCODEDMESSAGE = ""
    count = 1
    for i in range(1, len(message)):
        if message[i] != message[i-1]:
            ENCODEDMESSAGE += message[i-1]
            ENCODEDMESSAGE += str(count)
            count = 1
        else:
            count += 1
    ENCODEDMESSAGE += message[len(message)-1]
    ENCODEDMESSAGE += str(count)

    return ENCODEDMESSAGE

t = int(input())
for i in range(t):
    message = input()
    print(encode(message))


