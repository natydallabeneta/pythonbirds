"""1 - Classe Bola: Crie uma classe que modele uma bola:

a.Atributos: Cor, circunferência, material
b.Métodos: trocaCor e mostraCor"""



class CirculoPerfeito:
    def __init__(self):
        self.cor = 'Azul'
        self.cirfunferencia = 4
        self.material = 'Papel'

    def mostra_cor(self):
        return self.cor

    def troca_cor(self, cor):
        self.cor = cor



circulo_primeiro = CirculoPerfeito()
circulo_segundo = CirculoPerfeito()

circulo_segundo.troca_cor = 'Amarelo'

print(type(circulo_primeiro))
print(circulo_primeiro is circulo_segundo)
print(id(circulo_primeiro), circulo_primeiro.mostra_cor())
print(id(circulo_segundo), circulo_segundo.mostra_cor())

print(circulo_primeiro.cor, circulo_segundo.cor)



circulo_primeiro.cor = 'Amarelo'
circulo_primeiro.troca_cor = 'Verde'
print(circulo_primeiro.cor)
print(circulo_primeiro.cirfunferencia)
print(circulo_primeiro.material)

print(circulo_primeiro.cirfunferencia)


