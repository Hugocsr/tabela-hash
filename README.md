# tabela-hash
Crie as classes TabelaHash e NohHash e um programa principal em Python:
- O construtor da classe TabelaHash deverá receber uma função que deverá ser utilizada posteriormente
para retornar a posição da tabela;
- A classe NohHash deve ter os atributos: idNoh e uma lista listaDados, sendo que o idNoh será
utilizado pela função de hash para o cálculo da posição na tabela hash, assim como para a pesquisa de
elementos;
- A tabela hash deverá armazenar uma lista de nós para cada entrada da tabela. Portanto, as colisões que
porventura ocorram deverão ser pesquisadas na respectiva lista de acordo com o resultado da função de
hash;
- O uso da classe TabelaHash deverá ser precedido pela criação de uma função de hash que deverá ser
repassada ao seu método __init__.
- Criar o método Insere(noh), sendo noh um objeto da classe NohHash. Esta função deverá inserir o nó
na posição correta de acordo com a função de hash. Use uma lista de nós para tratar as colisões;
- Criar o método Atualiza(noh), sendo noh um objeto da classe NohHash. Este método deverá substituir
o nó armazenado anteriormente pelo noh fornecido;
- Criar o método Exclui(noh), sendo noh um objeto da classe NohHash. Este método deverá apagar o nó
fornecido através do uso do seu identificador (idNoh);
- Criar o método Pesquisa(noh), sendo noh um objeto da classe NohHash. Este método deverá retornar a
lista de dados (listaDados) armazenada dentro do nó;
- A classe TabelaHash deverá armazenar todos os dados em uma única lista em python. Os nós serão
armazenados nesta lista pelo seu programa. Lembre-se que podem ocorrer colisões de elementos na
mesma posição da tabela, portanto você deve armazenar uma lista de nós em cada posição (sua tabela
hash será uma “lista de listas de nós”).
Por fim, use as classes TabelaHash e NohHash em um programa principal para tratar as entradas e
saídas conforme segue:
