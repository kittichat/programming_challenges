n = int(input().strip())


if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and n in range(2,6):
    print("Not Werid")
elif n % 2 == 0 and n in range(6,21):
    print("Werid")
elif n % 2 == 0 and n > 20:
    print("Not Werid")
