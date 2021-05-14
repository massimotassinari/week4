# multiplicacion de un escalar por uan matriz

A =[

    [1,4,6],
    [4,2,5],
    [6,5,3]

]

numero= int(input('ingrese un numero:\n==>'))

R=[]
for x in range(len(A)):
    ar = []
    for y in range(len(A[x])):

        ar.append(numero*A[x][y])

    R.append(ar)

print(R)