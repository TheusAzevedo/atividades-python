# PROGRAMA PRINCIPAL
print("=" * 50)
print("LISTA DE NOMES")
print("=" * 50)


nomes = []


print("\nDigite 5 nomes:")
for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

print("\n" + "=" * 50)


print("NOMES CADASTRADOS:")
for nome in nomes:
    print(f"  - {nome}")

print("\n" + "=" * 50)


total = len(nomes)
print(f"Total de nomes cadastrados: {total}")

print("=" * 50)


pesquisa = input("\nDigite um nome para pesquisar: ")

if pesquisa in nomes:
    print(f"'{pesquisa}' esta na lista!")
    # Mostra a posição do nome
    posicao = nomes.index(pesquisa)
    print(f"Posicao: {posicao + 1} lugar")
else:
    print(f"'{pesquisa}' NAO esta na lista!")

print("=" * 50)