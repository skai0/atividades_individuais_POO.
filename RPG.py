import random

# Superclasse
class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def tomar_dano(self, valor):
        self.vida -= valor
        if self.vida < 0:
            self.vida = 0


# Subclasse Mago
class Mago(Personagem):
    def __init__(self, nome, vida, mana):
        super().__init__(nome, vida)
        self.mana = mana

    def __str__(self):
        return f"Mago: {self.nome} | Vida: {self.vida} | Mana: {self.mana:.2f}"

    def __add__(self, valor):
        self.mana += valor
        return self.mana

    def __sub__(self, valor):
        self.mana -= valor
        if self.mana < 0:
            self.mana = 0
        return self.mana

    def __mul__(self, valor):
        self.mana *= valor
        return self.mana

    def __truediv__(self, valor):
        self.mana /= valor
        return self.mana


# Subclasse Bárbaro
class Barbaro(Personagem):
    def __init__(self, nome, vida, stamina):
        super().__init__(nome, vida)
        self.stamina = stamina
        self.furia = False

    def __str__(self):
        return (
            f"Bárbaro: {self.nome} | Vida: {self.vida} | "
            f"Stamina: {self.stamina:.2f} | Fúria: {self.furia}"
        )

    def __add__(self, valor):
        self.stamina += valor
        if self.furia:
            self.stamina += valor * 1.5
        return self.stamina

    def __sub__(self, valor):
        self.stamina -= valor

        if self.stamina <= 0 and not self.furia:
            self.furia = True
            self.stamina = 5

        return self.stamina

    def __mul__(self, valor):
        self.stamina *= valor

        if self.furia:
            self.vida += 5

        return self.stamina

    def __truediv__(self, valor):
        self.stamina /= valor
        return self.stamina


# Programa Principal
tipo = input("Escolha o personagem (Mago ou Barbaro): ").strip().lower()

nome = input("Nome: ")
vida = int(input("Vida: "))

if tipo == "mago":
    mana = float(input("Mana inicial: "))
    personagem = Mago(nome, vida, mana)
else:
    stamina = float(input("Stamina inicial: "))
    personagem = Barbaro(nome, vida, stamina)

while personagem.vida > 0:
    print("\n", personagem)
    print("1 - Tomar poção simples (+5)")
    print("2 - Tomar poção especial (*1.5)")
    print("3 - Ataque básico (-2)")
    print("4 - Ataque especial (/2)")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        personagem + 5

    elif opcao == "2":
        personagem * 1.5

    elif opcao == "3":
        personagem - 2

    elif opcao == "4":
        personagem / 2

    elif opcao == "0":
        break

    else:
        print("Opção inválida!")
        continue

    dano = random.randint(1, 10)
    personagem.tomar_dano(dano)

    print(f"\nO personagem sofreu {dano} de dano!")

    if personagem.vida <= 0:
        print(f"{personagem.nome} foi derrotado!")
        break