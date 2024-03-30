# Buscas com Inteligência Artificial
"""
Mecanismos de Buscas
> Os agentes inteligentes guardam suas informações em estruturas, para acessá-las é necessária que este ato seja feito
de maneira eficiente;

            → F
        → E
    D
            → A
        → B
            → C

Busca em Extensão
> Começa explorando a raiz da árvore e visita cada nó do primeiro nível antes de prosseguir para o segundo nível e assim
por diante;
> D, B, E, A, C, F

Busca em Profundidade
> Explora a profundidade de um ramo de uma árvore o máximo o possível;
> Pré-Ordem:
    D, B, A, C, E, F
> Pós-Ordem:
    A, C, B, F, E, D
> Em-Ordem:
    A, B, C, D, E, F

Busca Heurística
> Baseada na análise dos nós e da disposição dos mesmo, sendo que à medida que cada visita ocorre, o mecanismo ajusta
uma estrutura interna que vai sendo criada para armazenar os resultados das visitas.
> Ocorre aprendizado de máquina
> Complexidade da busca heurística:
    - Complexidade da árvore ou grafo;
    - Regras que formam os nós das árvores;
    - Eficiência do algoritmo de busca;
"""