from objeto import Objeto
import imagens
class Boneco(Objeto):


	def __init__(self,ambiente,vida,vel_x,vel_y,intervalo_ataque,\
		pos_x,pos_y,image):
		
		Objeto.__init__(self,ambiente,pos_x,pos_y,image)
		self.vida = vida
		self.vel_x = vel_x
		self.vel_y = vel_y
		self.intervalo_ataque = intervalo_ataque

	def perder_vida(self,dano_sofrido):
		self.vida -= dano_sofrido

	def movimentar(self):
		self.rect.x += self.vel_x
		self.rect.y += self.vel_y
		#if self.cont <= (len(imagens.colono_atirador_caminhando)-1):
		#	self.definir_imagem(imagens.colono_atirador_caminhando[self.cont],self.rect.x,self.rect.y)
		#	self.cont += 1
		#else:
		#	self.cont = 0
		#	self.definir_imagem(imagens.colono_atirador_caminhando[self.cont],self.rect.x,self.rect.y)





	

