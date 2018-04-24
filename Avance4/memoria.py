import sys

class TipoSegmento():

	def __init__(self, nombreSegmento, empiezaMem, acabaMem):
		self.nombre = nombreSegmento
		self.empiezaMem = empiezaMem
		self.acabaMem = acabaMem
		self.memoriaActual = empiezaMem
		self.segmento = {}

	def __str__(self):
		return ("Segment : " + self.nombre + "\n" + "Initial address: " + str(self.empiezaMem) + "\n" + "Final address: " + str(self.acabaMem) + "\n" + "Current address " + str(self.memoriaActual) + "\n" + "Addresses " + str(self.segmento))

	def Disponible(self, cantidad = 0):
		if self.memoriaActual + cantidad <= self.acabaMem:
			return True
		else:
			return False

	def PideDireccion(self, valor):
		if self.Disponible():
			direccion = self.memoriaActual
			self.segmento[direccion] = valor
			self.memoriaActual += 1
			return direccion
		else:
			print("There is no available space in the " + self.nombre + " memory segment")
			sys.exit()

	def ChecaValor(self, valorAChecar):
		for direccion, valor in self.segmento.items():
			if valor == valorAChecar:
				return direccion
		return None

	def Resetea(self):
		self.segmento.clear()
		self.memoriaActual = self.empiezaMem

	def Valor(self, direccion):
		return self.segmento[direccion]

	def ModificaValor(self, direccion, valor):
		self.segmento[direccion] = valor

	def PideMemoriaArreglo(self, cantidad, valor):
		if self.Disponible(cantidad):
			direccionInicial = self.memoriaActual
			for i in range(cantidad):
				self.segmento[self.memoriaActual] = valor
				self.memoriaActual += 1
			return direccionInicial
		else:
			print("No more memoria space")
			sys.exit()
			


class MemoriaSegmentada():

	def __init__(self, ubicacionMem, empiezaMem, cantidadMem):
		self.nombreMem = ubicacionMem
		self.tamanoSeg = int(cantidadMem / 4)
		self.empiezaMem = empiezaMem
		self.acabaMem = empiezaMem + cantidadMem - 1
		self.empiezaIntMem = empiezaMem
		self.acabaIntMem = empiezaMem + self.tamanoSeg - 1
		self.empiezaDecimalMem = empiezaMem + self.tamanoSeg
		self.acabaDecimalMem = empiezaMem + (self.tamanoSeg * 2) - 1
		self.empiezaStringMem = empiezaMem + (self.tamanoSeg * 2)
		self.acabaStringMem = empiezaMem + (self.tamanoSeg * 3) - 1
		self.empiezaBoolMem = empiezaMem + (self.tamanoSeg * 3)
		self.acabaBoolMem = empiezaMem + (self.tamanoSeg * 4) - 1
		self.segmentoInt = TipoSegmento('Integer', self.empiezaIntMem, self.acabaIntMem)
		self.segmentoDecimal = TipoSegmento('Decimal', self.empiezaDecimalMem, self.acabaDecimalMem)
		self.segmentoString = TipoSegmento('String', self.empiezaStringMem, self.acabaStringMem)
		self.segmentoBool = TipoSegmento('Boolean', self.empiezaBoolMem, self.acabaBoolMem)

	def PideMemoria(self, tipoVariable, valor = None):
		if tipoVariable == 'int':
			if valor is None:
				valor = 0
			return self.segmentoInt.PideDireccion(valor)
		elif tipoVariable == 'decimal':
			if valor is None:
				valor = 0.0
			return self.segmentoDecimal.PideDireccion(valor)
		elif tipoVariable == 'string':
			if valor is None:
				valor = ""
			return self.segmentoString.PideDireccion(valor)
		elif tipoVariable == 'bool':
			if valor is None:
				valor = False
			return self.segmentoBool.PideDireccion(valor)

	def ChecaValor(self, tipoVariable, valor):
		if tipoVariable == 'int':
			return self.segmentoInt.ChecaValor(valor)
		elif tipoVariable == 'decimal':
			return self.segmentoDecimal.ChecaValor(valor)
		elif tipoVariable == 'string':
			return self.segmentoString.ChecaValor(valor)
		elif tipoVariable =='bool':
			return self.segmentoBool.ChecaValor(valor)

	def ReseteaMemoria(self):
		self.segmentoInt.Resetea()
		self.segmentoDecimal.Resetea()
		self.segmentoString.Resetea()
		self.segmentoBool.Resetea()
	
	def Valor(self, direccion):
		tipoSegmento = self.TipoSegmento(direccion)
		if tipoSegmento == 'Int':
			return self.segmentoInt.Valor(direccion)
		if tipoSegmento == 'Decimal':
			return self.segmentoDecimal.Valor(direccion)
		if tipoSegmento == 'String':
			return self.segmentoString.Valor(direccion)
		if tipoSegmento == 'Bool':
			return self.segmentoBool.Valor(direccion)

	def ModificaValor(self, direccion, valor):
		tipoSegmento = self.TipoSegmento(direccion)
		if tipoSegmento == 'Int':
			return self.segmentoInt.ModificaValor(direccion, valor)
		if tipoSegmento == 'Decimal':
			return self.segmentoDecimal.ModificaValor(direccion, valor)
		if tipoSegmento == 'String':
			return self.segmentoString.ModificaValor(direccion, valor)
		if tipoSegmento == 'Bool':
			return self.segmentoBool.ModificaValor(direccion, valor)
	
	def TipoSegmento(self, direccion):
		if direccion >= self.empiezaIntMem and direccion <= self.acabaIntMem:
			return 'Int'
		if direccion >= self.empiezaDecimalMem and direccion <= self.acabaDecimalMem:
			return 'Decimal'
		if direccion >= self.empiezaStringMem and direccion <= self.acabaStringMem:
			return 'String'
		if direccion >= self. empiezaBoolMem and direccion <= self.empiezaBoolMem:
			return 'Bool' 

	def PideMemoriaArreglo(self, tipoVariable, cantidad, valor = None):
		if tipoVariable == 'int':
			if valor is None:
				valor = 0
			return self.segmentoInt.PideMemoriaArreglo(cantidad, valor)
		if tipoVariable == 'decimal':
			if valor is None:
				valor = 0.0
			return self.segmentoDecimal.PideMemoriaArreglo(cantidad, valor)
		if tipoVariable == 'string':
			if valor is None:
				valor = ""
			return self.segmentoString.PideMemoriaArreglo(cantidad, valor)
		if tipoVariable == 'bool':
			if valor is None:
				valor = False
			return self.segmentoBool.PideMemoriaArreglo(cantidad, valor)

class Memoria():

	def __init__(self):
		self.memGlobales = MemoriaSegmentada('Global', 5000, 2000)
		self.memLocales = MemoriaSegmentada('Local', 9000, 2000)
		self.memConstantes = MemoriaSegmentada('Constant', 20000, 2000)
		self.memTemporales = MemoriaSegmentada('Temporal', 43000, 2000)

	def MemoriaGlobal(self, tipoVariable, valor = None,):
		return self.memGlobales.PideMemoria(tipoVariable, valor)

	def MemoriaLocal(self, tipoVariable, valor = None,):
		return self.memLocales.PideMemoria(tipoVariable, valor)

	def MemoriaConstante(self, tipoVariable, valor = None):
		return self.memConstantes.PideMemoria(tipoVariable, valor)

	def MemoriaTemporal(self, tipoVariable, valor = None):
		return self.memTemporales.PideMemoria(tipoVariable, valor)

	def ChecaConstante(self, tipoVariable, valor):
		return self.memConstantes.ChecaValor(tipoVariable, valor)
	
	def ReseteaMemoria(self):
		self.memLocales.ReseteaMemoria()
		self.memTemporales.ReseteaMemoria()

	def Valor(self, direccion):
		tipoVariable = self.TipoMemoria(direccion)
		if tipoVariable == 'Global':
			return self.memGlobales.Valor(direccion)
		if tipoVariable == 'Local':
			return self.memLocales.Valor(direccion)
		if tipoVariable == 'Constante':
			return self.memConstantes.Valor(direccion)
		if tipoVariable == 'Temporal':
			return self.memTemporales.Valor(direccion)

	def ModificaValor(self, direccion, valor):
		tipoVariable = self.TipoMemoria(direccion)
		if tipoVariable == 'Global':
			return self.memGlobales.ModificaValor(direccion, valor)
		if tipoVariable == 'Local':
			return self.memLocales.ModificaValor(direccion, valor)
		if tipoVariable == 'Constante':
			return self.memConstantes.ModificaValor(direccion, valor)
		if tipoVariable == 'Temporal':
			return self.memTemporales.ModificaValor(direccion, valor)
	 
	def TipoMemoria(self, direccion):
		if direccion >= self.memGlobales.empiezaMem and direccion <= self.memGlobales.acabaMem:
			return 'Global'
		if direccion >= self.memLocales.empiezaMem and direccion <= self.memLocales.acabaMem:
			return 'Local'
		if direccion >= self.memConstantes.empiezaMem and direccion <= self.memConstantes.acabaMem:
			return 'Constante'
		if direccion >= self.memTemporales.empiezaMem and direccion <= self.memTemporales.acabaMem:
			return 'Temporal'	

	def MemoriaGlobalArreglo(self, tipoVariable, cantidad, valor = None):
		return self.memGlobales.PideMemoriaArreglo(tipoVariable, cantidad, valor)
	
	def MemoriaLocalArreglo(self, tipoVariable, cantidad, valor = None):
		return self.memLocales.PideMemoriaArreglo(tipoVariable, cantidad, valor)
