import pygame
from sprites import Sprites
from inputs import Inputs
import imagens
from colono_atirador import Colono_atirador
from colono_espada import Colono_espada
from indio import Indio
from lanca import Lanca
from barra import Barra
from corvo import Corvo

class Main:

	
	ambiente = pygame
	ambiente.init()
	sprites = Sprites(pygame)
	inputs = Inputs(ambiente)
	clock_soldados = ambiente.time.get_ticks()
	clock_corvo = ambiente.time.get_ticks()
	relogio = ambiente.time.Clock()
	

	def inicializar_jogo(self):

		self.width = 800
		self.height = 600
		self.device_screen = self.ambiente.display.Info()
		print(self.device_screen.current_w)	
		self.screen = self.ambiente.display.set_mode([self.width,self.height])
		self.background = self.ambiente.image.load('imagens/mapa.png')
	

		self.indio = Indio(self.ambiente,3,1000,0,486)

		self.barra = Barra(self.ambiente,10,560)
		self.lanca = Lanca(self.ambiente,1,0,0,20,486,0,90)
		self.barreira = Barreira(self.ambiente,
		self.sprites.indio.add(self.indio)
		self.sprites.todos_objetos.add(self.sprites.indio,self.barra)
	
	def atualizar_objetos(self):

		self.screen.blit(self.background,[0,0])	
		self.screen.blit(self.lanca.image,self.lanca.rect)
		self.screen.blit(self.indio.img_vida,[10,10])
		self.sprites.todos_objetos.draw(self.screen)
		self.ambiente.display.flip()

	def respawn_soldados(self,time):
		
		if self.clock_soldados + time < self.ambiente.time.get_ticks():
			colono_atirador = Colono_atirador(self.ambiente,1,-2,0,2500,self.width,504)
			colono_espada = Colono_espada(self.ambiente,1,1,-2,0,2500,self.width,120)
			self.sprites.colonos_atirador.add(colono_atirador)
			self.sprites.colonos_espada.add(colono_espada)
			self.sprites.eixo.add(colono_atirador,colono_espada)
			self.sprites.todos_objetos.add(self.sprites.colonos_atirador,self.sprites.colonos_espada,self.sprites.eixo)
			self.clock_soldados = self.ambiente.time.get_ticks()
	
	def respawn_corvo(self,time):

		if self.clock_corvo + time < self.ambiente.time.get_ticks():
			corvo = Corvo(self.ambiente,1,-3,0,600000,800,40)
			self.sprites.corvo.add(corvo)
			self.sprites.todos_objetos.add(self.sprites.corvo)
			self.clock_corvo = self.ambiente.time.get_ticks()
	
	def iniciar(self):

		self.inicializar_jogo()
		self.ambiente.key.set_repeat(5,10)
		#self.respawn(2000)
		while True:
			#print('clock_tick',self.relogio.tick())
			#print('clock_fps',self.relogio.get_fps())
			print('corvo',self.sprites.corvo)
			self.ambiente.event.get()
			self.respawn_soldados(6000)
			self.respawn_corvo(2000)
			self.atualizar_objetos()
			self.sprites.interacoes(self.ambiente)
			self.inputs.checar_entradas(self.barra,self.lanca,self.sprites.lancas,self.sprites.todos_objetos)
			#print(self.sprites.lancas)

			

main = Main()
main.iniciar()






	 

