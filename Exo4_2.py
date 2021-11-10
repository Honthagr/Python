from Exo4_1 import est_premier

x = int(input("Entrez un entier : "))
A = []
for i in range(2,x):
    if est_premier(i):
        A.append(i)
print(A)
