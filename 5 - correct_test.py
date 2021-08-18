from random import randint
from BigInt import BigInt

max_range = 1000
for i in range(max_range):
    a = randint(1, 10**1000)
    b = randint(1, 10**1000)

    bigint_a = BigInt(a)
    bigint_b = BigInt(b)

    # testing sum
    int_sum = a + b
    bigint_sum = bigint_a + bigint_b

    # testing sub
    int_sub = a - b
    bigint_sub = bigint_a - bigint_b
    
    # testing mul
    int_mul = a * b
    bigint_mul = bigint_a * bigint_b

    # testing divide
    int_dive = int(a / b)
    bigint_div = bigint_a / bigint_b

    if str(bigint_sum) == str(int_sum) and str(bigint_sub) == str(int_sub) and str(bigint_mul) == str(int_mul) and str(int_dive) == str(bigint_div):
        print(f'Ok!  {i+1}/{max_range}')
    else:
        print('There is a problem!')
        break
    
