# Redes Neurais Artificiais
"""
> Adquirir, Armazenar e Utilizar conhecimento;
> Reconhecimento de Padrões;

Características do Neurônio Biológico
Neurônio: são células especializadas que compões a porção ativa de nossos cérebros e de nossos sistemas nervosos;

Neurônio Booleano de McCulloch-Pitts
> Elemento computacional capaz de receber várias entradas booleanas, atribuir pesos, processá-las, compará-las com o
valor pré-estabelecido e gerar um valor booleano na saída.
> Comparação com o limiar:
    Valor = Sum(Entrada * Peso)
> Saída:
    Saída = f(Valor) = 0 ↔ Valor ≤ Limiar
    Saída = f(Valor) = 1 ↔ Valor > Limiar

Conceitos e Elementos das redes neurais
> Rede Neural Artificial: sistemas de computação inspirados pelas redes neurais biológicas que conseguem realizar
aprendizado de máquina; É formada por nós conectados em uma única direção, formando uma rede, na qual os sinais de
entrada são processados e propagados (ou não), gerando combinações de sinas de saída.
> Conexões de Saída/Entrada: Conexões entre nós de uma camada com os nós da camada subsequente.
> Pesos: Fatores de multiplicação para cada um dos sinais de entrada em um nó.
> Função de Processamento (ou ativação): processa o sinal gerado da combinação dos vários binômios [sinal de entrada,
peso], para gerar o sinal de saída do neurônio;
> Limiar: Valor arbitrário estabelecido para cada nó com o qual o resultado da função de processamento será comparado.

> Fase de Aprendizado: utiliza-se algum dos vários mecanismos de reconfiguração de pesos e limiares para reforçar os
estados que geram respostas corretas e inibir os estados que geram respostas erradas;
> Fase de Utilização: Resolve o problema a qual foi proposta, sendo que seus pesos e valores permanecem inalterados.
"""