from BigInt import BigInt
from random import randint
import time

a = randint(0, 10**1000)
b = randint(0, 10**1000)

t1 = time.time()

res = a * b 

t2 = time.time()
res_time1 = t2-t1

a = BigInt(a)
b = BigInt(b)

t1 = time.time()

res = a * b 

t2 = time.time()

res_time2 = t2 - t1

print('T1: ', res_time1)
print('T2: ',res_time2)
print('T_diff: ',res_time2 - res_time1)

