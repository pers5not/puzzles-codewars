def gap(g, m, n):
    previous_num = n
    for i in range(m, n + 1):
        if is_prime(i):
            if i - previous_num == g:
                return [previous_num, i]
            previous_num = i   
    return None

def is_prime(x):
    for i in range(2, int(x**.5 + 1)):
        if x % i == 0:
            return False
    return True

print(gap(2,100,110))
print(gap(4,100,110))
print(gap(6,100,110))
print(gap(8,300,400))
print(gap(10,300,400))
print(gap(2,100,103))