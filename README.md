## Changelog

### 1

- As interfaces estão no mesmo nível de Personagem, no nível mais raso
- Os estilos dependem das duas últimas
- Na main, só importamos e instanciamos os estilos, chamando os métodos

### 2

- Mudanças na estrutura do projeto
- Resolvi transformar Personagem na classe principal, em vez de servir apenas de herança, pois estava indo pelo caminho errado. Ela tem como parâmetro "estilo: Estilo"
- Criei uma interface Estilo com o método abstrato gerar_atributos
- Os estilos herdam essa interface e implementam o método conforme sua necessidade
- Armazenei as funções que se repetem em um arquivo utils.py

### 3

- Foi adicionada a classe abstrata Raca que agora fica no arquivo bases, junto da interface estilo
- Dentro da pasta racas, cada raça particular herda de Raca e implementa seus próprios atributos
- Personagem agora instancia uma das raças para utilizar seus atributos

### 4
  
- Adição da classe abstrata Classe. Como há subclasses aqui, existe sempre uma intermediária entre os tipos de classe. Ex: Classe->BaseGuerreiro->Guerreiro. Também são utilizadas como composição em Personagem

### 5

- FrontEnd simples para criação de personagem e inserção no banco de dados