import imagens
from sprites import Sprites
from copy import copy
from lanca import Lanca
class Inputs:


	def __init__(self,ambiente):
		self.ambiente = ambiente

	def checar_entradas(self,barra,lanca,group_lancas,todos_objetos):
		
		key = self.ambiente.key.get_pressed()
		
		for event in self.ambiente.event.get():	
			
			if event.type == self.ambiente.KEYDOWN:
				if key[self.ambiente.K_SPACE]:
					self.espaco(barra)
				
				elif key[self.ambiente.K_UP]:
					self.key_up(lanca)

				elif key[self.ambiente.K_DOWN]:
					self.key_down(lanca)
			
				elif key[self.ambiente.K_z]:
					exit()

			elif event.type == self.ambiente.KEYUP:
				if event.key == self.ambiente.K_SPACE:
					lanca_nova = Lanca(self.ambiente,lanca.dano,barra.energia,0,lanca.rect.x,lanca.rect.y,barra.energia,lanca.angulo)
					lanca_nova.angulo = lanca.angulo
					group_lancas.add(lanca_nova)
					todos_objetos.add(group_lancas)
					barra.zerar_energia()

	
	def espaco(self,barra):

		if barra.energia < 15:

			barra.aumentar_energia(0.5)
		
		else:
			barra.zerar_energia()

		barra.animar()
	
	def key_up(self,lanca):

		if lanca.angulo <= 87:
			lanca.angulo += 3 % 360
			lanca.animar(lanca.angulo+270)
			#print(lanca.angulo)

	def key_down(self,lanca):
		
		if lanca.angulo > 0: 
			lanca.angulo -= 3 % 360
			lanca.animar(lanca.angulo+270)
			#print(lanca.angulo)





