import ply.lex as lex
import sys
from core import Core
from cuadruplo import Cuadruplo

#TOKENS#
tokens = (
'LT',
'EQ',
'GT',
'NE',
'LE',
'GE',
'ASSIGN',
'PLUSPLUS',
'MINUSMINUS',
'PLUS',
'MINUS',
'MULT',
'DIV',
'LPAREN',
'RPAREN',
'LBRACKET',
'RBRACKET',
'SLBRACKET',
'SRBRACKET',
'SEMICOLON',
'COMMA',
'IF',
'ELSE',
'INT',
'DECIMAL',
'STRING',
'CHAR',
'BOOL',
'PRINT',
'START',
'EDJO',
'VOID',
'RETURN',
'MAIN',
'FOR',
'VAR_ID',
'VAR_INT',
'VAR_DECIMAL',
'VAR_STRING',
'TRUE',
'FALSE',
'DO',
'WHILE',
'POINT',
'POS',
'FORWARD',
'CIRCLE',
'LEFT',
'RIGHT',
'TUR',
'TURTLE',
'ZERO',
'RET',
'FUNC',
'FINISH'
)

#Palabras reservadas#
reserved = {
'if'		:	'IF',
'else'		:	'ELSE',
'for'		:	'FOR',
'int'		:	'INT',
'do'		:	'DO',
'while'		:	'WHILE',
'decimal'	:	'DECIMAL',
'string'	:	'STRING',
'char'		:	'CHAR',
'bool'		:	'BOOL',
'void'		:	'VOID',
'return'	:	'RETURN',
'main'		:	'MAIN',
'print'		:	'PRINT',
'start'		:	'START',
'EDJO'		:	'EDJO',
'true'		:	'TRUE',
'false'		:	'FALSE',
'turtle'	:	'TUR',
'Turtle'	:	'TURTLE',
'pos'		:	'POS',
'forward'	:	'FORWARD',
'circle'	:	'CIRCLE',
'left'		:	'LEFT',
'right'		:	'RIGHT',
'zero'		:	'ZERO',
'Return'	:	'RET',
'func'		:	'FUNC',
'finish'	:	'FINISH'
}

#Expresiones regulares para los tokens simples#
t_LT = r'<'
t_GT = r'>'
t_EQ = r'=='
t_NE = r'!='
t_LE = r'<='
t_GE = r'>='

t_ASSIGN = r'='
t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'--'

t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_SLBRACKET = r'\['
t_SRBRACKET = r'\]'


t_SEMICOLON = r';'
t_COMMA = r','
t_POINT = r'\.'

#ignora espacios y tabs
t_ignore = ' \t' 

#Expresiones regulares con reglas
def t_newline(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")

def t_error(t):
	print("Illegal character '%s" % t.value[0])
	t.lexer.skip(1)

def t_TRUE(t):
	r'(true)'
	t.value = True
	return t

def t_FALSE(t):
	r'(false)'
	t.value = False
	return t

def t_VAR_DECIMAL(t):
	r'\d+\.\d+'
	t.value = float(t.value)
	return t

def t_VAR_INT(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_VAR_STRING(t):
	r'\"(\\.|[^\\"])*\"'
	t.value = t.value[1:-1]
	return t

def t_VAR_ID(t):
	r'[a-zA-Z](_?([a-zA-Z]|[0-9]))*'
	t.type = reserved.get(t.value,'VAR_ID') #checa for las palabras reservadas
	return t


lexer = lex.lex()
file = open('prueba.txt','r')
lexer.input(file.read())

#while True:
#	tok = lexer.token()
#	if not tok:
#		break
#	print(tok)

edjo = Core()
def p_inicio(p):
	'''program	:	START EDJO VAR_ID crea_primer_cuadruplo crea_funcion_global SEMICOLON Vars funciones Main
	'''

#Crea primer Cuadruplo
def p_crea_primer_cuadruplo(p):
	'''crea_primer_cuadruplo	: 
	'''
	cuadruplo = Cuadruplo(edjo.numCuadruplo,'GOTO', 'MAIN', None, None)
	edjo.cuadruplos.append(cuadruplo)
	edjo.numCuadruplo += 1

#Crea funcion global
def p_crea_funcion_global(p):
	'''crea_funcion_global	: 
	'''
	edjo.funcionGlobal = p[-2]
	edjo.funcionLocal = p[-2]
	edjo.dirFuncion.AgregaFuncion(edjo.funcionGlobal, 'void')
	
def p_Vars(p):
	'''Vars		:	Tipo VAR_ID mas_vars agrega_var_funcion SEMICOLON Vars
			|	Tipo VAR_ID SLBRACKET VAR_INT push_int_PilaOperandos SRBRACKET agrega_limites_arreglo agrega_arr_funcion SEMICOLON Vars
			| 
	'''
def p_agrega_limites_arreglo(p):
	'''agrega_limites_arreglo	: 
	'''
	#Crea el diccionario de un arreglo con su limite superior
	nombreArreglo = p[-5]
	tamanoArregloMemoria = edjo.pilaOperandos.pop()
	tamanoArreglo = edjo.memoria.Valor(tamanoArregloMemoria)
	tipoArreglo = edjo.pilaTipos.pop()
	if tamanoArreglo <= 0:
		print("Arrays can't be less than or equal to 0")
		sys.exit()
	edjo.arreglos = {
		'Name' : nombreArreglo,
		'LimiteInferior' : 0,
		'LimiteSuperior' : tamanoArreglo
	}

def p_agrega_arr_funcion(p):
	'''agrega_arr_funcion	: 
	'''
	#Mete el arreglo en la funcion
	tipoVariable = p[-7]
	variable = edjo.arreglos
	verificaVariable = edjo.dirFuncion.ChecaVariable(edjo.funcionLocal, variable['Name'])
	if not verificaVariable:
		if edjo.funcionLocal == edjo.funcionGlobal:
			memoriaVariable = edjo.memoria.MemoriaGlobalArreglo(tipoVariable, variable['LimiteSuperior'])
		else:
			memoriaVariable = edjo.memoria.MemoriaLocalArreglo(tipoVariable, variable['LimiteSuperior'])
		variable['Type'] = tipoVariable
		variable['MemoryAddress'] = memoriaVariable
		edjo.dirFuncion.AgregaArregloFuncion(edjo.funcionLocal, variable)
	else:
		print("Variable " + variable['Name'] + " has already been declared")
		sys.exit()	

def p_Tipo(p):
	'''Tipo		:	INT
			|	DECIMAL
			|	STRING
			|	CHAR
			|	BOOL
	'''
	p[0] = p[1]

def p_mas_vars(p):
	'''mas_vars	:	COMMA VAR_ID mas_vars
			| 
	'''
	if p[-1] is not None:
		nombreVariable = p[-1]
		edjo.variablesTemp.append(nombreVariable)

#Agrega la variable a la funcion actual ya sea global o local
def p_agrega_var_funcion(p):
	'''agrega_var_funcion	: 
	'''
	tipoVariable = p[-3]
	edjo.variablesTemp.reverse()
	for variable in edjo.variablesTemp:
		verificaVariable = edjo.dirFuncion.ChecaVariable(edjo.funcionLocal, variable)
		if not verificaVariable:
			if edjo.funcionLocal == edjo.funcionGlobal:
				memoriaVariable = edjo.memoria.MemoriaGlobal(tipoVariable)
			else:
				memoriaVariable = edjo.memoria.MemoriaLocal(tipoVariable)			
			edjo.dirFuncion.AgregaVariableFuncion(edjo.funcionLocal, tipoVariable, variable, memoriaVariable)
		else:
			print("Variable " + variable + " has already been declared")
			sys.exit()
	del edjo.variablesTemp[:]

def p_Asignacion(p):
	'''Asignacion	:	VAR_ID push_var_PilaOperandos ASSIGN push_operador_PilaOperadores ExpI SEMICOLON resuelve_asignacion
	'''

#Push el id a la pila operandos 
def p_push_var_PilaOperandos(p):
	'''push_var_PilaOperandos	: 
	'''
	variable = edjo.dirFuncion.RegresaVariableFuncion(edjo.funcionLocal, p[-1])
	if variable is None:
		variable = edjo.dirFuncion.RegresaVariableFuncion(edjo.funcionGlobal, p[-1])
		if variable is None:
			print("The variable " + p[-1] + " has not been declared")
			sys.exit()
		else:
			edjo.pilaOperandos.append(variable['MemoryAddress'])
			edjo.pilaTipos.append(variable['Type'])
	else:
		edjo.pilaOperandos.append(variable['MemoryAddress'])
		edjo.pilaTipos.append(variable['Type'])

#Push el operador al pila operadores
def p_push_operador_PilaOperadores(p):
	'''push_operador_PilaOperadores	: 
	'''
	edjo.pilaOperadores.append(p[-1])

#Resuelve la asignacion
def p_resuelve_asignacion(p):
	'''resuelve_asignacion	: 
	'''
	operador = edjo.pilaOperadores.pop()
	if operador == '=':
		operandoDer = edjo.pilaOperandos.pop()
		tipoOperandoDer = edjo.pilaTipos.pop()
		operandoIzq = edjo.pilaOperandos.pop()
		tipoOperandoIzq = edjo.pilaTipos.pop()
		resultado = edjo.cuboSemantico.get_semantic_type(tipoOperandoIzq, tipoOperandoDer, operador)
		if resultado != 'error':
			cuadruplo = Cuadruplo(edjo.numCuadruplo, operador, operandoDer, None, operandoIzq)
			edjo.cuadruplos.append(cuadruplo)
			edjo.numCuadruplo += 1
		else:
			print('Operation type mismatch at {0}'.format(p.lexer.lineno))
			sys.exit()


def p_ExpI(p):
	'''ExpI		:	ExpK resuelve_operadores_relacionales 
			|	ExpK Operandos push_operador_PilaOperadores ExpK resuelve_operadores_relacionales
	'''

def p_Operandos(p):
	'''Operandos	:	LT
			|	GT
			|	NE
			|	LE
			|	GE
			|	EQ
	'''
	p[0] = p[1]

#Resuelve operadores relacionales
def p_resuelve_operadores_relacionales(p):
	'''resuelve_operadores_relacionales	: 
	'''
	if len(edjo.pilaOperadores) > 0 and len(edjo.pilaOperandos) > 1:
		if edjo.pilaOperadores[-1] == '<=' or edjo.pilaOperadores[-1] == '<' or edjo.pilaOperadores[-1] == '>=' or edjo.pilaOperadores[-1] == '>' or edjo.pilaOperadores[-1] == '==' or edjo.pilaOperadores[-1] == '!=':
			resuelve_operacion(p)

#Resuelve operacion
def resuelve_operacion(p):
	operandoDer = edjo.pilaOperandos.pop()
	operandoIzq = edjo.pilaOperandos.pop()
	tipoOperandoDer = edjo.pilaTipos.pop()
	tipoOperandoIzq = edjo.pilaTipos.pop()
	operador = edjo.pilaOperadores.pop()
	resultado = edjo.cuboSemantico.get_semantic_type(tipoOperandoIzq, tipoOperandoDer, operador)
	if resultado != 'error':
		memTemp = edjo.memoria.MemoriaTemporal(resultado)
		edjo.dirFuncion.AgregaTemporal(edjo.funcionLocal, resultado)
		cuadruplo = Cuadruplo(edjo.numCuadruplo, operador, operandoIzq, operandoDer, memTemp)
		edjo.cuadruplos.append(cuadruplo)
		edjo.numCuadruplo += 1
		edjo.pilaOperandos.append(memTemp)
		edjo.pilaTipos.append(resultado)
	else:
		print('Operation type mismatch at {0}'.format(p.lexer.lineno))
		sys.exit()
	
def p_ExpK(p):
	'''ExpK		:	ExpT resuelve_termino 
			|	ExpT resuelve_termino pos_SUMRES push_operador_PilaOperadores ExpK
	'''

#Resuelve termino
def p_resuelve_termino(p):
	'''resuelve_termino	: 
	'''
	if len(edjo.pilaOperadores) > 0 and len(edjo.pilaOperandos) > 1:
		if edjo.pilaOperadores[-1] == '+' or edjo.pilaOperadores[-1] == '-':
			resuelve_operacion(p)


def p_pos_SUMRES(p):
	'''pos_SUMRES	:	PLUS 
			|	MINUS 
	'''
	p[0] = p[1]

def p_ExpT(p):
	'''ExpT		:	ExpF resuelve_factor 
			|	ExpF resuelve_factor pos_MULTDIV push_operador_PilaOperadores ExpT
	'''

#Resuelve factor
def p_resuelve_factor(p):
	'''resuelve_factor	: 
	'''
	if len(edjo.pilaOperadores) > 0 and len(edjo.pilaOperandos) > 1:
		if edjo.pilaOperadores[-1] == '*' or edjo.pilaOperadores[-1] == '/':
			resuelve_operacion(p)


def p_pos_MULTDIV(p):
	'''pos_MULTDIV	:	MULT 
			|	DIV 
	'''
	p[0] = p[1]

def p_ExpF(p):
	'''ExpF		:	VAR_CTE
			|	LPAREN agrega_falso ExpI RPAREN quita_falso
			|	VAR_ID push_var_PilaOperandos pos_arreglo
			|	llama_funcion 
	'''
	#falta arreglos

def p_VAR_CTE(p):
	'''VAR_CTE	:	VAR_INT push_int_PilaOperandos
			|	VAR_DECIMAL push_decimal_PilaOperandos
			|	VAR_STRING push_string_PilaOperandos
			|	VAR_BOOL push_bool_PilaOperandos
	'''

def p_VAR_BOOL(p):
	'''VAR_BOOL	:	FALSE
			|	TRUE
	'''
	p[0] = p[1]

#Push int pila operandos
def p_push_int_PilaOperandos(p):
	'''push_int_PilaOperandos	:
	'''
	memConst = edjo.memoria.ChecaConstante('int', int(p[-1]))
	if memConst is None:
		memConst = edjo.memoria.MemoriaConstante('int', int(p[-1]))
	edjo.pilaOperandos.append(memConst)
	edjo.pilaTipos.append('int')
		
#Push decimal pila operandos
def p_push_decimal_PilaOperandos(p):
	'''push_decimal_PilaOperandos	: 
	'''
	memConst = edjo.memoria.ChecaConstante('decimal', float(p[-1]))
	if memConst is None:
		memConst = edjo.memoria.MemoriaConstante('decimal', float(p[-1]))
	edjo.pilaOperandos.append(memConst)
	edjo.pilaTipos.append('decimal')

#Push string pila operandos	
def p_push_string_PilaOperandos(p):
	'''push_string_PilaOperandos	: 
	'''
	memConst = edjo.memoria.ChecaConstante('string', str(p[-1]))
	if memConst is None:
		memConst = edjo.memoria.MemoriaConstante('string', str(p[-1]))
	edjo.pilaOperandos.append(memConst)
	edjo.pilaTipos.append('string')

#Push bool pila operandos
def p_push_bool_PilaOperandos(p):
	'''push_bool_PilaOperandos	: 
	'''
	if p[-1] is False:
		memConst = edjo.memoria.ChecaConstante('bool', False)
		if memConst is None:
			memConst = edjo.memoria.MemoriaConstante('bool', False)
		edjo.pilaOperandos.append(memConst)
		edjo.pilaTipos.append('bool')
	else:
		memConst = edjo.memoria.ChecaConstante('bool', True)
		if memConst is None:
			memConst = edjo.memoria.MemoriaConstante('bool', True)
		edjo.pilaOperandos.append(memConst)
		edjo.pilaTipos.append('bool')

#Crea la marca falsa 
def p_agrega_falso(p):
	'''agrega_falso	: 
	'''
	edjo.pilaOperadores.append('(')

#Elimina la marca falsa
def p_quita_falso(p):
	'''quita_falso	: 
	'''
	edjo.pilaOperadores.pop()

#Llama funcion con valor diferente a void
def p_llama_funcion(p):
	'''llama_funcion	:	VAR_ID LPAREN agrega_falso checa_funcion_si_existe argumentos RPAREN quita_falso resuelve_llamada_funcion guarda_resultado_funcion
	'''

#Checa si la funcion existe
def p_checa_funcion_si_existe(p):
	'''checa_funcion_si_existe	: 
	'''
	funcion = p[-3]
	if edjo.dirFuncion.TieneFuncion(funcion):
		cuadruplo = Cuadruplo(edjo.numCuadruplo, 'ERA', funcion, None, None)
		edjo.cuadruplos.append(cuadruplo)
		edjo.numCuadruplo += 1
		parametros = edjo.dirFuncion.RegresaParametrosFuncion(funcion)
		edjo.tiposArgumentos = list(parametros['Types'])
	else:
		print("The function " +  funcion + " doesn't exist")
		sys.exit()


def p_argumentos(p):
	'''argumentos	:	ExpI resuelve_argumentos mas_argumentos
			| 
	'''

def p_mas_argumentos(p):
	'''mas_argumentos	: 	COMMA ExpI resuelve_argumentos mas_argumentos
				| 
	'''

#Resuelve argumentos
def p_resuelve_argumentos(p):
	'''resuelve_argumentos	: 
	'''
	if edjo.tiposArgumentos:
		argumento = edjo.pilaOperandos.pop()
		tipoArgumento = edjo.pilaTipos.pop()
		tipoParametro = edjo.tiposArgumentos.pop(0)
		if tipoArgumento == tipoParametro:
			cuadruplo = Cuadruplo(edjo.numCuadruplo, 'PARAMETER', argumento, None, None)
			edjo.cuadruplos.append(cuadruplo)
			edjo.numCuadruplo += 1
		else:
			print('Argument type mismatch at {0} lines'.format(p.lexer.lineno))
			sys.exit()
	else:
		print('Argument number mismatch at {0} lines'.format(p.lexer.lineno))
		sys.exit()

#Resuelve llamada funcion
def p_resuelve_llamada_funcion(p):
	'''resuelve_llamada_funcion	: 
	'''
	if not edjo.tiposArgumentos:
		funcion = p[-7]
		numInicioFuncion = edjo.dirFuncion.RegresaNumeroCuadruplo(funcion)
		cuadruplo = Cuadruplo(edjo.numCuadruplo, 'GOSUB', funcion, None, numInicioFuncion)
		edjo.cuadruplos.append(cuadruplo)
		edjo.numCuadruplo += 1
	else:
		print('Argument number mismatch at {0} line '.format(p.lexer.lineno))
		sys.exit()

#Guarda resultado de funcion
def p_guarda_resultado_funcion(p):
	'''guarda_resultado_funcion	: 
	'''
	nomFuncion = p[-8]
	funcion = edjo.dirFuncion.RegresaFuncion(nomFuncion)
	valorRetorno = funcion['ReturnMemory']
	tipoFuncion = funcion['Return']
	memTemp = edjo.memoria.MemoriaTemporal(tipoFuncion)
	edjo.dirFuncion.AgregaTemporal(edjo.funcionLocal, tipoFuncion)
	cuadruplo = Cuadruplo(edjo.numCuadruplo, '=', valorRetorno, None, memTemp)
	edjo.cuadruplos.append(cuadruplo)
	edjo.numCuadruplo += 1
	edjo.pilaOperandos.append(memTemp)
	edjo.pilaTipos.append(tipoFuncion)
	

def p_pos_arreglo(p): #todavia no tenemos arreglos
	'''pos_arreglo	:	SLBRACKET ExpI SRBRACKET
			| 
	'''


def p_funciones(p):
	'''funciones	:	FUNC tipo_funcion VAR_ID LPAREN param RPAREN agrega_funcion LBRACKET Vars reg_brack RBRACKET fin_func_cuad funciones
			| 
	''' 

def p_tipo_funcion(p):
	'''tipo_funcion	:	VOID
			|	Tipo
	'''
	p[0] = p[1]

def p_param(p):
	'''param	:	Tipo VAR_ID pos_commaf
			| 
	'''

def p_pos_commaf(p):
	'''pos_commaf	:	COMMA Tipo VAR_ID pos_commaf
			| 
	'''
	if p[-1] is not None:
		nombreParametro = p[-1]
		tipoParametro = p[-2]
		edjo.nombresParametros.insert(0, nombreParametro)
		edjo.tiposParametros.insert(0, tipoParametro)

#Agrega nueva funcion
def p_agrega_funcion(p):
	'''agrega_funcion	: 
	'''
	edjo.funcionLocal = p[-4]
	tipoFuncion = p[-5]
	memoriaParametros = []
	edjo.dirFuncion.AgregaFuncion(edjo.funcionLocal, tipoFuncion)
	edjo.dirFuncion.AsignaNumeroCuadruplo(edjo.funcionLocal, edjo.numCuadruplo)
	if tipoFuncion != 'void':
		function_address = edjo.memoria.MemoriaGlobal(tipoFuncion)
		edjo.dirFuncion.AsignaMemoriaFuncion(edjo.funcionLocal, function_address)
	parametros = zip(edjo.nombresParametros, edjo.tiposParametros)
	for nombreParametro, tipoParametro in parametros:
		parameter_address = edjo.memoria.MemoriaLocal(tipoParametro)
		memoriaParametros.append(parameter_address)
		edjo.dirFuncion.AgregaVariableFuncion(edjo.funcionLocal, tipoParametro, nombreParametro, parameter_address)
	edjo.dirFuncion.AgregaParametros(edjo.funcionLocal, list(edjo.tiposParametros), list(edjo.nombresParametros), list(memoriaParametros))
	del edjo.nombresParametros[:]
	del edjo.tiposParametros[:]

#Crea cuadruplo fin de funcion	
def p_fin_func_cuad(p):
	'''fin_func_cuad	: 
	'''
	tipoFuncion = p[-10]
	if tipoFuncion == 'void' and edjo.tieneReturn:
		print('Function {0} of type {1} should not have return statement'.format(edjo.funcionLocal, tipoFuncion))
		sys.exit()
	elif tipoFuncion != 'void' and not edjo.tieneReturn:
		print('Function {0} of type {1} should have return statement'.format(edjo.funcionLocal, tipoFuncion))
		sys.exit()
	else:
		cuadruplo = Cuadruplo(edjo.numCuadruplo, 'ENDPROC', None, None, None)
		edjo.cuadruplos.append(cuadruplo)
		
	if edjo.tieneReturn:
		while edjo.regresa:
			cuadruploALlenar = edjo.regresa.pop()
			edjo.cuadruplos[cuadruploALlenar - 1].LlenaResultado(edjo.numCuadruplo)
	edjo.numCuadruplo += 1
	edjo.tieneReturn = False
	edjo.funcionLocal = edjo.funcionGlobal
	edjo.memoria.ReseteaMemoria()

def p_reg_brack(p):
	'''reg_brack	:	Estatutos reg_brack
			| 
	'''
def p_Estatutos(p):
	'''Estatutos	:	Condicion 
			|	Ciclo  
			|	Return 
			|	Asignacion
			|	Print 
			|	Llamada_Func 
			|	Turtle
	'''

def p_Condicion(p):
	'''Condicion	:	IF LPAREN ExpI RPAREN crea_GOTOF LBRACKET reg_brack RBRACKET pos_else llena_cuadruplo_if
	'''

def p_crea_GOTOF(p):
	'''crea_GOTOF	: 
	'''
	tipoResultado = edjo.pilaTipos.pop()
	if tipoResultado != 'bool':
		print('Operation type mismatch in line {0}'.format(p.lexer.lineno))
		sys.exit()
	else:
		resultado = edjo.pilaOperandos.pop()
		cuadruplo = Cuadruplo(edjo.numCuadruplo, 'GOTOF', resultado, None, None)
		edjo.cuadruplos.append(cuadruplo)
		edjo.saltos.append(edjo.numCuadruplo - 1)
		edjo.numCuadruplo += 1

def p_llena_cuadruplo_if(p):
	'''llena_cuadruplo_if	: 
	'''
	cuadruploALlenar = edjo.saltos.pop()
	cuadruplo = edjo.cuadruplos[cuadruploALlenar]
	cuadruplo.LlenaResultado(edjo.numCuadruplo)


def p_pos_else(p):
	'''pos_else	:	ELSE crea_else_cuadruplo LBRACKET reg_brack RBRACKET
			| 
	'''

def p_crea_else_cuadruplo(p):
	'''crea_else_cuadruplo	: 
	'''
	cuadruplo = Cuadruplo(edjo.numCuadruplo, 'GOTO', None, None, None)
	edjo.cuadruplos.append(cuadruplo)
	cuadruploALlenar = edjo.saltos.pop()
	cuadruplo = edjo.cuadruplos[cuadruploALlenar]
	edjo.saltos.append(edjo.numCuadruplo - 1)
	edjo.numCuadruplo += 1
	cuadruplo.LlenaResultado(edjo.numCuadruplo)

def p_Return(p):
	'''Return 	:	RETURN ExpI SEMICOLON resuelve_return
	'''

#Resuelve el return
def p_resuelve_return(p):
	'''resuelve_return	: 
	'''
	edjo.tieneReturn = True
	operando = edjo.pilaOperandos.pop()
	tipoOperando = edjo.pilaTipos.pop()
	funcion = edjo.dirFuncion.RegresaFuncion(edjo.funcionLocal)
	tipoFuncion = funcion['Return']
	memValorRetorno = funcion['ReturnMemory']
	if tipoFuncion != tipoOperando:
		print("Return type of function {0} doesn't match function return type".format(edjo.funcionLocal))
		sys.exit()
	cuadruplo = Cuadruplo(edjo.numCuadruplo, 'RETURN', operando, None, memValorRetorno)
	edjo.cuadruplos.append(cuadruplo)
	edjo.numCuadruplo += 1
	cuadruplo = Cuadruplo(edjo.numCuadruplo, 'GOTO', None, None, None)
	edjo.regresa.append(edjo.numCuadruplo)
	edjo.cuadruplos.append(cuadruplo)
	edjo.numCuadruplo += 1
	

def p_Print(p):
	'''Print	:	PRINT LPAREN ExpI RPAREN SEMICOLON crea_print
	'''

def p_crea_print(p):
	'''crea_print	: 
	'''
	operando = edjo.pilaOperandos.pop()
	cuadruplo = Cuadruplo(edjo.numCuadruplo, 'PRINT', operando, None, None)
	edjo.cuadruplos.append(cuadruplo)
	edjo.numCuadruplo += 1

#Llama funcion tipo void
def p_Llamada_Func(p):
	'''Llamada_Func	:	VAR_ID LPAREN agrega_falso checa_funcion_si_existe argumentos RPAREN quita_falso resuelve_llamada_funcion SEMICOLON checa_void
	'''

def p_checa_void(p):
	'''checa_void	: 
	'''
	funcion = p[-9]
	tipoFuncion = edjo.dirFuncion.RegresaTipoFuncion(funcion)
	if tipoFuncion != 'void':
		print("This function {0} is not a void function".format(funcion))
		sys.exit()

def p_Ciclo(p):
	'''Ciclo	:	For
			|	While
			|	DoWhile
	'''

def p_While(p):
	'''While	:	WHILE guarda_numero_cuadruplo LPAREN ExpI RPAREN crea_GOTOF LBRACKET reg_brack RBRACKET regresa_inicio_while
	'''

def p_guarda_numero_cuadruplo(p):
	'''guarda_numero_cuadruplo	: 
	'''
	edjo.saltos.append(edjo.numCuadruplo)
	
def p_regresa_inicio_while(p):
	'''regresa_inicio_while	: 
	'''
	cuadruploALlenar = edjo.saltos.pop()
	regresarCuadruplo = edjo.saltos.pop()
	cuadruploWhile = Cuadruplo(edjo.numCuadruplo, 'GOTO', None, None, regresarCuadruplo)
	edjo.cuadruplos.append(cuadruploWhile)
	edjo.numCuadruplo += 1
	cuadruploWhileALlenar = edjo.cuadruplos[cuadruploALlenar]
	cuadruploWhileALlenar.LlenaResultado(edjo.numCuadruplo)

def p_DoWhile(p):
	'''DoWhile	:	DO guarda_numero_cuadruplo LBRACKET reg_brack RBRACKET WHILE LPAREN ExpI RPAREN SEMICOLON crea_GOTOV
	'''

def p_crea_GOTOV(p):
	'''crea_GOTOV	: 
	'''
	tipoResultado = edjo.pilaTipos.pop()
	regresarCuadruplo = edjo.saltos.pop()
	if tipoResultado != 'bool':
		print('Operation type mismatch in line {0}'.format(p.lexer.lineno))
		sys.exit()
	else:
		resultado = edjo.pilaOperandos.pop()
		cuadruplo = Cuadruplo(edjo.numCuadruplo, 'GOTOV', resultado, None, regresarCuadruplo)
		edjo.cuadruplos.append(cuadruplo)
		edjo.saltos.append(edjo.numCuadruplo - 1)
		edjo.numCuadruplo += 1

def p_For(p):#todavia no
	'''For		:	FOR LPAREN VAR_ID ASSIGN ExpI SEMICOLON ExpI SEMICOLON VAR_ID Exp_ciclo RPAREN LBRACKET reg_brack RBRACKET
	'''

def p_Exp_ciclo(p):
	'''Exp_ciclo	:	PLUS VAR_INT
			|	MINUS VAR_INT
			|	MULT VAR_INT
			|	DIV VAR_INT
			|	PLUSPLUS
			|	MINUSMINUS
	'''



def p_Main(p):
	'''Main		:	MAIN agrega_main_funcion LPAREN RPAREN LBRACKET Vars reg_brack RET ZERO SEMICOLON RBRACKET
	'''

def p_agrega_main_funcion(p):
	'''agrega_main_funcion	: 
	'''
	edjo.funcionLocal = p[-1]
	edjo.dirFuncion.AgregaFuncion(edjo.funcionLocal, 'void')
	edjo.dirFuncion.AsignaNumeroCuadruplo(edjo.funcionLocal, edjo.numCuadruplo)
	cuadruplo = edjo.cuadruplos[0]
	cuadruplo.LlenaResultado(edjo.numCuadruplo)

def p_Turtle(p):
	'''Turtle	:	Forward
			|	Right
			|	Left
			|	Circle
			|	Position
			|	IniciaTurtle
			|	TerminaTurtle
	'''

def p_Forward(p):
	'''Forward	:	TUR POINT FORWARD LPAREN ExpI RPAREN SEMICOLON crea_cuadruplo_forward
	'''

def p_crea_cuadruplo_forward(p):
	'''crea_cuadruplo_forward	: 
	'''
	operando = edjo.pilaOperandos.pop()
	cuadruplo = Cuadruplo(edjo.numCuadruplo, 'TUR_FORWARD', operando, None, None)
	edjo.cuadruplos.append(cuadruplo)
	edjo.numCuadruplo += 1
 

def p_Right(p):
	'''Right	:	TUR POINT RIGHT LPAREN ExpI RPAREN SEMICOLON crea_cuadruplo_right
	'''

def p_crea_cuadruplo_right(p):
	'''crea_cuadruplo_right	: 
	'''
	operando = edjo.pilaOperandos.pop()
	cuadruplo = Cuadruplo(edjo.numCuadruplo, 'TUR_RIGHT', operando, None, None)
	edjo.cuadruplos.append(cuadruplo)
	edjo.numCuadruplo += 1

def p_Left(p):
	'''Left		:	TUR POINT LEFT LPAREN ExpI RPAREN SEMICOLON crea_cuadruplo_left
	'''

def p_crea_cuadruplo_left(p):
	'''crea_cuadruplo_left	: 
	'''
	operando = edjo.pilaOperandos.pop()
	cuadruplo = Cuadruplo(edjo.numCuadruplo, 'TUR_LEFT', operando, None, None)
	edjo.cuadruplos.append(cuadruplo)
	edjo.numCuadruplo += 1


def p_Circle(p):
	'''Circle	:	TUR POINT CIRCLE LPAREN ExpI RPAREN SEMICOLON crea_cuadruplo_circle
	'''

def p_crea_cuadruplo_circle(p):
	'''crea_cuadruplo_circle	: 
	'''
	operando = edjo.pilaOperandos.pop()
	cuadruplo = Cuadruplo(edjo.numCuadruplo, 'TUR_CIRCLE', operando, None, None)
	edjo.cuadruplos.append(cuadruplo)
	edjo.numCuadruplo += 1	

def p_Position(p):
	'''Position	:	TUR POINT POS LPAREN ExpI COMMA ExpI RPAREN SEMICOLON crea_cuadruplo_pos
	'''

def p_crea_cuadruplo_pos(p):
	'''crea_cuadruplo_pos	: 
	'''
	y = edjo.pilaOperandos.pop()
	x = edjo.pilaOperandos.pop()
	cuadruplo = Cuadruplo(edjo.numCuadruplo, 'TUR_POS', x, y, None)
	edjo.cuadruplos.append(cuadruplo)
	edjo.numCuadruplo += 1


def p_IniciaTurtle(p):
	'''IniciaTurtle	:	TUR POINT TURTLE LPAREN RPAREN SEMICOLON crea_cuadruplo_inicia
	'''

def p_crea_cuadruplo_inicia(p):
	'''crea_cuadruplo_inicia	: 
	'''
	cuadruplo = Cuadruplo(edjo.numCuadruplo, 'TUR_INICIA', None, None, None)
	edjo.cuadruplos.append(cuadruplo)
	edjo.numCuadruplo += 1

def p_TerminaTurtle(p):
	'''TerminaTurtle	:	TUR POINT FINISH LPAREN RPAREN SEMICOLON crea_cuadruplo_termina
	'''

def p_crea_cuadruplo_termina(p):
	'''crea_cuadruplo_termina	: 
	'''
	cuadruplo = Cuadruplo(edjo.numCuadruplo, 'TUR_TERMINA', None, None, None)
	edjo.cuadruplos.append(cuadruplo)
	edjo.numCuadruplo += 1

import ply.yacc as yacc
import pprint
parser = yacc.yacc()
pp = pprint.PrettyPrinter(indent=4)

with open('prueba.txt','r') as f:
	input = f.read()
	pp.pprint(parser.parse(input))
	edjo.dirFuncion.printDirFuncion()
	edjo.printCuadruplos()
