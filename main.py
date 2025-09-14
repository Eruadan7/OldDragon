from app import *  # importa a classe pai (ou direto de onde você definiu)
# monta o map dinâmico

estilos_map = {cls().nome.lower(): cls for cls in Estilo.__subclasses__()}

print("disponíveis no map:")
for chave, classe in estilos_map.items():
    print(f"{chave} -> {Estilo.__name__}")