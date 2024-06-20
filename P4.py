import random

# Definir parâmetros do problema
capacidade_mochila = 10  # Capacidade máxima da mochila
num_itens = 4 # Número de itens disponíveis
pesos = [3, 5, 2, 4]  # Pesos dos itens
valores = [15, 20, 10, 25]  # Valores dos itens

# Parâmetros do algoritmo genético
tam_populacao = 50  # Tamanho da população
taxa_crossover = 0.8  # Taxa de crossover
taxa_mutacao = 0.2  # Taxa de mutação
num_geracoes = 100  # Número de gerações

# Função de avaliação (fitness)
def avaliar_individuo(individuo):
    peso_total = 0
    valor_total = 0
    for i in range(num_itens):
        if individuo[i] == 1:
            peso_total += pesos[i]
            valor_total += valores[i]
    if peso_total > capacidade_mochila:
        valor_total = 0  # Penaliza soluções inválidas (peso excedido)
    return valor_total

# Função de crossover (dois pontos)
def crossover(individuo1, individuo2):
    ponto1 = random.randint(0, num_itens - 1)
    ponto2 = random.randint(ponto1 + 1, num_itens)
    filho1 = individuo1[:ponto1] + individuo2[ponto1:ponto2] + individuo1[ponto2:]
    filho2 = individuo2[:ponto1] + individuo1[ponto1:ponto2] + individuo2[ponto2:]
    return filho1, filho2

# Função de mutação (bit flip)
def mutacao(individuo):
    for i in range(num_itens):
        if random.random() < taxa_mutacao:
            individuo[i] = 1 - individuo[i]  # Troca o bit
    return individuo

# Inicialização da população
populacao = []
for _ in range(tam_populacao):
    individuo = [random.randint(0, 1) for _ in range(num_itens)]
    populacao.append(individuo)

# Execução do algoritmo genético
for geracao in range(num_geracoes):
    # Avaliação da população
    aptidoes = [avaliar_individuo(individuo) for individuo in populacao]
    melhores = sorted(range(len(aptidoes)), key=lambda k: aptidoes[k], reverse=True)
    populacao = [populacao[i] for i in melhores[:tam_populacao]]
    
    # Seleção, crossover e mutação
    nova_populacao = []
    while len(nova_populacao) < tam_populacao:
        pai1, pai2 = random.choices(populacao, weights=aptidoes, k=2)
        if random.random() < taxa_crossover:
            filho1, filho2 = crossover(pai1, pai2)
        else:
            filho1, filho2 = pai1[:], pai2[:]
        filho1 = mutacao(filho1)
        filho2 = mutacao(filho2)
        nova_populacao.append(filho1)
        nova_populacao.append(filho2)
    
    # Atualização da população
    populacao = nova_populacao

# Encontrar o melhor indivíduo (solução)
melhor_individuo = max(populacao, key=avaliar_individuo)
melhor_valor = avaliar_individuo(melhor_individuo)

# Resultado
print("Melhor solução encontrada:")
print("Itens selecionados:", melhor_individuo)
print("Valor total:", melhor_valor)
