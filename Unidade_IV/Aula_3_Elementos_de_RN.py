# Elementos de Redes Neurais
"""
ADALINE
> Neurônio artificial;
> Desenvolvido em 1960 com o objetivo de chaveamento de circuitos telefônicos
> Foi a primeira RNA aplicada na indústria;
> Desenvolvimento da Regra Delta;

ADALINE x Neurônio padrão de McCulloch-Pitts
> Na fase de aprendizado do ADALINE os pesos são ajustados de acordo com uma combinação linear das entradas ponderadas,
já no neurônio de McCulloch-Pitts as entradas ponderadas passam pela função de ativação não linear, e a saída dessa
função é usada para ajustar os pesos.

Regra Delta
> Algoritmo de Aprendizado;
> Busca calcular o quadrado da taxa de erro (e^2), pois assim trata de erros positivos e negativos;
> O objetivo é trazer o erro mais próximo de zero;
"""


from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np


class Adaline:
    def __init__(self, taxa_aprendizado=0.01, epocas=50):
        self.taxa_aprendizado = taxa_aprendizado
        self.epocas = epocas

    def treinar(self, X, y):
        self.w_ = np.zeros(X.shape[1])
        self.b_ = 0

        for _ in range(self.epocas):
            for xi, alvo in zip(X, y):
                # passagem direta
                modelo_linear = np.dot(xi, self.w_) + self.b_
                y_pred = self.funcao_ativacao(modelo_linear)

                # passagem de volta
                erro = y_pred - alvo
                self.w_ -= self.taxa_aprendizado * erro * xi
                self.b_ -= self.taxa_aprendizado * erro

    def prever(self, X):
        modelo_linear = np.dot(X, self.w_) + self.b_
        y_pred = self.funcao_ativacao(modelo_linear)
        return y_pred

    def funcao_ativacao(self, t):
        return np.where(t >= 0, 1, 0)


# gerar dados sintéticos
X, y = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, random_state=42)

# dividir os dados em conjuntos de treinamento e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

# instanciar o modelo ADALINE e treiná-lo
modelo = Adaline()
modelo.treinar(X_treino, y_treino)

# fazer previsões no conjunto de testes
y_predito = modelo.prever(X_teste)

# avaliar a acurácia do modelo
acuracia = accuracy_score(y_teste, y_predito)
print("Acurácia:", acuracia)

#%%
# Regra Delta Generalizada
"""
Retropropagação de Erro
> Algoritmo utilizado para o treinamento de redes neurais multicamadas e possui dois passos:
    1. Processamento direto;
    2. Processamento reverso;
    
> Feedforward (alimentação por avanço)
    Camada de Entrada -> Camada Oculta -> Camada de Saida
    
> Backpropagation (alimentação por regressão)
    Erro da Camada de Saida -> Erro da Camada Oculta -> Camada de Entrada
"""


class RegraDelta:
    def __init__(self, taxa_aprendizado=0.01, epocas=50):
        self.taxa_aprendizado = taxa_aprendizado
        self.epocas = epocas

    def treinar(self, X, y):
        self.w_ = np.zeros(X.shape[1])
        self.b_ = 0

        for _ in range(self.epocas):
            for xi, alvo in zip(X, y):
                y_pred = self.predizer(xi)
                erro = alvo - y_pred
                self.w_ += self.taxa_aprendizado * erro * xi
                self.b_ += self.taxa_aprendizado * erro

    def predizer(self, X):
        return np.dot(X, self.w_) + self.b_

# exemplo de uso
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 1])

modelo = RegraDelta()
modelo.treinar(X, y)

# fazer previsões
for xi in X:
    predicao = modelo.predizer(xi)
    print(f"Para entrada {xi}, a previsão é {predicao}")