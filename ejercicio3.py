
estudiantes = []

continuar = 0

while continuar==0:

    menu = int(input('ingrese:\n1.-para agregar un estudiante.\n2.-para eliminar un estudiante.\n3.-para mostrar los estudiantes de la base'))
    
    if menu==1:
        alumno=[]
        nombre=input('ingrese el nombre del estudiante:\n==>')
        cedula= int(input('ingresa la edad del estudiante:\n==>'))
        edad=int(input('ingresa la edad del estudiante:\n==>'))

        materias=[]

        mas_materias=0
        while mas_materias==0:
            nombre_materia=input('ingrese el nombre de la materia:\n==>')
            materias.append(nombre_materia)

            mas_materias=int(input('ingresa 0 si deseas agregar otra materia u otro numero si no:\n==>'))

        alumno.append(nombre)
        alumno.append(cedula)
        alumno.append(edad)
        alumno.append(materias)

        estudiantes.append(alumno)

    elif menu==2:
        for x in range(len(estudiantes)):
            print((x+1), "nombre:\n==>", estudiantes [x][0], 'cedula:\n==>', estudiantes[x][1], 'edad:\n==>', estudiantes[x][2], 'materias:\n==>', estudiantes[x][3])


        indice = int(input('ingrese el indice del estudiante a eliminar:\n==>'))

        estudiantes.pop(indice-1)


    elif menu==3:

        for x in range(len(estudiantes)):
            print((x+1), "nombre:\n==>", estudiantes [x][0], 'cedula:\n==>', estudiantes[x][1], 'edad:\n==>', estudiantes[x][2], 'materias:\n==>', estudiantes[x][3])







    continuar=int(input('ingresa 0 para continuar, sino ingresa cualquier otro numero:\n==>'))