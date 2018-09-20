import imagens
from boneco import Boneco

class Colono_espada(Boneco):


	def __init__(self,ambiente,vida,dano,vel_x,vel_y,intervalo_ataque,\
		pos_x,pos_y):
		Boneco.__init__(self,ambiente,vida,vel_x,vel_y,intervalo_ataque,\
			pos_x,pos_y,imagens.colono_espada)
		self.dano = dano
		self.cont_caminhar = 0
		self.cont_golpear = 0

	def atacar(alvo):
		alvo.perder_vida(self.dano)


	def animar(self):
		self.animacao_caminhando()

	def animacao_caminhando(self):

		if self.cont_caminhar <= (len(imagens.colono_espada_caminhando)-1):
			self.image = self.ambiente.image.load(imagens.colono_espada_caminhando[self.cont_caminhar])
			self.cont_caminhar += 1

		else:
			self.image = self.ambiente.image.load(imagens.colono_espada)
			self.cont_caminhar = 0

	def animacao_golpeando(self):

		if self.cont_golpear <= (len(imagens.colono_golpeando)-1):
			self.image = self.ambiente.image.load(imagens.colono_golpeando[self.cont_golpear])
			self.cont_golpear += 1
		else:
			self.image = self.ambiente.image.load(imagens.colono_golpeando[0])
			self.cont_golpear = 0		

	def animacao_parado(self):
		self.image = imagens.colono_espada


