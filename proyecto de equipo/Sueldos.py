#Mensaje de bienvenida
print("Hola!! Bienvenido a tu consulta de salario, Dime, ¿Que puesto tienes?")

#Declaracion de la funcion global
def seleccion_de_puesto():
    print("1)Gerente\n2)Coordinador\n3)Obrero..... \n(Selecciona tu puesto correspondiente)")
    puesto=input().upper()
    
#CONDICIONAL DE PUESTO SELECCIONADO (LEE Y VALIDA EL PUESTO INGRESADO)
    if puesto != "GERENTE" and puesto != "OBRERO" and puesto != "COORDINADOR":
        print("\nELIJA UNA OPCION VALIDA POR FAVOR!!!\n")
        seleccion_de_puesto()
        
#MENSAJE DE CONFIRMACION
    else:
        print("\nTu puesto es "+puesto+"\n¿Es correcto ese dato?(Y/N)")
        conf=input().upper()
        
#CONDICION EN CASO DE HABER CONFIRMADO PUESTO
        if conf == "Y":
            
#INGRESA DATOS DE EMPLEADO
            if puesto == "GERENTE":
                nombre = input("INGRESE SU NOMBRE POR FAVOR: ").upper()
                apellidos = input("INGRESE APELLIDOS POR FAVOR: ").upper()
                salario_inicial = 24000
                SegSoc= salario_inicial * 0.062
                IVA=salario_inicial * 0.16
                ifv = input("¿Cuenta con infonavit? (Y/N) ").upper()
                if ifv == "Y":
                    
                    #DESGLOSE DE SALARIO, IMPUESTOS Y OTRAS PRESTACIONES SI CUENTA CON INFONAVIT
                    Infonavit= salario_inicial * 0.05
                    salario_final = salario_inicial -SegSoc - Infonavit- IVA 
                    print("\n\nTus datos son :\nNombre: "+nombre+"\nApellidos: "+apellidos+"\nSalario mensual (sin impuestos): "+"$"+str(salario_inicial))
                    print("Tu Descuento de Seguro Social equivale a: "+"$"+str(SegSoc))
                    print("Tu descuento de vivienda : "+"$"+str(Infonavit))
                    print("IVA: "+str(IVA))
                    print ("Tu nuevo salario neto mensual es de: "+ "$"+str(salario_final))
                else:
                    
                    #DESGLOSE DE SALARIO, IMPUESTOS Y OTRAS PRESTACIONES SI NO CUENTA CON INFONAVIT
                    salario_final = salario_inicial -SegSoc -  IVA 
                    print("\n\nTus datos son :\nNombre: "+nombre+"\nApellidos: "+apellidos+"\nSalario mensual (sin impuestos): "+"$"+str(salario_inicial))
                    print("Tu Descuento de Seguro Social equivale a: "+"$"+str(SegSoc))
                    print("IVA: "+str(IVA))
                    print ("Tu nuevo salario neto mensual es de: "+"$"+ str(salario_final))
                    
            #INGRESA DATOS DE EMPLEADO
            elif puesto == "COORDINADOR":
                nombre = input("INGRESE SU NOMBRE POR FAVOR: ").upper()
                apellidos = input("INGRESE APELLIDOS POR FAVOR: ").upper()
                salario_inicial = 15000
                SegSoc= salario_inicial * 0.062
                IVA=salario_inicial * 0.16
                ifv = input("¿Cuenta con infonavit? (Y/N) ").upper()
                if ifv == "Y":
                    
                    #DESGLOSE DE SALARIO, IMPUESTOS Y OTRAS PRESTACIONES SI CUENTA CON INFONAVIT
                    Infonavit= salario_inicial * 0.05
                    salario_final = salario_inicial -SegSoc - Infonavit- IVA 
                    print("\n\nTus datos son :\nNombre: "+nombre+"\nApellidos: "+apellidos+"\nSalario mensual (sin impuestos): "+"$"+str(salario_inicial))
                    print("Tu Descuento de Seguro Social equivale a: "+"$"+str(SegSoc))
                    print("Tu descuento de vivienda : "+"$"+str(Infonavit))
                    print("IVA: "+str(IVA))
                    print ("Tu nuevo salario neto mensual es de: "+"$"+ str(salario_final))
                else:
                    
                    #DESGLOSE DE SALARIO, IMPUESTOS Y OTRAS PRESTACIONES SI NO CUENTA CON INFONAVIT
                    salario_final = salario_inicial -SegSoc -  IVA 
                    print("\n\nTus datos son :\nNombre: "+nombre+"\nApellidos: "+apellidos+"\nSalario mensual (sin impuestos): "+"$"+str(salario_inicial))
                    print("Tu Descuento de Seguro Social equivale a: "+"$"+str(SegSoc))
                    print("IVA: "+str(IVA))
                    print ("Tu nuevo salario neto mensual es de: "+"$"+ str(salario_final))
                    
            #INGRESA DATOS DE EMPLEADO
            elif puesto == "OBRERO":
                nombre = input("INGRESE SU NOMBRE POR FAVOR: ").upper()
                apellidos = input("INGRESE APELLIDOS POR FAVOR: ").upper()
                salario_inicial = 6000
                SegSoc= salario_inicial * 0.062
                IVA=salario_inicial * 0.16
                ifv = input("¿Cuenta con infonavit? (Y/N) ").upper()
                if ifv == "Y":
                    #DESGLOSE DE SALARIO, IMPUESTOS Y OTRAS PRESTACIONES SI CUENTA CON INFONAVIT
                    Infonavit= salario_inicial * 0.05
                    salario_final = salario_inicial -SegSoc - Infonavit- IVA 
                    print("\n\nTus datos son :\nNombre: "+nombre+"\nApellidos: "+apellidos+"\nSalario mensual (sin impuestos): "+"$"+str(salario_inicial))
                    print("Tu Descuento de Seguro Social equivale a: "+"$"+str(SegSoc))
                    print("Tu descuento de vivienda : "+"$"+str(Infonavit))
                    print("IVA: "+str(IVA))
                    print ("Tu nuevo salario neto mensual es de: "+ "$"+str(salario_final))
                else:
                    #DESGLOSE DE SALARIO, IMPUESTOS Y OTRAS PRESTACIONES SI NO CUENTA CON INFONAVIT
                    salario_final = salario_inicial -SegSoc -  IVA 
                    print("\n\nTus datos son :\nNombre: "+nombre+"\nApellidos: "+apellidos+"\nSalario mensual (sin impuestos): "+"$"+str(salario_inicial))
                    print("Tu Descuento de Seguro Social equivale a: "+"$"+str(SegSoc))
                    print("IVA: "+str(IVA))
                    print ("Tu nuevo salario neto mensual es de: "+"$"+ str(salario_final))
            
            #SI NO SE CUMPLE NINGUNA DE LAS CONDICIONES DE PUESTO
            else:
                print("INGRESE UNA OPCION VALIDA POR FAVOR")
                seleccion_de_puesto()
        
        #SI NO SE ESCRIBE CORRECTAMENTE EL PUESTO
        else:
            print("SELECCIONA TU PUESTO CORRECTAMENTE....")
            seleccion_de_puesto()
#INICIALIZA LA FUNCION GLOBAL
seleccion_de_puesto()