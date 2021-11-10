from Exo4_1 import est_premier
i = 0
while est_premier(2**2**i +1):
    i+=1
print("Le premier nombre de Fermat qui n'est pas premier est : " + str(2**2**i+1))

x = 100000 #int(input("Entrez un entier : "))

for i in range(x,x**x):
    if est_premier(i):
        print(str(i) +"est premier")
        break

y = 100000 #int(input("Entrez un entier : "))

for i in range(y,y**y):
    if est_premier(i) and est_premier(i+2):
        print("Le couple " + str(i) + " et " + str(i+2) + " est premier")
        break

z = 100000 #int(input("Entrez un entier : "))

for i in range(z,z**z):
    if est_premier(i) and est_premier(2*i+1):
        print("Le nombre Germain " + str(i) + " est premier")
        break