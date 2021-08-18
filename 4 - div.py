a = ('123')
b = ('45')


divide = 0
while True:
    # change int to BigInt in the original code
    a = int(a) - int(b)
    # print(a)
    if str(a) == '0':
        divide += 1
        break

    elif str(a)[0] == '-':
        break   

    divide += 1

print(divide)
