n = int(input())
for i in range (n):
    a = int(input())
    if a <= 10:
        print("Go to work!")
    elif 10 < a and a <= 25:
        print("You are weak")
    elif 25 < a and a <= 45:
        print("Okay, fine")
    elif a > 45:
        print("Burn! Burn! Burn Young!")