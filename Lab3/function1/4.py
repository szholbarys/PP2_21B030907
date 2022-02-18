def filter_prime(list):
    cnt = 0
    list1 = []

    for i in range(len(list)):
        cnt = 0
        for j in range(1 ,list[i]):
            if list[i] % j == 0:
                cnt += 1

        if cnt == 1:
            list1.append(list[i])

    return list1

n = input().split()

x = 0
list = []

for i in range(len(n)):
    list.append(int(n[i]))


print(*(filter_prime(list)))