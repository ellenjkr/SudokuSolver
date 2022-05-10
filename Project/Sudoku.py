from Vertice import Vertice
from copy import deepcopy
from math import sqrt
import random


class Sudoku():
	def __init__(self):
		super(Sudoku, self).__init__()

	def reseta_vertice(self, vertice):
		vertice.colorido = False
		vertice.label = 0
		vertice.cor = 0
		vertice.grau_saturacao = 0
		return vertice

	def gera_sudoku(self, tamanho, inicial):
		self.tamanho = tamanho
		self.inicial = inicial

		tabuleiro = self.monta_tabuleiro()
		vertices = self.cria_vertices(tabuleiro)
		matriz = self.gera_matriz(vertices)
		matriz_copia = deepcopy(matriz)
		vertices_copia = deepcopy(vertices)
		vertices, finalizado = self.resolve_sudoku(matriz, vertices_copia)
		# Enquanto a tentativa de resolução falhar, tenta de novo
		while finalizado is False:
			for vertice in vertices_copia:
				vertice = self.reseta_vertice(vertice)
			vertices, finalizado = self.resolve_sudoku(matriz_copia, vertices_copia)
		
		for j in range(self.tamanho):
			vertices_coluna = [tabuleiro[x][j] for x in range(self.tamanho)]
			cores_coluna = []
			for v in vertices_coluna:
				cores_coluna.append(vertices[v - 1].cor)
			ja_estava = list(dict.fromkeys(cores_coluna))
			if len(ja_estava) != len(cores_coluna):
				print(f"coluna {j + 1} com valores repetidos")
		return vertices

	def monta_tabuleiro(self):
		tabuleiro = []
		cont = 1
		for i in range(self.tamanho):
			linha_tabuleiro = []  # Cria linha do tabuleiro
			for j in range(self.tamanho):  # Cada coluna da linha
				nome_casa = cont  # Nome da casa varia de 1-N*N
				cont += 1

				linha_tabuleiro.append(nome_casa)  # Adiciona casa na linha

			tabuleiro.append(linha_tabuleiro)  # Adiciona linha no tabuleiro

		return tabuleiro

	def cria_vertices(self, tabuleiro):
		tam_quadrante = int(sqrt(self.tamanho))
		vertices = []

		for i in range(self.tamanho):  # Percorre linha
			for j in range(self.tamanho):  # Percorre coluna
				valor_casa = tabuleiro[i][j]

				# ======================================
				# VÉRTICES ADJACENTES DA CASA

				# Vértices adjacentes por linha
				vertices_linha = tabuleiro[i].copy()
				vertices_linha.remove(valor_casa)

				# Vértices adjacentes por coluna
				vertices_coluna = [tabuleiro[x][j] for x in range(self.tamanho)]
				vertices_coluna.remove(valor_casa)

				# Vértices adjacentes por quadrante
				vertices_quadrante = []
				quadrante_coluna = j // tam_quadrante
				quadrante_linha = i // tam_quadrante

				# Percorre vértices do quadrante
				for m in range(quadrante_linha * tam_quadrante, tam_quadrante * quadrante_linha + tam_quadrante):
					for n in range(tam_quadrante * quadrante_coluna, tam_quadrante * quadrante_coluna + tam_quadrante):
						if m != i and n != j:
							vertices_quadrante.append(tabuleiro[m][n])

				# Junta todos os vértices adjacentes
				conexoes = vertices_linha + vertices_coluna + vertices_quadrante

				# ======================================
				novo_vertice = Vertice(
					valor_casa,
					conexoes
				)

				vertices.append(novo_vertice)

		return vertices

	def gera_matriz(self, vertices):
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

		return matriz

	def todos_pintados(self, vertices):
		for vertice in vertices:
			if vertice.colorido is False:
				return False
		return True

	def define_cor(self, vertices, atual, coloridos):
		# Obtém as cores utilizadas pelos adjacentes do vértice atual
		cores_adj = [vertices[adj - 1].cor for adj in atual.conexoes if vertices[adj - 1].colorido is True]

		# Identifica quais cores já utilizadas estão disponíveis para reutilização
		cores_disponiveis = []
		for vertice in coloridos:
			if vertice.id not in atual.conexoes and vertice.cor not in cores_adj:
				cores_disponiveis.append(vertice)
		

		if cores_disponiveis != []:  # Se tiver cores disponíveis
			cor = cores_disponiveis[0]
			for iter_cor in cores_disponiveis:
				if iter_cor.grau_saturacao < cor.grau_saturacao:
					cor = iter_cor
			cor = cor.cor
		else:  # Se não tiver nenhuma cor disponível é criada uma cor nova
			maior_cor = coloridos[0].cor
			for colorido in coloridos:
				if colorido.cor > maior_cor:
					maior_cor = colorido.cor
			cor = maior_cor + 1

		return cor

	def troca_cor(self, vertices, atual, coloridos, trocar, vertice_trocado=None):
		# Obtém as cores utilizadas pelos adjacentes do vértice atual
		conexoes = deepcopy(atual.conexoes)
		if vertice_trocado is not None:
			conexoes.remove(vertice_trocado.id)
		cores_adj = [vertices[adj - 1].cor for adj in conexoes if vertices[adj - 1].colorido is True]

		# Identifica quais cores já utilizadas estão disponíveis para reutilização
		cores_disponiveis = []
		for vertice in coloridos:
			if vertice.id not in conexoes and vertice.cor not in cores_adj:
				if vertice.cor not in cores_disponiveis:
					cores_disponiveis.append(vertice)
		
		cor = None
		if cores_disponiveis != []:  # Se tiver cores disponíveis
			for iter_cor in cores_disponiveis:
				if iter_cor.cor in trocar:
					cor = iter_cor
			if cor is not None:
				for iter_cor in cores_disponiveis:
					if iter_cor.grau_saturacao < cor.grau_saturacao and iter_cor.cor in trocar:
						cor = iter_cor
				cor = cor.cor
		else:  # Se não tiver nenhuma cor disponível é criada uma cor nova
			cor = None

		return cor

	def corrige_cor(self, atual, vertices, coloridos, direcao):
		cores = list(range(1, self.tamanho + 1))
		if direcao == "linha":
			linha_atual = atual.id // self.tamanho if atual.id % self.tamanho != 0 else (atual.id - 1) // self.tamanho
			mesma_direcao = [vertice for vertice in vertices[linha_atual * self.tamanho:linha_atual * self.tamanho + self.tamanho] if vertice.cor != 0]
		elif direcao == "coluna":
			coluna_atual = atual.id % self.tamanho
			mesma_direcao = [vertice for vertice in vertices if vertice.id % self.tamanho == coluna_atual and vertice.cor != 0]
		elif direcao == "quadrante":
			tam_quadrante = int(sqrt(self.tamanho))
			mesma_direcao = []
			linha_atual = atual.id // self.tamanho if atual.id % self.tamanho != 0 else (atual.id - 1) // self.tamanho
			coluna_atual = atual.id % self.tamanho - 1 if atual.id % self.tamanho != 0 else self.tamanho - 1
			quadrante_coluna = coluna_atual // tam_quadrante
			quadrante_linha = linha_atual // tam_quadrante
			# Percorre vértices do quadrante
			for m in range(quadrante_linha * tam_quadrante, tam_quadrante * quadrante_linha + tam_quadrante):
				for n in range(tam_quadrante * quadrante_coluna, tam_quadrante * quadrante_coluna + tam_quadrante):
					if m != linha_atual and n != coluna_atual:
						id_vertice = m * self.tamanho + n + 1
						vertice = vertices[id_vertice - 1]
						if vertice.cor != 0:
							mesma_direcao.append(vertice)

		utilizadas_na_direcao = [item.cor for item in mesma_direcao]

		faltam = [cor for cor in cores if cor not in utilizadas_na_direcao]

		substituta = None
		cor_atual = None
		pos_vertice = 0

		# print(f"Atual: {atual.id}")
		while substituta is None or cor_atual is None:
			if pos_vertice == len(mesma_direcao) or len(mesma_direcao) == 0:
				return vertices, False
			vertice = vertices[mesma_direcao[pos_vertice].id - 1]
			# print(f"Vertice: {vertice.id}, cor: {vertice.cor}")
			substituta = self.troca_cor(vertices, vertice, coloridos, faltam)
			# print(f"Substituta: {substituta}")
			cor_atual = self.troca_cor(vertices, atual, coloridos, [vertice.cor], vertice_trocado=vertice)

			pos_vertice += 1

		vertices[atual.id - 1].cor = vertices[mesma_direcao[pos_vertice - 1].id - 1].cor
		vertices[atual.id - 1].label = vertices[atual.id - 1].cor
		vertices[atual.id - 1].colorido = True
		vertices[mesma_direcao[pos_vertice - 1].id - 1].cor = substituta

		return vertices, True

	def resolve_sudoku(self, matriz, vertices):
		atual = vertices[self.inicial - 1]  # Pega o vertice inicial definido pelo usuário
		atual.colorido = True
		atual.label = 1
		atual.cor = 1


		coloridos = []  # Lista para adicionar os vértices já coloridos
		coloridos.append(atual)  # Adiciona o primeiro vértice colorido
		for i in range(len(matriz)):  # Percorre a matriz de adjacência
			# Aumenta o grau de saturação nos vértices adjacentes
			if matriz[self.inicial - 1][i] == 1:
				if i != self.inicial - 1:
					vertices[i].grau_saturacao += 1

		continua = True
		while self.todos_pintados(vertices) is False:  # Enquanto todos não estiverem pintados
			# Obtém o vértice atual a partir do anterior, verificando se já está colorido e se é o maior grau de saturação
			# atual = next((vertice for vertice in vertices[atual.id - 1:] if vertice.colorido is False), None)
			# if atual is None:
			# 	atual = next((vertice for vertice in vertices if vertice.colorido is False))
			# for vertice in vertices:
			# 	if vertice.grau_saturacao > atual.grau_saturacao and vertice.colorido is False:
			# 		atual = vertice

			for vertice in vertices:
				if vertice.colorido is False:
					maior_grau_saturacao = vertice.grau_saturacao
			for vertice in vertices:
				if vertice.grau_saturacao > maior_grau_saturacao and vertice.colorido is False:
					maior_grau_saturacao = vertice.grau_saturacao

			lista_maiores_graus = [vertice for vertice in vertices if vertice.grau_saturacao == maior_grau_saturacao and vertice.colorido is False]
			if len(lista_maiores_graus) > 1:
				atual_pos = random.randint(0, len(lista_maiores_graus) - 1)
				atual = vertices[lista_maiores_graus[atual_pos].id - 1]
			else:
				atual = vertices[lista_maiores_graus[0].id - 1]

			atual.colorido = True
			# Obtém cor para o vértice atual
			cor = self.define_cor(vertices, atual, coloridos)
			
			if cor > self.tamanho:
				vertices, continua = self.corrige_cor(atual, vertices, coloridos, "linha")
				if continua is False:
					vertices, continua = self.corrige_cor(atual, vertices, coloridos, "coluna")
					if continua is False:
						vertices, continua = self.corrige_cor(atual, vertices, coloridos, "quadrante")
						if continua is False:
							return vertices, False
				atual = vertices[atual.id - 1]
			else:
				atual.cor = cor
				atual.label = cor

			# Adiciona o vertice atual a lista de coloridos
			coloridos.append(atual)

			# Aumenta o grau de saturação de seus adjacentes
			for i in range(len(matriz)):
				if matriz[atual.id - 1][i] == 1:
					if i != (atual.id - 1):
						vertices[i].grau_saturacao += 1
		return vertices, True
