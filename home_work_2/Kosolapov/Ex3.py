def is_prime(a):
    flag = 0
    b = a**0.5
    for i in range(2,round(b)+1):
        if a % i == 0:
            flag = 1
            break
    if flag == 0:
        return True
    else:
        return False
    
