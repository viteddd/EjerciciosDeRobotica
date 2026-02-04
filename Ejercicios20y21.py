#Ejercicio 20

def calcular_salario(horastrabajadas, tarifahora):
    if horastrabajadas <= 40:
        salario = horastrabajadas * tarifahora
    else:
        horas_normales = 40
        horas_extras = horastrabajadas - 40
        salario = (horas_normales * tarifahora) + (horas_extras * tarifahora * 1.5)

    return salario
horas = float(input("Ingresa las horas trabajadas: "))
tarifa = float(input("Ingresa la tarifa por hora: "))

total = calcular_salario(horas, tarifa)
print("El salario total es:", total)

#Ejercicio 21

def numero_mayor(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
n1 = float(input("Ingresa el primer numero: "))
n2 = float(input("Ingresa el segundo numero: "))
n3 = float(input("Ingresa el tercer numero: "))
mayor = numero_mayor(n1, n2, n3)
print("El numero mayor es:", mayor)

