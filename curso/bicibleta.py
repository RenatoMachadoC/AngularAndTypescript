class Bibibleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.disponivel = True
        
    def buzinar(self):
        print("Buzinando")
        
    def parar(self):
        print("Parando")
        
    def correr(self):
        print("Correndo")
        
        
b1 = Bibibleta("azul", "caloi", 2020, 500)

b1.buzinar()
b1.parar()
b1.correr()
b1.parar()