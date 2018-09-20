from boneco import Boneco
import imagens

class Indio(Boneco):

	def __init__(self,ambiente,vida,intervalo_ataque,pos_x,pos_y):
		Boneco.__init__(self,ambiente,vida,0,0, intervalo_ataque,pos_x,pos_y,imagens.indio)
		self.angulo_lanca = 0
		self.img_vida = self.ambiente.image.load(imagens.vida_3).convert_alpha()

	def atirar_lanca(self):
		pass

	def perder_vida(self,dano_sofrido):
		self.vida -= dano_sofrido

		if self.vida == 2:
			self.img_vida = self.ambiente.image.load(imagens.vida_2).convert_alpha()
		elif self.vida == 1:
			self.img_vida = self.ambiente.image.load(imagens.vida_1).convert_alpha()
		else:
			self.img_vida = self.ambiente.image.load('imagens/blanka.jpg').convert_alpha()