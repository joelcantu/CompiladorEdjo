class TablaVariables():

	def __init__(self):
		self.listaVariables = {}

	#Mete variable
	def AgregaVariable(self, tipoVariable, nombreVariable, memoriaVariable = 0):
		self.listaVariables[nombreVariable] = {
			'Type' : tipoVariable,
			'Name' : nombreVariable,
			'MemoryAddress' : memoriaVariable
		}

	#Verifica si la variable existe
	def TieneVariable(self, nombreVariable):
		return nombreVariable in self.listaVariables.keys()

	#Regresa la variable
	def RegresaVariable(self, nombreVariable):
		if self.TieneVariable(nombreVariable):
			return self.listaVariables[nombreVariable]
		else:
			return None

	#Mete arreglo dentro de la tabla de variable
	def AgregaArreglo(self, variable):
		self.listaVariables[variable['Name']] = variable

	def __str__(self):
		return self.listaVariables

class DirFuncion():

	def __init__(self):
		self.listaFunciones = {}

	#Agrega una nueva funcion al diccionario
	def AgregaFuncion(self, nombreFuncion, tipoFuncion, tipoParametros = [], nombreParametros = [], memoriaParametros = []):
		self.listaFunciones[nombreFuncion] = {
			'Name' : nombreFuncion,
			'Return' : tipoFuncion,
			'ReturnMemory' : -1,
			'Quadruple' : -1,
			'Parameters' : {
				'Types' : tipoParametros,
				'Names' : nombreParametros,
				'Addresses' : memoriaParametros,
			},
			'Variables': TablaVariables(),
			'LocalVariables' : {
				'int' : 0,
				'decimal' : 0,
				'string' : 0,
				'bool' : 0
			},
			'TemporalVariables' : {
				'int' : 0,
				'decimal' : 0,
				'string' : 0,
				'bool' : 0
			}
		}

	#Checa si exisite cierta funcion
	def TieneFuncion(self, nombreFuncion):
		return nombreFuncion in self.listaFunciones.keys()

	#Regresa toda la funcion
	def RegresaFuncion(self, nombreFuncion):
		if self.TieneFuncion(nombreFuncion):
			return self.listaFunciones[nombreFuncion]
		else:
			print("The function doesn't exist")
			return None

	#Agrega parametros a la funcionn
	def AgregaParametros(self, nombreFuncion, tipoParametros, nombreParametros, memoriaParametros):
		funcion = self.RegresaFuncion(nombreFuncion)
		if funcion is not None:
			funcion['Parameters']['Types'] = tipoParametros
			funcion['Parameters']['Names'] = nombreParametros
			funcion['Parameters']['Addresses'] = memoriaParametros
		else:
			print("The function doesn't exist")

	#Agrega una variable a la funcion
	def AgregaVariableFuncion(self, nombreFuncion, tipoVariable, nombreVariable, memoriaVariable=0):
		funcion = self.RegresaFuncion(nombreFuncion)
		if funcion is not None:
			if funcion['Variables'].TieneVariable(nombreVariable):
				print("This function already has a variable with that name")
			else:
				funcion['Variables'].AgregaVariable(tipoVariable, nombreVariable, memoriaVariable)
				funcion['LocalVariables'][tipoVariable] += 1
		else:
			print("The function doesnt exists")


	#Checa si la funcion tiene cierta variable	
	def ChecaVariable(self, nombreFuncion, nombreVariable):
		funcion = self.RegresaFuncion(nombreFuncion)
		if funcion is not None:
			if funcion['Variables'].TieneVariable(nombreVariable):
				return True
			else:
				return False
		else:
			print("The variable " + nombreVariable + " has been already declared")

	#Agrega una temporal a la funcion
	def AgregaTemporal(self, nombreFuncion, tipoTemporal):
		funcion = self.RegresaFuncion(nombreFuncion)
		if funcion is not None:
			funcion['TemporalVariables'][tipoTemporal] += 1
		else:
			print("The function doesnt exists")

	#Regresa alguna variable de cierta funcion	
	def RegresaVariableFuncion(self, nombreFuncion, nombreVariable):
		funcion = self.RegresaFuncion(nombreFuncion)
		if funcion is not None:
			variable = funcion['Variables'].RegresaVariable(nombreVariable)
			if variable is not None:
				return variable
			else:
				return None
		else:
			print("The function doesn't exists")

	#Regresa el tipo de funcion
	def RegresaTipoFuncion(self, nombreFuncion):
		funcion = self.RegresaFuncion(nombreFuncion)
		if funcion is not None:
			tipoFuncion = funcion['Return']
			return tipoFuncion
		else:
			print("The function doesn't exists")

	#Regresa los parametros de una funcion
	def RegresaParametrosFuncion(self, nombreFuncion):
		funcion = self.RegresaFuncion(nombreFuncion)
		if funcion is not None:
			return funcion['Parameters']
		else:
			print("The function doesn't exists")
	
	#Asinga el numero del cuadruplo de la funcion
	def AsignaNumeroCuadruplo(self, nombreFuncion, numCuadruplo):
		funcion = self.RegresaFuncion(nombreFuncion)
		if funcion is not None:
			funcion['Quadruple'] = numCuadruplo
		else:
			print("The function doesn't exists")

	#Si la funcion es de tipo no void, asigna una direccion de memoria al return del final
	def AsignaMemoriaFuncion(self, nombreFuncion, memoria):
		funcion = self.RegresaFuncion(nombreFuncion)
		if funcion is not None:
			funcion['ReturnMemory'] = memoria
		else:
			print("The function doesn't exists")

	#Regresa el numero de cuadruplo
	def RegresaNumeroCuadruplo(self, nombreFuncion):
		funcion = self.RegresaFuncion(nombreFuncion)
		if funcion is not None:
			return funcion['Quadruple']
		else:
			print("The function doesn't exists")

	#Aregrega Arreglos a una funcion
	def AgregaArregloFuncion(self, nombreFuncion, variable):
		funcion = self.RegresaFuncion(nombreFuncion)
		if funcion is not None:
			if funcion['Variables'].TieneVariable(variable['Name']):
				print("Variable already declared")
			else:
				funcion['Variables'].AgregaArreglo(variable)
				for i in range(variable['LimiteSuperior']):
					funcion['LocalVariables'][variable['Type']] += 1
		else:
			print("The function doesn't exists")

	def printDirFuncion(self):
		for funcion, properties in self.listaFunciones.items():
			print("Function : " + str(funcion))
			for prop, value in properties.items():
				if isinstance(value, TablaVariables):
					print("\t" + str(prop) + " : " + str(value.listaVariables))
				elif isinstance(value, dict):
					print("\t" + str(prop) + " : " + str(value))
				else:
					print("\t" + str(prop) + " : " + str(value))
			print("\n")
