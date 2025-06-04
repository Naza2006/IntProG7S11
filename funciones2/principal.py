import operaciones as operation

def main():
    while(True):
        operation.limpiar()
        opertion,persionar()
        menu()
        op = input("Digita una opcion: ")
        if op == '1':
            limpiar()
            num1 = int(input("Primer valor: "))
            num2 = int(input("Segundo valor: "))
            suma = sumar(num1, num2)
            print(f"{num1} + {num2} = {suma}")
            presionar()
        elif op == '2':
            operation.limpiar
            limpiar()
            num1 = int(input("Primer valor: "))
            num2 = int(input("Segundo valor: "))
            resta = restar(num1, num2)
            print(f"{num1} - {num2} = {resta}")
            presionar()
        elif op == '3':
            limpiar()
            num1 = int(input("Primer valor: "))
            num2 = int(input("Segundo valor: "))
            multiplicacion = multiplicar(num1, num2)
            print(f"{num1} * {num2} = {multiplicacion}")
            presionar()
        elif op == '4':
            limpiar()
            num1 = int(input("Primer valor: "))
            num2 = int(input("Segundo valor: "))
            divicion = dividir(num1, num2)
            print(f"{num1} / {num2} = {divicion}")
            presionar()
        elif op == '5':
            False
            break
        elif op == '6':
            x = int(input("Valor de X "))
            y = int(input("Valor de Y "))
            z = int(input("Valor de Z "))
            mult = multiplicar(2, y)
            sum = sumar(x, mult)
            div = dividir(sum, z)
            print(div)
            presionar()
main()           