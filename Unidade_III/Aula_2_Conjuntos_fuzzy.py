# Conjuntos Fuzzy
"""
Definição de Conjunto Fuzzy
> Objetos Matemáticos: elementos matemáticos que representam coleções, permitindo que relações sejam estabelecidas;
> Imprecisão: admite que uma proposição seja parcialmente verdadeira;
> Característica da linguagem natural: aptos a lidar com descrições em linguagem natural;

Definição de Funções de Pertinência
> Uma função de pertinência define em que grau o elemento pertence a um conjunto fuzzy;
> Um conjunto fuzzy pode ser definido como um par (U, m) onde:
    U: Conjunto Fuzzy
    m: Função de pertinência sobre U

Definição e Funções e Pertinência
> Função Triangular (trimf): função linear que define 3 pontos, produzindo um pico;
    trimf(x, a, b, c) = max(0, min((x-a)/(b-a), (c-x)/(c-b)))
> Função Trapezoide (trapmf): função linear que define 3 pontos, produzindo um patamar;
    trapmf(x, a, b, c, d) = max(0, min((x-a)/(b-a), (d-x)/(d-c)))
> Função Gaussiana (gaussmf): curva gaussiana, curva do sino, simétrica, define-se 2 pontos;
    gaussmf(x, mu, sigma) = 1/(sqrt(2*pi)*sigma)*exp(-(x-mu)^2/(2*sigma^2))
> Função Sigmoide (sigmf): define 2 pontos, formando uma curva em S;
    sigmf(x, a, b) = 1/(1+exp((x-a)/(b-a)))
"""