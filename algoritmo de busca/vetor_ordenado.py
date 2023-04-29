class Vertice:
    
    def __init__(self,rotulo, distancia_objetivo):
        self.rotulo = rotulo
        self.visitado = False
        self.distancia_objetivo = distancia_objetivo
        self.adjacentes = []

    def adiciona_adjacentes(self,adjacente):
        self.adjacentes.append(adjacente)

    def mostra_adjacente(self):
        for i in self.adjacentes:
            print(i.vertice_rotulo, i.custo)

class Adjacente:

    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo
        # A Estrela
        self.distancia_aestrela = vertice.distancia_objetivo + self.custo

class Grafo:
    Porto_Uniao = Vertice("Porto União", 203)
    Paulo_Frontin = Vertice("Paulo Frontin", 172)
    Canoinhas = Vertice("Canoinhas", 141)
    Tres_Barras = Vertice("Três Barras", 131)
    Sao_Matheus_Sul = Vertice("São Matheus do Sul", 123)
    Irati = Vertice("Irati", 139)
    Curitiba = Vertice("Curitiba", 0)
    Palmeira = Vertice("Palmeira", 59)
    Mafra = Vertice("Mafra", 94)
    Campo_Largo = Vertice("Campo Largo", 27)
    Balsa_Nova = Vertice("Balsa Nova", 41)
    Lapa = Vertice("Lapa", 74)
    Tijucas_Sul = Vertice("Tijucas do Sul", 56)
    Auracaria = Vertice("Auracária", 23)
    Sao_Jose_Pinhais = Vertice("São José dos Pinhais", 13)
    Contenda = Vertice("Contenda", 39)

    Porto_Uniao.adiciona_adjacentes(Adjacente(Paulo_Frontin, 46))
    Porto_Uniao.adiciona_adjacentes(Adjacente(Sao_Matheus_Sul, 87))
    Porto_Uniao.adiciona_adjacentes(Adjacente(Canoinhas, 78))

    Paulo_Frontin.adiciona_adjacentes(Adjacente(Irati, 75))
    Paulo_Frontin.adiciona_adjacentes(Adjacente(Porto_Uniao, 46))
    
    Canoinhas.adiciona_adjacentes(Adjacente(Porto_Uniao, 78))
    Canoinhas.adiciona_adjacentes(Adjacente(Tres_Barras, 12))
    Canoinhas.adiciona_adjacentes(Adjacente(Mafra, 66))

    Tres_Barras.adiciona_adjacentes(Adjacente(Sao_Matheus_Sul, 43))
    Tres_Barras.adiciona_adjacentes(Adjacente(Canoinhas, 12))

    Sao_Matheus_Sul.adiciona_adjacentes(Adjacente(Irati, 57))
    Sao_Matheus_Sul.adiciona_adjacentes(Adjacente(Palmeira, 77))
    Sao_Matheus_Sul.adiciona_adjacentes(Adjacente(Lapa, 60))
    Sao_Matheus_Sul.adiciona_adjacentes(Adjacente(Porto_Uniao, 87))
    Sao_Matheus_Sul.adiciona_adjacentes(Adjacente(Tres_Barras, 43))

    Irati.adiciona_adjacentes(Adjacente(Sao_Matheus_Sul, 57))
    Irati.adiciona_adjacentes(Adjacente(Palmeira, 75))
    Irati.adiciona_adjacentes(Adjacente(Paulo_Frontin, 75))

    Palmeira.adiciona_adjacentes(Adjacente(Sao_Matheus_Sul, 77))
    Palmeira.adiciona_adjacentes(Adjacente(Campo_Largo, 55))
    Palmeira.adiciona_adjacentes(Adjacente(Irati, 75))

    Mafra.adiciona_adjacentes(Adjacente(Lapa, 57))
    Mafra.adiciona_adjacentes(Adjacente(Tijucas_Sul, 99))
    Mafra.adiciona_adjacentes(Adjacente(Canoinhas, 66))

    Campo_Largo.adiciona_adjacentes(Adjacente(Balsa_Nova, 22))
    Campo_Largo.adiciona_adjacentes(Adjacente(Curitiba, 29))
    Campo_Largo.adiciona_adjacentes(Adjacente(Palmeira, 55))

    Balsa_Nova.adiciona_adjacentes(Adjacente(Contenda, 19))
    Balsa_Nova.adiciona_adjacentes(Adjacente(Campo_Largo, 22))
    Balsa_Nova.adiciona_adjacentes(Adjacente(Curitiba, 51))

    Lapa.adiciona_adjacentes(Adjacente(Mafra, 57))
    Lapa.adiciona_adjacentes(Adjacente(Contenda, 26))
    Lapa.adiciona_adjacentes(Adjacente(Sao_Matheus_Sul, 60))

    Tijucas_Sul.adiciona_adjacentes(Adjacente(Mafra, 99))
    Tijucas_Sul.adiciona_adjacentes(Adjacente(Sao_Jose_Pinhais, 49))

    Auracaria.adiciona_adjacentes(Adjacente(Curitiba, 37))
    Auracaria.adiciona_adjacentes(Adjacente(Contenda, 18))

    Sao_Jose_Pinhais.adiciona_adjacentes(Adjacente(Tijucas_Sul, 49))
    Sao_Jose_Pinhais.adiciona_adjacentes(Adjacente(Curitiba, 15))

    Contenda.adiciona_adjacentes(Adjacente(Balsa_Nova, 19))
    Contenda.adiciona_adjacentes(Adjacente(Auracaria, 18))
    Contenda.adiciona_adjacentes(Adjacente(Lapa, 26))

    Curitiba.adiciona_adjacentes(Adjacente(Campo_Largo, 29))
    Curitiba.adiciona_adjacentes(Adjacente(Balsa_Nova, 51))
    Curitiba.adiciona_adjacentes(Adjacente(Auracaria, 37))
    Curitiba.adiciona_adjacentes(Adjacente(Sao_Jose_Pinhais, 15))

grafo = Grafo()

import numpy as np
class VetorOrdenado:

    def __init__(self,capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        #Tipo de dado se torna um objeto e não mais inteiro
        self.valores = np.empty(self.capacidade, dtype=object)

    #Referência para o vértice e comparação com a distância para o objetivo
    def insere(self, adjacente):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i].distancia_aestrela > adjacente.distancia_aestrela:
                break
            if i == self.ultima_posicao:
                posicao= i + 1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x+1] = self.valores[x]
            x -= 1
        self.valores[posicao] = adjacente
        self.ultima_posicao += 1

    def imprime(self):
        if self.ultima_posicao == -1:
            print("O vetor está vazio.")
        else:
            for i in range(self.ultima_posicao + 1):
                print(i,' - ',self.valores[i].vertice.rotulo,' - ',
                      self.valores[i].custo,' - ',
                      self.valores[i].vertice.distancia_objetivo,' - ',
                      self.valores[i].distancia_aestrela)
                
class Aestrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False
    
    def buscar(self, atual):
        print('-'*10)
        print(f"Atual: {atual.rotulo}")
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if adjacente.vertice.visitado == False:
                    adjacente.vertice.visitado = True
                    vetor_ordenado.insere(adjacente)
            vetor_ordenado.imprime()

            if vetor_ordenado.valores[0] != None:
                self.buscar(vetor_ordenado.valores[0].vertice)

busca_aestrela = Aestrela(grafo.Curitiba)
busca_aestrela.buscar(grafo.Mafra)


