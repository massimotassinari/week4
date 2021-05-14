

numero = input('ingrese un numero:\n==>')

if numero.isnumeric() and len(numero) == 3:
 

    if (int(numero[0])<int(numero[1])<int(numero[2])):

        print('si')

    else:
        print('NO')

else:
    print('no introdujo un numero entero, ingrese un numero de tres digitos')
