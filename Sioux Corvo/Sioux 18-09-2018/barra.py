import imagens
from objeto import Objeto

class Barra(Objeto):


	def __init__(self,ambiente,pos_x,pos_y):
		Objeto.__init__(self,ambiente,pos_x,pos_y,imagens.barra[0])
		self.energia = 0
		self.cont_img = 0
		self.cont_img2 = 0
	
	def aumentar_energia(self,valor):
		self.energia += valor

	def zerar_energia(self):
		self.energia = 0
		self.cont_img = 0
		self.image = self.ambiente.image.load(imagens.barra[self.cont_img])
		
	def animar(self):
		if self.cont_img <= (len(imagens.barra)-1):
			self.image = self.ambiente.image.load(imagens.barra[self.cont_img])
			self.cont_img += 1
		else:
			self.cont_img = 0
			




		