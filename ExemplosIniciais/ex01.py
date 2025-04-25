import random

#INFO: parametros iniciais do algoritmo
TAMANHO_POPULACAO = 50
TAMANHO_GENOMA = 100
GERACOES = 500
TAXA_MUTACAO = 0.05 #NOTE: utilize 0.1 para o torneio, 0.01 para a primeira roleta e 0.005 para a segunda roleta


#INFO: passo 1: Inicializacao da populacao
def inicializar_populacao():
    return [[random.randint(0,1) for _ in range(TAMANHO_GENOMA)] for _ in range(TAMANHO_POPULACAO)]

#INFO: passo 2: avaliar individuos
def avaliar_fitness(individuo):
    return sum(individuo)

#INFO: passo 3: selecionar pais 
def selecionar_pais(populacao, fitness):
    tamanho_torneio = 3
    pai1 = max(random.sample(list(zip(populacao, fitness)), tamanho_torneio),  key =lambda x: x[1])[0]
    pai2 = max(random.sample(list(zip(populacao, fitness)), tamanho_torneio),  key =lambda x: x[1])[0]
    
    return pai1, pai2

def selecionar_pais_roleta(populacao, fitness):
    total_fitness = sum(fitness)
    probabilidade = [f / total_fitness for f in fitness]

    pai1 = random.choices(populacao, weights=probabilidade, k=1)[0]
    pai2 = random.choices(populacao, weights=probabilidade, k=1)[0]

    return pai1, pai2


#INFO: passo 4: cruzamento (recombinacao)
def crossover(pai1, pai2):
    ponto_cruzamento = random.randint(1, TAMANHO_GENOMA - 1)
    filho1 = pai1[:ponto_cruzamento] + pai2[ponto_cruzamento:]
    filho2 = pai1[ponto_cruzamento:] + pai2[:ponto_cruzamento]
    return filho1, filho2

#INFO: passo 5: mutacao
def mutar(individuo):
    for i in range(TAMANHO_GENOMA):
        if (random.random() < TAXA_MUTACAO):
            individuo[i] = 1 - individuo[i]
        return individuo

#INFO: algoritmo genetico
def algoritmo_genetico():
    populacao = inicializar_populacao()
    
    for geracao in range(GERACOES):
        #AVALIAR a aptidao de cada individuo
        fitness = [avaliar_fitness(individuo) for individuo in populacao]
        
        #exibir o melhor individuo da geracao
        melhor_individuo = max(populacao, key=avaliar_fitness)
        print(f"geracao: {geracao} | melhor individuo: {melhor_individuo}, aptidao = {avaliar_fitness(melhor_individuo)}")
        
        nova_populacao = []

        #criar nova geracao com cruzamento e mutacao
        while len(nova_populacao) < TAMANHO_POPULACAO:
            #NOTE: existem duas funcoes para selecionar os pais
            # o metodo do torneio eh mais eficiente
            pai1,pai2 = selecionar_pais_roleta(populacao, fitness)
            filho1, filho2 = crossover(pai1, pai2)
            nova_populacao.append(mutar(filho1))
            nova_populacao.append(mutar(filho2))

        populacao = nova_populacao

    return max(populacao, key=avaliar_fitness)


#executar algoritmo genetico
melhor_solucao = algoritmo_genetico()
print(f"\nmelhor solucao encontrada: {melhor_solucao}")
