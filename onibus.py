class Onibus:
    def __init__(self, placa, nome_motorista, num_assentos):
        self.placa = placa
        self.nome_motorista = nome_motorista
        self.assentos = [False] * num_assentos

    def __len__(self):
        return len(self.assentos)

    def __getitem__(self, indice):
        if indice < 0 or indice >= len(self.assentos):
            raise IndexError(
                f"Escolha um valor entre 0 e {len(self.assentos)-1}"
            )
        return self.assentos[indice]

    def __setitem__(self, indice, valor):
        if indice < 0 or indice >= len(self.assentos):
            raise IndexError(
                f"Escolha um valor entre 0 e {len(self.assentos)-1}"
            )

        if not isinstance(valor, bool):
            raise TypeError("Valor deve ser booleano (True/False)")

        self.assentos[indice] = valor

    def __str__(self):
        ocupados = self.assentos.count(True)
        livres = self.assentos.count(False)

        return (
            f"Ônibus (Placa: {self.placa}) - Motorista: {self.nome_motorista}\n"
            f"Assentos totais: {len(self.assentos)}\n"
            f"Assentos ocupados: {ocupados}\n"
            f"Assentos livres: {livres}"
        )


# Programa de teste
onibus = Onibus("ABC-1234", "Michael Kaiser", 10)

# Ocupando alguns assentos
onibus[0] = True
onibus[3] = True
onibus[5] = True

print(onibus)

print("\nQuantidade de assentos:", len(onibus))
print("Assento 3:", onibus[3])
print("Assento 2:", onibus[2])