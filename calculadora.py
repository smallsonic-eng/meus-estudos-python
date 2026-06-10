print("--- CALCULADORA ---")
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
print("1-Soma | 2-Subtração")
op = input("Escolha: ")
if op == '1':
    print(f"Resultado: {n1 + n2}")
elif op == '2':
    print(f"Resultado: {n1 - n2}")
else:
    print("Opção inválida!")
  
