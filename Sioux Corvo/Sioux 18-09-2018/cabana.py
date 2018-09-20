from objeto import Objeto

class Cabana(Objeto):


	def __init__(self,ambiente,vida,pos_x,pos_y,image):
		Objeto.__init__(self,ambiente,pos_x,pos_y,image)
		self.vida = vida
		
	def perder_vida(dano_sofrido):
		self.vida -= dano_sofrido
		


	def colidir(self,ambiente,objetos):
		colisoes = ambiente.sprite.spritecollide(self.eu,objetos,False,ambiente.sprite.collide_mask)
		if colisoes:
			for i in colisoes:
				self.perder_vida(dano_sofrido)

				
