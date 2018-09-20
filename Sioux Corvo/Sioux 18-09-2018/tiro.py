from objeto import Objeto
import imagens

class Tiro(Objeto):


	def __init__(self,ambiente,dano,vel_x,pos_x,pos_y):
		Objeto.__init__(self,ambiente,pos_x,pos_y,imagens.tiro)
		self.dano = dano
		self.vel_x = vel_x
	
	def movimentar(self):
		self.rect.x += self.vel_x

