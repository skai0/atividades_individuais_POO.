class Carteira():
    def __init__(self, moeda, saldo):
        self.moeda = moeda
        self.saldo = saldo

    def converter_yuan(self, valor_yuan):
        if self.moeda == "USD":
            return valor_yuan * 0.14
        elif self.moeda == "BRL":
            return valor_yuab * 0.85
        elif self.moeda == "CNY":
            return valor_yuan 
    
    def __add__(self, valor_yuan):
        valor_convertido = self.converter_yuan(valor_yuan):
        return self.saldo + valor_convertido

    def __sub__(self, valor_yuan):
        valor_convertido = self.converter_yuan(valor_yuan):
        return self.saldo - valor_convertido

      carteira_usd = Carteira("USD", 10.0)
      print("Soma de carteira USD + 50 yuan =", carteira_usd + 50.0)

    carteira_brl = Carteira("BRL", 20.0)
    print("Soma de carteira BRL + 50 yuan =", carteira_brl + 50.0)

    carteira_cny = Carteira("CNY", 100.0)
      print("Subtração de carteira CNY - 30 yuan =", carteira_cny - 30.0)



    
