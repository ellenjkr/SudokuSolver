import pandas as pd


class Vertice():
	def __init__(self, nome, conexoes):
		super(Vertice, self).__init__()
		self.nome = nome
		self.conexoes = conexoes
		self.grau = 0
		self.grau_saturacao = 0
		self.colorido = False
		self.cor = 0  # A cor seria o mesmo valor que o número


def monta_tabuleiro(tamanho):
	tabuleiro = []
	cont = 0
	for i in range(tamanho):
		linha_tabuleiro = []
		for j in range(tamanho):
			nome_casa = cont
			cont += 1

			linha_tabuleiro.append(nome_casa)

		tabuleiro.append(linha_tabuleiro)

	return tabuleiro


def cria_vertices(tabuleiro, tamanho):
	vertices = {}
	cont = 0

	for pos_linha, linha in enumerate(tabuleiro):
		for pos_coluna, casa in enumerate(linha):
			nome_vertice = cont
			cont += 1
			conexoes_vertice = []

			if pos_linha == 0:
				conexoes_vertice.append(tabuleiro[tamanho - 1][pos_coluna])  # Cima (conecta com o último de baixo)
			else:
				conexoes_vertice.append(tabuleiro[pos_linha - 1][pos_coluna])  # Cima

			if pos_linha == (tamanho - 1):  # Última linha
				conexoes_vertice.append(tabuleiro[0][pos_coluna])  # Baixo (conecta com o primeiro de cima)
			else:
				conexoes_vertice.append(tabuleiro[pos_linha + 1][pos_coluna])  # Baixo

			if pos_coluna == 0:  # Primeira coluna
				conexoes_vertice.append(tabuleiro[pos_linha][tamanho - 1])  # Esquerda (conecta com o último da direita)
			else:
				conexoes_vertice.append(tabuleiro[pos_linha][pos_coluna - 1])  # Esquerda

			if pos_coluna == (tamanho - 1):  # Última coluna
				conexoes_vertice.append(tabuleiro[pos_linha][0])  # Direita (conecta com o primeiro da esquerda)
			else:
				conexoes_vertice.append(tabuleiro[pos_linha][pos_coluna + 1])  # Direita

			novo_vertice = Vertice(
				nome_vertice,
				conexoes_vertice
			)

			vertices[nome_vertice] = novo_vertice

	return vertices


def gera_matriz(vertices, tamanho):
	matriz = []

	# Percorre os vértices
	for vertice in vertices.values():
		linha_matriz = []
		# Verifica as conexões do vértice atual com os demais
		for aux_vertice in vertices.values():
			""" Adiciona 1 à linha se o vértice estiver nas conexões do
				vértice atual e 0 se não estiver """
			linha_matriz.append(1) if aux_vertice.nome in vertice.conexoes else linha_matriz.append(0)
		matriz.append(linha_matriz)

	header = [vertice for vertice in range(tamanho * tamanho)]
	matriz_df = pd.DataFrame(matriz, columns=header)

	for vertice in vertices.values():
		grau = int(matriz_df[vertice.nome].value_counts()[1])
		vertice.grau = grau

	conexoes = matriz_df.loc[matriz_df[5] == 1]  # Utilizando o vértice 5 como exemplo
	conexoes = list(conexoes.index)
	for conexao in conexoes:
		vertices[conexao].grau_saturacao += 1

	# a partir daqui da pra aumentar o grau de saturação de cada uma


T = 4
tabuleiro = monta_tabuleiro(T)
vertices = cria_vertices(tabuleiro, T)
gera_matriz(vertices, T)

# 00 01 02 03
# 10 11 12 13
# 20 21 22 23
# 30 31 32 33


# ver que na vdd nao tenho que validar so o ultimo com o primeiro, os do meio tambem tem que se validar