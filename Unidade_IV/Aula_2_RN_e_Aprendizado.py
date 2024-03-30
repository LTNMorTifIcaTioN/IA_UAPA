# Redes Neurais e Aprendizado
"""
Aprendizado em Redes Neurais
> A aprendizagem é um processo pelo qual os parâmetros livres de uma rede neural são adaptados por meio de um processo de
estimulação pelo ambiente no qual a rede está inserida;

> Parâmetros Livres: pesos de entrada de cada sinal e o valor do limiar;
> Adaptação dos Parâmetros Livres: Processo de ajuste dos valores tanto de pesos quanto de limiares com base nos
resultados obtidos;
> Estimulação pelo Ambiente: Estímulos providos por dados de entrada, cuja saída desejada é conhecida;

> Supervisionado: indica explicitamente um comportamento bom ou ruim;
> Não-supervisionado: não existe um supervisor em relação ao conjunto de treinamento, ou seja, os dados são
não rotulados;

Tipos de Aprendizado:
> Aprendizado por Correção de Erro
    Função de Erro: é o resultado da diferença entre o resultado obtido e o resultado esperado;
> Aprendizado por Memória: a correção dos pesos se dá pela construção de um vetor de duplas, que contém duplas de
valores de entra e valores desejados de saída;
> Aprendizado Hebbiano: o peso de uma sinapse é aumentado se ambos os neurônios são excitados simultaneamente;
> Aprendizado Competitivo: os neurônicos de saída de uma rede neural competem entre si para se tornarem ativos. Somente
um neurônio de saída fica ativo em um determinado instante;
> Aprendizado de Boltzmann: esse mecanismo não enxerga os neurônios individualmente, mas cim a rede como um to.do;

Perceptron
> Elemento capaz de aprendizado supervisionado;
> Atua em classificadores binários;
> Utiliza uma função linear de previsão;
"""