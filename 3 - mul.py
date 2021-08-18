a = list('36')
b = list('37')

# check the sign
if a[0] == '-' and b[0] == '-':
    a.pop(0)
    b.pop(0)

elif a[0] == '-':
    sign_flag = True
    a.pop(0)

elif b[0] == '-':
    sign_flag = True
    b.pop(0)



min_len = min(len(a), len(b))

up = a
down = b

carry = 0
total_sum = []

if min_len == len(a):
    up = b
    down = a

print('  ',up)
print('* ',down)
print('-'*20)
z_count = 0
all_muls = []

while len(down) > 0 :

    down_pop = down.pop()
    local_mul = []
    carry = 0
    temp_up = up.copy()
    while len(temp_up) > 0 or carry > 0:

        try:
            up_pop = temp_up.pop()
            small_mul =  int(up_pop) * int(down_pop) + carry
        except:
            small_mul = carry

        print(down_pop , ' * ', up_pop , ' + ', carry, ' = ' , end='')

        if small_mul < 10:
            print(small_mul, '  carry: ', carry,'\n')
            carry = 0
            
            local_mul.insert(0, small_mul)

        else:
            small_mul = int(down_pop) * int(up_pop) + carry
            mul_mod = small_mul % 10
            carry = int((small_mul - mul_mod) / 10)
            print(mul_mod, '  carry: ', carry,'\n')
            local_mul.insert(0, mul_mod)



    for _ in range(z_count):
        local_mul.append(0)

    all_muls.append(local_mul)
    # print(local_mul)
    z_count += 1
    print('_'*30)

# print(all_muls)


int_muls = []
for mul in all_muls:
    temp = ''
    for num in mul:
        temp += str(num)

    int_muls.append(temp)

for num in int_muls:
    print(num)


res = 0
for num in int_muls:
    num = int(num)
    res = res + num

print('_'*20)
print(res)
