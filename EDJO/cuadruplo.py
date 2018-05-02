class Cuadruplo():
	def __init__(self, numCuadruplo, operador, operandoIzq, operandoDer, resultado):
		self.numCuadruplo = numCuadruplo
		self.operador = operador
		self.operandoIzq = operandoIzq
		self.operandoDer = operandoDer
		self.resultado = resultado

	#Llena el salto para ir a otro cuadruplo
	def LlenaResultado(self, numCuadruplo):
		self.resultado = numCuadruplo

	def __str__(self):
		return (str(self.numCuadruplo)  + "\t | \t" + str(self.operador) + "\t | \t" + str(self.operandoIzq) + "\t |  \t" + str(self.operandoDer) + "\t |  \t" + str(self.resultado))
