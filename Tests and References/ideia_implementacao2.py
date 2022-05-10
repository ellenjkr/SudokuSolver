import pandas as pd
from math import sqrt


class Vertice():
	def __init__(self, vertice_id, conexoes):
		super(Vertice, self).__init__()
		self.id = vertice_id
		self.conexoes = conexoes
		self.grau = 0
		self.grau_saturacao = 0
		self.colorido = False
		self.label = 0
		self.cor =  0 # A cor seria o mesmo valor que o número


def monta_tabuleiro(tamanho):
	tabuleiro = []
	cont = 1
	for i in range(tamanho):
		linha_tabuleiro = []
		for j in range(tamanho):
			nome_casa = cont
			cont += 1

			linha_tabuleiro.append(nome_casa)

		tabuleiro.append(linha_tabuleiro)

	return tabuleiro


def cria_vertices(tabuleiro, tamanho):
	tam_quadrante = int(sqrt(tamanho))
	vertices = []

	for i in range(tamanho): #percorre linha
		for j in range(tamanho): #percorre coluna
			valor_casa = tabuleiro[i][j]

			vertices_linha = tabuleiro[i].copy()
			vertices_linha.remove(valor_casa)

			vertices_coluna = [tabuleiro[x][j] for x in range(tamanho)]
			vertices_coluna.remove(valor_casa)

			vertices_quadrante = []
			quadrante_coluna = j//tam_quadrante
			quadrante_linha = i//tam_quadrante
			for m in range(quadrante_linha * tam_quadrante, tam_quadrante*quadrante_linha+tam_quadrante):
				for n in range(tam_quadrante*quadrante_coluna,tam_quadrante*quadrante_coluna+tam_quadrante):
					if m != i and n != j:
						vertices_quadrante.append(tabuleiro[m][n])				

			conexoes = vertices_linha + vertices_coluna + vertices_quadrante

			novo_vertice = Vertice(
				valor_casa,
				conexoes
			)

			vertices.append(novo_vertice)

	return vertices




def gera_matriz(vertices, tamanho):
	matriz = []

	# Percorre os vértices
	for vertice in vertices:
		linha_matriz = []
		# Verifica as conexões do vértice atual com os demais
		for aux_vertice in vertices:
			""" Adiciona 1 à linha se o vértice estiver nas conexões do
				vértice atual e 0 se não estiver """
			linha_matriz.append(1) if aux_vertice.id in vertice.conexoes else linha_matriz.append(0)
		matriz.append(linha_matriz)

	header = [vertice + 1 for vertice in range(tamanho * tamanho)]
	
	#for i in matriz:
		#print(i)
	return matriz

def todos_pintados(vertices):
	for vertice in vertices:
		if vertice.colorido == False:
			return False
	return True

def cor_nova(vertices, atual, coloridos):
	cor = None
	cores_adj = [vertices[adj - 1].cor for adj in atual.conexoes if vertices[adj - 1].colorido is True]

	cores_disponiveis = []
	for vertice in coloridos:
		if vertice.id not in atual.conexoes and vertice.cor not in cores_adj:
			cores_disponiveis.append(vertice)

	if cores_disponiveis != []:
		cor = cores_disponiveis[0]
		for iter_cor in cores_disponiveis:
			if iter_cor.grau_saturacao > cor.grau_saturacao:
				cor = iter_cor
		#cor = next((vertice.cor for vertice in coloridos if vertice.id not in atual.conexoes and vertice.cor not in cores_adj), None)
		cor = cor.cor
	else:
		maior_cor = coloridos[0].cor
		for colorido in coloridos:
			if colorido.cor > maior_cor:
				maior_cor = colorido.cor
		cor = maior_cor + 1

	return cor

def resolve_sudoku(matriz, vertices, inicio = 1):
	vertices[inicio - 1].colorido = True
	vertices[inicio - 1].label = 1
	vertices[inicio - 1].cor = 1

	coloridos = []
	coloridos.append(vertices[inicio - 1])
	for i in range(len(matriz)):
		if matriz[inicio - 1][i] == 1:
			if i != inicio - 1:
				vertices[i].grau_saturacao += 1

	while todos_pintados(vertices) is False:

		atual = next((vertice for vertice in vertices if vertice.colorido is False))
		
		for vertice in vertices:
			if vertice.grau_saturacao > atual.grau_saturacao and vertice.colorido is False:
				atual = vertice

		atual.colorido = True

		cor = cor_nova(vertices, atual, coloridos)

		atual.cor = cor
		atual.label = cor

		coloridos.append(atual)
		for i in range(len(matriz)):
			if matriz[atual.id - 1][i] == 1:
				# print(i)
				if i != (atual.id - 1) and vertices[i].colorido is False:
					vertices[i].grau_saturacao += 1

	return vertices

# T = 9
# tabuleiro = monta_tabuleiro(T)
# vertices = cria_vertices(tabuleiro, T)
# matriz = gera_matriz(vertices, T)
# vertices = resolve_sudoku(matriz, vertices)


