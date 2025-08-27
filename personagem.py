from estilos import *
from racas import *
from bases import Estilo, Raca, Classe

class Personagem:
    def __init__(self, estilo: Estilo, raca: Raca, classe: Classe):   
        self.atributos = {
            "forca": None,
            "destreza": None,
            "constituicao": None,
            "inteligencia": None,
            "sabedoria": None,
            "carisma": None
        }
        self.estilo = estilo
        self.raca = raca
        self.classe = classe

        valores = self.estilo.gerar_atributos()
        for i, chave in enumerate(self.atributos, start=0):
            self.atributos[chave] = valores[i]

    def mostrar_atributos_personagem(self):
        for i, (nome, valor) in enumerate(self.atributos.items(), start=1):
            print(f"{i}.{nome}: {'Vazio' if valor is None else valor}")

    def mostrar_atributos_raca(self):
        print("HABILIDADES DE RAÇA:")
        for (nome, valor) in self.raca.habilidades.items():
            print(f"{nome}: {'Vazio' if valor is None else valor}")
        print("BONUS DE RAÇA:")
        for i in self.raca.bonus: print("-",i)

    def mostrar_atributos_classe(self):
        print("Estatísticas DE CLASSE:")
        for (nome, valor) in self.classe.estatisticas.items():
                print(f"{nome}: {'Vazio' if valor is None else valor}")
        print("HABILIDADES DE CLASSE:")
        for (nome, valor) in self.classe.habilidades_classe.items():
                print(f"{nome}: {'Vazio' if valor is None else valor}")
        print("LIMITES DE ITENS DE CLASSE:")
        for (nome, valor) in self.classe.limite_itens.items():
                print(f"{nome}: {'Nenhum' if valor[0] is None else valor}")
