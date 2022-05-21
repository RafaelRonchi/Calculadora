n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print(" ")
print("1: + ")
print("2: - ")
print("3: * ")
print("4: / ")
print(" ")
n = float(input("Escolha a operação (1,2,3 ou 4): "))

if n == 1:
    x = n1+n2
    print(" %.2f + %.2f : %.2f" % (n1, n2, x))
elif n == 2:
    x = n1 - n2
    print(" %.2f - %.2f : %.2f" % (n1, n2, x))
elif n == 3:
    x = n1*n2
    print(" %.2f * %.2f : %.2f" % (n1, n2, x))
elif n== 4:
    x = n1 / n2
    print(" ")
    print(" %.2f / %.2f : %.2f" % (n1, n2, x))