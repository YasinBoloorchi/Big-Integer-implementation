a = list('-123')
b = list('-3490')

sign = ''
if a[0] == '-' and b[0] == '-':
    print('1# if')
    sing = '-'
    a.pop(0)
    b.pop(0)


elif a[0] == '-':
    print('2# if')
    a.pop(0)
    res = int(b) - int(a)


elif b[0] == '-':
    print('3# if')
    b.pop(0)
    res = int(a) - int(b)





min_len = min(len(a), len(b))

up = a
down = b

carry = 0
total_sum = []

if min_len == len(a):
    up = b
    down = a

print('  ',up)
print('+ ',down)
print('-'*20)


while len(up) > 0 or carry > 0:
    print()

    if len(down) > 0:
        up_pop = up.pop()
        down_pop = down.pop()
        local_sum = int(down_pop) + int(up_pop) + carry

        print(str(up_pop), ' + ', str(down_pop), ' + ' , str(carry), ' = ', str(local_sum))

    elif len(up) == 0:
        local_sum = carry
        print(str(up_pop), ' + ', str(down_pop), ' + ' , str(carry), ' = ', str(local_sum))

    else:
        local_sum = int(up.pop()) + carry
        print(str(up_pop), ' + ' , str(carry), ' = ', str(local_sum))

    if local_sum >= 10:
        sum_mod = local_sum % 10

        carry = int( (local_sum - sum_mod) / 10 )

        total_sum.insert(0, sum_mod)

    else:
        total_sum.insert(0, local_sum)
        carry = 0 
    

try:
    print('nicee')
    print(res)

except:
    res = ''
    res += sign
    print(sign)
    for num in total_sum:
        res += str(num)

    print(res)