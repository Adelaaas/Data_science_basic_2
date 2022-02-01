def is_prime(n):
    answer = True
    for i in range(2, n):
        if n % i == 0:
            answer = False
    return(answer)
print(is_prime(int(input())))
