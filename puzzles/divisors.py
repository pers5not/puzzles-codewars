def divisors(number):
    check_num = 0
    for num in range(1, number+1):
        if (number % num == 0):
            if num * check_num == number:
                return (num, check_num)
            else:
                check_num = num


print(divisors(4895))
