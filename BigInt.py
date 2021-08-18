class BigInt():
    def __init__(self, data):
        # get data as string
        self.data = str(data)

    def __str__(self):
        # return data for printing
        return self.data

    # sum function
    def __add__(self, other):
        # get left side and right side of the operator
        a = self.data
        b = other.data

        # handling the negetive sign of the number
        neg_flag = False

        # if both numbers are negative

        if a[0] == '-' and b[0] == '-':
            neg_flag = True
            a = list(a)
            b = list(b)
            
            # remove the negetive sign from the number string
            a.pop(0)
            b.pop(0)


        # if one of the numbers is negative
        
        elif str(a)[0] == '-':
            # remove the negative sign from the number 
            # and change the operator to sub (-)
            a = a.replace('-', '')
            res = BigInt(b) - BigInt(a)
            return BigInt(res)

        elif b[0] == '-':
            # remove the negative sign from the number 
            # and change the operator to sub (-)
            b = b.replace('-', '')
            res = BigInt(a) - BigInt(b)
            return BigInt(res) 
        
        # if bothe numbers are positive
        else:
            a , b = list(a), list(b) 

        # seting up the start values and set the up and down value
        # by their lenth 
        up = a
        down = b

        carry = 0
        total_sum = []
        
        min_len = min(len(a), len(b))

        if min_len == len(a):
            up = b
            down = a

        # poping all the numbers one by one and add them to each other
        while len(up) > 0 or carry > 0:
            
            # handling the carry and the sum
            if len(down) > 0:
                local_sum = int(down.pop()) + int(up.pop()) + carry
            
            elif len(up) == 0:
                local_sum = carry

            else:
                local_sum = int(up.pop()) + carry

            # handling the carry and the mod 
            if local_sum >= 10:
                sum_mod = local_sum % 10

                carry = int( (local_sum - sum_mod) / 10 )

                total_sum.insert(0, sum_mod)

            else:
                total_sum.insert(0, local_sum)
                carry = 0 
        
        # convert result list to string
        res = ''
        if neg_flag:
            res += '-'
        for num in total_sum:
            res += str(num)

        return BigInt(res)

    # subtrac function
    def __sub__(self, other):
        # convert string to list for hadling indexes
        a = list(self.data)
        b = list(other.data)

        up = a
        down = b
        sign = ''

        # check for up and down of the number and sign
        if  len(down) > len(up):
            up, down = down, up
            sign = '-'

        # check to see with number is going up and wich is
        # going down
        elif len(down) == len(up):
            for i in range(len(up)):

                if int(up[i]) < int(down[i]):
                    # up is smaller! so we change it!!
                    up, down = down, up
                    sign = '-'
                    break

                elif int(up[i]) > int(down[i]):
                    # up is bigger so we are good!
                    break
                
        # setup starting values
        carry = 0
        total_sub = []

        # sub untill all the up numbers are gone
        while len(up) > 0 :
            
            # normaly we do this (when we still have down numbers)
            if len(down) > 0:
                up_pop = up.pop()
                down_pop = down.pop()
                local_sub = int(up_pop) - int(down_pop) - carry
                carry = 0
                # up_pop - down_pop - carry =  local_sub


            # if down numbers are finished, continue with  carry and up number
            else:
                up_pop = up.pop()
                local_sub = int(up_pop) - carry
                carry = 0
                # up_pop - carry =  local_sub
                

            if local_sub < 0:
                local_sub += 10
                carry = 1

            total_sub.insert(0, local_sub)

        # we use start flag to remove zeros from the frist of the number
        start_flag = True
        res = ''

        res += sign
        for num in total_sub:
            if start_flag and not num :
                pass

            else:
                start_flag = False
                res += str(num)
            

        # check if result is 0 
        if res == '': res = 0

        return BigInt(res)
    
    # multiply function
    def __mul__(self, other):
        # convert string to list for hadling indexes
        a = list(self.data)
        b = list(other.data)

        # handling the sign at the first of the number
        sign_flag = False

        # both of the numbers are negative
        if a[0] == '-' and b[0] == '-':
            a.pop(0)
            b.pop(0)

        # one of the is negative
        elif a[0] == '-':
            sign_flag = True
            a.pop(0)

        elif b[0] == '-':
            sign_flag = True
            b.pop(0)

        # calculating the lenth of the list for define
        # the up and down number
        min_len = min(len(a), len(b))

        up = a
        down = b
        carry = 0

        if min_len == len(a):
            up = b
            down = a

        # setting up the startup values
        z_count = 0
        all_muls = []

        while len(down) > 0 :
            # for each numbers in down number we do the multiply 

            down_pop = down.pop()
            local_mul = []
            carry = 0
            temp_up = up.copy()

            # do the multiply in here
            while len(temp_up) > 0 or carry > 0:

                try:
                    up_pop = temp_up.pop()
                    small_mul =  int(up_pop) * int(down_pop) + carry
                except:
                    small_mul = carry

                # down_pop * up_pop + carry  = small_mul

                if small_mul < 10:
                    # small_mul : carry
                    carry = 0
                    
                    local_mul.insert(0, small_mul)

                else:
                    small_mul = int(down_pop) * int(up_pop) + carry
                    mul_mod = small_mul % 10
                    carry = int((small_mul - mul_mod) / 10)
                    # print(mul_mod, '  carry: ', carry,'\n')
                    local_mul.insert(0, mul_mod)

            # add zero to the end of each multiply line
            for _ in range(z_count):
                local_mul.append(0)
            
            all_muls.append(local_mul)
            z_count += 1

        # convert each multiply list result to string
        int_muls = []
        for mul in all_muls:
            temp = ''
            for num in mul:
                temp += str(num)

            int_muls.append(temp)

        # sum all multiplys with each other
        res = BigInt(0)
        for num in int_muls:
            num = BigInt(num)
            res = res + num

        # add sign to the number if needed
        if sign_flag:
            res = '-' + str(res)
            print()
            res = BigInt(res)

        return res

    # divide function
    def __truediv__(self, other):
        # for divde we subtrac the left number 
        # for the (right number) time
        a = BigInt(self.data)
        b = BigInt(other.data)

        # set divde to 0 by default
        divide = 0
        while True:
            
            a = a - b
            
            # if the remain number is zero we add one the result
            # and finish subtracing
            if str(a) == '0':
                divide += 1
                break
            
            # if the remain number is less than a zero we just 
            # stop subtracing and return the result
            elif str(a)[0] == '-':
                break   
            
            # add one if the subtracing had done correctly
            divide += 1
               
        return BigInt(divide)

