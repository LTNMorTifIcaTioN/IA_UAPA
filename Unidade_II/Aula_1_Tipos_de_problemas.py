# Resolução de problemas em Inteligência Artificial
"""
Métodos Probabilísticos
> Oferece uma maneira quantitativa de codificar incertezas;
> Probabilidade é extraída dos dados;
> Redes Bayesianas;

Redes Bayesianas
> Probabilidade de ganhar na loteria: P(L)
> Probabilidade de chover: P(C)
P(L, C) = P(L) * P(C)
> Probabilidade de o chão estar molhado: P(M)
P(M|C) = P(M^C) / P(C)

P(A): 1 = A ou ~A
P(B): 1 = B ou ~B
P(C|A, B): 2^2 = 4 = AeC ou ~AeC e BeC ou ~BeC
P(D|C): 2^1 = 2 = CeD ou ~CeD
P(E|C): 2^1 = 2 = CeE ou ~CeE
Estados de redes Bayesianas = 10
"""

"""
Métodos Baseados em Classificadores
> Classificadores são tipos de agentes inteligentes especializados;
> Percebem o ambiente e extraem as características;
> Classificam e agrupam as características;
> Classificar é a tarefa mais importante no aprendizado de máquina;
> Classificadores são essenciais para o reconhecimento de padrões;
> Exemplos: filtros anti-SPAM e reconhecimento facial;

Reconhecimento de Padrões
> Naive Bayes: baseado no Teorema de Bayes, é assumido a independência entre as variáveis e montamos uma tabela com os
valores assumindo que não se influenciam;
> AODE: utiliza um grau de dependência para as variáveis, mais preciso que o Naive Bayses;
> KNN (Vizinho mais próximo): dado um ponto, o algoritmo classifica os elementos mais próximos a ele, classificando como
elementos da classe vizinha;

Avaliação de Progresso de Aprendizagem
> Classificadores: progresso da precisão da classificação;
> Regressores: com base no fator ed correlação, que é um fator que relaciona as distâncias entre o ponto de regressão e
todos os pontos da amostra;
"""