print("*****BIENVENIDO AL CAJERO AUTOMATICO SISMONEY*******")

estado_cuenta = 1000

def menu():
    print("***MENU PRINCIPAL***")
    print("1. Realizar una transaccion")
    print("2. Realizar un retiro")
    print("3. Realizar un deposito")
    print("4. Finalizar programa")

menu()
opcion = int(input("Ingrese la opcion a escoger: "))

if opcion == 1:
    transaccion = float(input("Cuanto desea transferir ?"))
    print(f"La transaccion que se hizo fue de: {str(transaccion)}")
elif opcion == 2:
    retiro = float(input("Cuanto desea retirar ?: "))
    if retiro > estado_cuenta:
        print(f"No cuenta con el saldo suficiente")
    else:
        estado_cuenta -= retiro
        print(f"El estado de cuenta ahora es: {str(estado_cuenta)}")
elif opcion == 3:
    deposito = float(input("Ingresa el monto a depositar: "))
    estado_cuenta += deposito
    print(f"Ahora tiene: {str(estado_cuenta)}")
elif opcion == 4:
    print("Gracias por utilizar el cajero automatico")
    print(f"Su saldo final es: {str(estado_cuenta)}")
else: 
    print("Error ! Ingrese una opcion valida")