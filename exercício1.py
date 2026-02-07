# --- EXERCÍCIOS 1: CONDICIONAIS ---

# 1. Positivo, Negativo ou Zero
print("--- EXERCÍCIO 1 ---")
num1 = float(input("Digite um número: "))
if num1 > 0:
    print("O número é positivo.")
elif num1 < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

# 2. Idade para Votar
print("\n--- EXERCÍCIO 2 ---")
idade = int(input("Digite sua idade: "))
if idade >= 16:
    print("Pode votar!")
else:
    print("Não pode votar.")

# 3. Par ou Ímpar
print("\n--- EXERCÍCIO 3 ---")
valor = 42 # Variável declarada como solicitado
if valor % 2 == 0:
    print(f"O número {valor} é par.")
else:
    print(f"O número {valor} é ímpar.")

# 4. Tipo de Triângulo
print("\n--- EXERCÍCIO 4 ---")
l1 = float(input("Lado 1: "))
l2 = float(input("Lado 2: "))
l3 = float(input("Lado 3: "))

if l1 == l2 == l3:
    print("Triângulo Equilátero.")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("Triângulo Isósceles.")
else:
    print("Triângulo Escaleno.")

# 5. Múltiplo de 5 e 7
print("\n--- EXERCÍCIO 5 ---")
num5 = int(input("Digite um número: "))
if num5 % 5 == 0 and num5 % 7 == 0:
    print(f"{num5} é múltiplo de 5 e 7.")
else:
    print(f"{num5} não é múltiplo de 5 e 7 ao mesmo tempo.")

# 6. Positivo e Maior que 10
print("\n--- EXERCÍCIO 6 ---")
num6 = float(input("Digite um número: "))
if num6 > 0 and num6 > 10:
    print("O número é positivo e maior que 10.")
else:
    print("O número não atende aos dois critérios.")

# 7. Divisível por 3 ou 5
print("\n--- EXERCÍCIO 7 ---")
num7 = int(input("Digite um número: "))
if num7 % 3 == 0 or num7 % 5 == 0:
    print(f"{num7} é divisível por 3 ou 5.")
else:
    print(f"{num7} não é divisível por 3 nem por 5.") 
