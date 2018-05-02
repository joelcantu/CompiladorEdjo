from dirFuncion import DirFuncion
from memoria import Memoria
from cuboSemantico import CuboSemantico

class Core():
	def __init__(self, funcionGlobal = "", funcionLocal = ""):
		self.funcionGlobal = funcionGlobal
		self.funcionLocal = funcionLocal
		#Inicializa dir funcion
		self.dirFuncion = DirFuncion()
		#Inicializa cubo semantico
		self.cuboSemantico = CuboSemantico()
		#Inicializa memoria
		self.memoria = Memoria()
		#Variables temporales
		self.variablesTemp = []
		self.nombresParametros = []
		self.tiposParametros = []
		self.tiposArgumentos = []
		self.pilaOperandos = []
		self.pilaTipos = []
		self.pilaOperadores = []
		self.cuadruplos = []
		#Para los saltos tipo gotoF y gotoV
		self.saltos = []
		#Para los de regreso
		self.regresa = []
		#Empieza contador de cuadruplos
		self.numCuadruplo = 1
		#Sirve para ver si una funcion puede tener return o no
		self.tieneReturn = False
		#Sirve para crear el diccionario de arreglos
		self.arreglos = {}
		#Mete el arreglo para poder hacer su cuadruplo
		self.stackArreglos = []		

	def printCuadruplos(self):
		for cuadruplo in self.cuadruplos:
			print(cuadruplo)
