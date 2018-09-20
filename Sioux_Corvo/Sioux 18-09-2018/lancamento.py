import math

class Lancamento():

	def __init__(self, angulo, vel_0):
		self.an = angulo
		self.vel_0 = vel_0
		self.grav = -0.4
		self.tx = 0
		self.ty = 0
		self.t = 3
		self.vox = self.vel_0*math.cos(self.an*math.pi/180)
		self.voy = self.vel_0*math.sin(self.an*math.pi/180)
		print('vel_y',self.voy)
		print('vel_x',self.vox)
		self.yo = 486
		self.xo = 0
		#self.alcance = ((self.grav*-1)/2)*(self.t_subida**2)
		#self.t_descida = math.sqrt(self.alcance/(self.grav/2))
		#self.t = self.t_subida + self.t_descida
		#print('alcance', self.alcance)
		#print('tempo', self.t)
		#print('t_descida',self.t_descida)
	def calcular(self):
		#self.y = self.yo+self.voy*self.ty+self.grav/2*self.ty**2
		#self.x = self.xo+self.vox*self.tx
		
		#self.x = self.xo+self.vox*self.t	
		#self.y = self.yo+self.voy*self.t-(1/2)*self.grav*(self.t**2)
		self.xo += self.vox
		self.yo -= self.voy
		self.voy += self.grav
		print(self.voy)
			#print('x = '+str(self.x))
			#print('y = '+str(self.y))
			
			#if self.alcance-self.yo < 0 :
			#	self.subindo = False
			#	self.voy = 0
			
		#else:
		#	self.voy -= self.grav
			#print('x = '+str(self.x))
			#print('y = '+str(self.y))

	def calcular_tempo(self,vel,grav):
		
		tempo = vel/grav
		return tempo
		
	def somar(self):
		pass
		#self.tx = self.tx+1
		#self.ty = self.ty+1
		#print(self.ty)
		
	def lancar(self):
		while self.ty < 50:
			self.calcular()
			self.somar()

if __name__ == "__main__":
	lancamento = Lancamento(30,50)
	lancamento.lancar()



