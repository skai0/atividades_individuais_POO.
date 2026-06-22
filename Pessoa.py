class Pessoa:
    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura

    def __str__(self):
        return f"Nome: {self.nome} | Altura: {self.altura:.2f} m"

    def __gt__(self, other):
        return self.altura > other.altura

    def __lt__(self, other):
        return self.altura < other.altura


# Programa principal
qtd = int(input("Quantas pessoas serão cadastradas? "))

lst = []

for i in range(qtd):
    nome = input(f"Nome da pessoa {i+1}: ")
    altura = float(input(f"Altura da pessoa {i+1}: "))
    lst.append(Pessoa(nome, altura))

print("Pessoa mais alta:")
print(max(lst))

print("Pessoa mais baixa:")
print(min(lst))

print("Pessoas ordenadas por altura:")
for pessoa in sorted(lst):
    print(pessoa)