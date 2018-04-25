from dirFuncion import DirFuncion
from memoria import Memoria
from cuboSemantico import CuboSemantico

class Core():
	def __init__(self, funcionGlobal = "", funcionLocal = ""):
		self.funcionGlobal = funcionGlobal
		self.funcionLocal = funcionLocal
		self.dirFuncion = DirFuncion()
		self.cuboSemantico = CuboSemantico()
		self.memoria = Memoria()
		self.variablesTemp = []
		self.nombresParametros = []
		self.tiposParametros = []
		self.tiposArgumentos = []
		self.pilaOperandos = []
		self.pilaTipos = []
		self.pilaOperadores = []
		self.cuadruplos = []
		self.saltos = []
		self.regresa = []
		self.numCuadruplo = 1
		self.tieneReturn = False
		self.arreglos = {}
		self.stackArreglos = []		

	def printCuadruplos(self):
		for cuadruplo in self.cuadruplos:
			print(cuadruplo)
