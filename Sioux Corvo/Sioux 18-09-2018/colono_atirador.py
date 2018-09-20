import imagens
from boneco import Boneco

class Colono_atirador(Boneco):


	def __init__(self,ambiente,vida,vel_x,vel_y,intervalo_ataque,\
		pos_x,pos_y):
		Boneco.__init__(self,ambiente,vida,vel_x,vel_y,intervalo_ataque,\
			pos_x,pos_y,imagens.colono_atirador)
		self.cont_caminhar = 0
		self.cont_atirar = 0
		self.clock_atirar = self.ambiente.time.get_ticks()
		print(self.image.get_width())
		
	def atirar():
		pass

	def animar(self):
		self.animacao_caminhando()

	def animar_morte(self):
		self.image = self.ambiente.image.load(imagens.colono_atirador_morto)
		
	def animacao_caminhando(self):

		if self.cont_caminhar <= (len(imagens.colono_atirador_caminhando) -1):
			self.image = self.ambiente.image.load(imagens.colono_atirador_caminhando[self.cont_caminhar])
			self.cont_caminhar += 1
		else:
			self.image = self.ambiente.image.load(imagens.colono_atirador_caminhando[0])
			self.cont_caminhar = 0

	def animacao_atirando(self):

		if self.cont_atirar <= (len(imagens.colono_atirando)-1):
			self.image = self.ambiente.image.load(imagens.colono_atirando[self.cont_atirar])
			self.cont_atirar += 1
		else:
			self.image = self.ambiente.image.load(imagens.colono_atirando[0])
			self.cont_atirar = 0		

	def animacao_parado(self):
		self.image = self.ambiente.image.load(imagens.colono_atirador)
