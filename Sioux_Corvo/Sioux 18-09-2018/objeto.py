import pygame

class Objeto(pygame.sprite.Sprite):


	def __init__(self,ambiente,pos_x,pos_y,image):
		
		pygame.sprite.Sprite.__init__(self)
		self.ambiente = ambiente
		self.definir_imagem(image,pos_x,pos_y)
		self.cont = 0
		

	def definir_imagem(self,image,pos_x,pos_y):

		self.image = self.ambiente.image.load(image).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = pos_x
		self.rect.y = pos_y
		self.mask = self.ambiente.mask.from_surface(self.image)




