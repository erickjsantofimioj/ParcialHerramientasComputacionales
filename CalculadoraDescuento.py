print('!!!!!Bienvenido a su cafeteria buen sabor!!!!!')
cedula = input('Por favor digite su numero de cedula: (solo números aqui): ')
rol = input('Por favor digite su rol (Estudiante o Profesor): ')
codigo = input('Digite el codigo del producto: ')
cantidad = int(input('Digite la cantidad de unidades que llevará: '))
precio = int(input('Digite el precio del producto: '))
precio_final = 0
if rol == "estudiante":
    precio_final = precio*cantidad-precio*cantidad*0.5
    print("El:",rol,"con cedula:",cedula,", debe pagar:",precio_final,"por el producto:",codigo)
if rol == "profesor":
    precio_final = precio*cantidad-precio*cantidad*0.2
    print("El:", rol, "con cedula:", cedula, ", debe pagar:", precio_final, "por el producto:", codigo)
