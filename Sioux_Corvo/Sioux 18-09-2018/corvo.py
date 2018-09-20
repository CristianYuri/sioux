import imagens
from boneco import Boneco



class Corvo(Boneco):

	def __init__(self,ambiente,vida,vel_x,vel_y,intervalo_ataque,\
		pos_x,pos_y):
		self.cont_voar = 0
		Boneco.__init__(self,ambiente,vida,vel_x,vel_y,intervalo_ataque,\
		pos_x,pos_y,imagens.corvo[0])


	def animar(self):

		if self.cont_voar <= (len(imagens.corvo) -1):
			self.image = self.ambiente.image.load(imagens.corvo[self.cont_voar])
			self.cont_voar += 1
		else:
			self.image = self.ambiente.image.load(imagens.corvo[0])
			self.cont_voar = 0

