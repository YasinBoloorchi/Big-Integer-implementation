a = list('123')
b = list('3490')

up = a
down = b

sign = ''

print('  ',up)
print('- ',down)
print('-'*20)

# check for down and up
if  len(down) > len(up):
    up, down = down, up
    sign = '-'

elif len(down) == len(up):
    for i in range(len(up)):
        if int(up[i]) < int(down[i]):
            # print('up is smaller! so we change it!!')
            up, down = down, up
            sign = '-'
            break

        elif int(up[i]) > int(down[i]):
            # print('up is bigger so we are good!')
            break

carry = 0
total_sub = []

while len(up) > 0 :
    
    if len(down) > 0:

        up_pop = up.pop()
        down_pop = down.pop()
        local_sub = int(up_pop) - int(down_pop) - carry

        print(str(up_pop), ' - ', str(down_pop), ' - ' , str(carry), ' = ', str(local_sub))
        carry = 0

    else:
        up_pop = up.pop()
        local_sub = int(up_pop) - carry
        
        print(str(up_pop), ' - ', str(carry), ' = ', str(local_sub))
        carry = 0

    if local_sub < 0:
        local_sub += 10
        carry = 1
    
    total_sub.insert(0, local_sub)

start_flag = True
res = ''

res += sign
for num in total_sub:
    if start_flag and not num :
        pass
    else:
        start_flag = False
        res += str(num)

print(res)
