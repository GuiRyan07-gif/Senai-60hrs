# --- PARTE 1: Contador de 0 a 1000 ---
print("Iniciando contagem de 0 a 1000...")
contagem = 0
while contagem <= 1000:
    print(contagem)
    contagem += 1

print("-" * 30)

# --- PARTE 2: Sistema de Lista de Nomes ---
nomes = []
i = 1

print("Agora, vamos cadastrar 10 nomes:")
while i <= 10:
    nome = input(f"Digite o {i}º nome: ")
    nomes.append(nome)
    i += 1

print("\nExibindo a lista final de nomes:")
posicao = 0
while posicao < len(nomes):
    print(f"Pessoa {posicao + 1}: {nomes[posicao]}")
    posicao += 1
