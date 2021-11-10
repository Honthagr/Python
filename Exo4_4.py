#x = int(input("Entre nombre :"))
A = [0,0] #Temps de vol
B = [0,0] #Temps de vol en altitude
C = [0,0] #Altitude

Compt = 0
Test = 1
for x in range(1,10000):
    i = x
    while i !=1:
        if i%2 == 0:
            i = i/2
            Compt+=1
            if i < x and Compt > B[1] and Test == 1:
                B[1] = Compt-1
                B[0] = x
                Test = 0
        else:
            i= i*3 +1
            Compt+=1
            if i > C[1]:
                C[1] = i
                C[0] = x
    if Compt > A[1]:
        A[1] = Compt
        A[0] = x
    Compt = 0
    Test = 1
print(A, "Temps de Vol maximale")
print(B, "Temps de Vol en altitude maximale")
print(C, "Altitude maximale")