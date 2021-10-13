x = int(input("Entrez un entier : "))

a = int(x**1/2)

for i in range(a):
    if x%a != 0:
        print(x ," est premier")
        break
else:
    print(x, "n'est pas premier")