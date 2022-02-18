def spy_game(n):
    for i in range(len(n)):

        if n[i] == 0:
            list.append(n[i])
        elif n[i] == 7 and len(list) >= 2:
            return True

    return False

n = list(map ( int , input().split()))

list = []

if spy_game(n) == True:
    print("True")
else:
    print("False")