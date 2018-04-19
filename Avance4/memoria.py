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

	def Disponible(self):
		if self.memoriaActual <= self.acabaMem:
			return True
		else:
			return False

	def PideDireccion(self, value):
		if self.Disponible():
			direccion = self.memoriaActual
			self.segmento[direccion] = value
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
		self.segment.clear()
		self.memoriaActual = self.empiezaMem



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

