## Changelog

### 1

- As interfaces estão no mesmo nível de Personagem, no nível mais raso
- Os estilos dependem das duas últimas
- Na main, só importamos e instanciamos os estilos, chamando os métodos

### 2

- Mudanças na estrutura do projeto
- Resolvi transformar Personagem na classe principal, em vez de servir apenas de herança, pos estava indo pelo caminho errado
- Criei uma interface Estilo com o método abstrato gerar_atributos
- Os estilos herdam essa interface e implementam o método conforme sua necessidade
- Armazenei as funções que se repetem em um arquivo utils.py
- A estrutura ficou assim, do nível mais alto até a raiz:
    interfaces -> estilos e utils.py -> Personagem e main

