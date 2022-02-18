def check_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
        return True

a = list(map(int, input().split()))
result = list(filter(lambda  x: check_prime(x), a))    
print(*result)