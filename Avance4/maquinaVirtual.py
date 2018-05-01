from dirFuncion import DirFuncion
from memoria import Memoria
from ast import literal_eval
import turtle
import sys

class MaquinaVirtual():

    def __init__(self, memoria, dirFunciones, instructions):
        self.memoria = memoria # Memoria
        self.dirFunciones = dirFunciones #Directorio de funciones
        self.instructions =instructions #Instruccion siguiente
        self.cantInstrucciones = len(self.instructions) #Cantidad de instrucciones
        self.cantInstruccionesActuales = 0  #Inicializa contador
        self.parametroActual = 0 # Es EL parametro de la funcion (guarda si es el primero, segundo o tercer parametro)
        self.turtle = False
        if(turtle): # If que la ventana de python turtle graphics no abra siempre, que solo se abra cuando se haya creado una tortuga
            self.turtleActual = turtle.Turtle() #Inicializacion de Turtle

    def recibeTipoInput(self, value): # Recibe el tipo de variable del input (int, string, decimal etc)
        try:
            return type(literal_eval(value))
        except (ValueError, SyntaxError):
            return str

    def ModificaTipoInput(self, value): # Modifica el tipo de variable
        if self.recibeTipoInput(value) is int:
            return int(value)
        elif self.recibeTipoInput(value) is float:
            return float(value)
        elif self.recibeTipoInput(value) is str:
            return str(value)
        elif self.recibeTipoInput(value) is bool:
            return bool(value)

    def TipoInput(self, value): # Determina el tipo del valor (si es int, decimal, string etc)
        if self.recibeTipoInput(value) is int:
            return 'int'
        elif self.recibeTipoInput(value) is float:
            return 'decimal'
        elif self.recibeTipoInput(value) is str:
            return 'string'
        elif self.recibeTipoInput(value) is bool:
            return 'bool'

    def MemoriaLocal(self, funcionLlamada): #Regresa la cantidad de variables locales en la funcion por tipo
        for i in range (funcionLlamada['funcion']['LocalVariables']['int']):
            funcionLlamada['memoria'].MemoriaLocal('int')
        for i in range (funcionLlamada['funcion']['LocalVariables']['decimal']):
            funcionLlamada['memoria'].MemoriaLocal('decimal')
        for i in range (funcionLlamada['funcion']['LocalVariables']['string']):
            funcionLlamada['memoria'].MemoriaLocal('string')
        for i in range (funcionLlamada['funcion']['LocalVariables']['bool']):
            funcionLlamada['memoria'].MemoriaLocal('bool')

    def MemoriaTemporal(self, funcionLlamada): #regresa la cantidad de variables temporales en la funcion por tipo
        for i in range (funcionLlamada['funcion']['TemporalVariables']['int']):
            funcionLlamada['memoria'].MemoriaTemporal('int')
        for i in range (funcionLlamada['funcion']['TemporalVariables']['decimal']):
            funcionLlamada['memoria'].MemoriaTemporal('decimal')
        for i in range (funcionLlamada['funcion']['TemporalVariables']['string']):
            funcionLlamada['memoria'].MemoriaTemporal('string')
        for i in range (funcionLlamada['funcion']['TemporalVariables']['bool']):
            funcionLlamada['memoria'].MemoriaTemporal('bool')


    def execute(self, print_step_by_step):
        funcionLlamada = {} # Guarda la funcion cuando es llamada
        memoriaActual = self.memoria 
        apuntadorLocalLista = []
        apuntadorTempLista = []
        numeroInstrucionLista = []

        a = self.cantInstruccionesActuales
        b = self.cantInstrucciones

        #print(a)
        #print(b)
 
        # Ciclo para generacion de cuadruplos e imprimir
        while self.cantInstruccionesActuales < self.cantInstrucciones:
            instruccionActual = self.instructions[self.cantInstruccionesActuales]

            if print_step_by_step == 'Y':
                #Imprime de nuevo los cuadruplos
                print("Quadruplos de VM")
                print(instruccionActual)

            instruccionDiccionario = instruccionActual.operador # InstruccionDiccionario contiene la "instruccion" del cuadruplo (Ej. '+', 'GOTO', etc)
            dirOperandoIzquierdo = instruccionActual.operandoIzq # Direccion del operando izquierdo de la instruccion actual
            dirOperandoDerecho = instruccionActual.operandoDer # Direccion del operando derecho de la instruccion actual
            dirResultado = instruccionActual.resultado # Direccion donde el resultado es guardado

            # Recibe el valor de la direccion que esta guardado en memoria para el operando izquierdo
            if isinstance(dirOperandoIzquierdo, dict): 
                dirOperandoIzquierdo = memoriaActual.Valor(
                    dirOperandoIzquierdo['Direccion'])
            # Recibe el valor de la direccion que esta guardado en memoria para el operando derecho
            if isinstance(dirOperandoDerecho, dict):
                dirOperandoDerecho = memoriaActual.Valor(
                    dirOperandoDerecho['Direccion'])
            # Recibe el valor de la direccion que esta guardado en memoria para la direccion que contiene el resultado
            if isinstance(dirResultado, dict):
                dirResultado = memoriaActual.Valor(
                    dirResultado['Direccion'])


            #AQUIIIII EMPIEZAAA MI MADAFUCKIN SWITCH
            def SUMA():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo) #Mete el valor guardado en memoria al operando izquierdo
                    operandoDerecho = memoriaActual.Valor(dirOperandoDerecho) # Mete el valor guardado en memoria al operando derecho 
                    resultado = operandoIzquierdo + operandoDerecho # Guarda el valor resultado de la suma del operando izquiero y derecho
                    memoriaActual.ModificaValor(dirResultado, resultado) # Modifica el valor en memoria con su direccion
                    self.cantInstruccionesActuales += 1 # Incrementa el contador de instructions

            def RESTA():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo) #Mete el valor guardado en memoria al operando izquierdo
                    operandoDerecho = memoriaActual.Valor(dirOperandoDerecho) # Mete el valor guardado en memoria al operando derecho
                    resultado = operandoIzquierdo - operandoDerecho # Guarda el valor resultado del operando izquiero menos el operando derecho
                    memoriaActual.ModificaValor(dirResultado, resultado) # Modifica el valor en memoria con su direccion
                    self.cantInstruccionesActuales += 1 # Incrementa el contador de instructions

            def MULTIPLICACION():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo) #Mete el valor guardado en memoria al operando izquierdo
                    operandoDerecho = memoriaActual.Valor(dirOperandoDerecho) # Mete el valor guardado en memoria al operando derecho
                    resultado = operandoIzquierdo * operandoDerecho # Guarda el valor resultado del operando izquiero por el operando derecho
                    memoriaActual.ModificaValor(dirResultado, resultado) # Modifica el valor en memoria con su direccion
                    self.cantInstruccionesActuales += 1 # Incrementa el contador de instructions

            def DIVISION():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo) #Mete el valor guardado en memoria al operando izquierdo
                    operandoDerecho = memoriaActual.Valor(dirOperandoDerecho) # Mete el valor guardado en memoria al operando derecho

                    # Valida que no se haga una division por 0
                    if operandoDerecho == 0:
                        print("ERROR! Division por 0 no es valido")
                        sys.exit() # Termina el programa
                    else:
                        if isinstance(operandoIzquierdo, float) or isinstance(operandoDerecho, float): #Revisa que los valores sean flotantes
                            resultado = operandoIzquierdo / operandoDerecho # Guarda el valor resultado del operando izquiero entre el operando derecho
                        else:
                            resultado = int(operandoIzquierdo / operandoDerecho) # Guarda el valor resultado del operando izquiero entre el operando derecho

                        memoriaActual.ModificaValor(dirResultado, resultado) # Modifica el valor en memoria con su direccion
                        self.cantInstruccionesActuales += 1 # Incrementa el contador de instructions 

            def IGUAL():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo) #Mete el valor guardado en memoria en la direccion del operando izquierdo al operando izquierdo
                    resultado = operandoIzquierdo # Guarda el valor en resultado
                    memoriaActual.ModificaValor(dirResultado, resultado) # Modifica el valor en memoria con su direccion
                    self.cantInstruccionesActuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion

            def IMPRIME():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo) #Mete el valor guardado en memoria al operando izquierdo
                    print(str(operandoIzquierdo)) #Print del valor
                    self.cantInstruccionesActuales += 1 #Incrementa el contador de instructions

            def GOTO():
                    self.cantInstruccionesActuales = dirResultado - 1 # Actualiza el numero de instruccion con respecto a la nueva linea que debe irse

            def GOTOF():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo) #Mete el valor guardado en memoria al operando izquierdo
                    if not operandoIzquierdo: # Si es Falso 
                        self.cantInstruccionesActuales = dirResultado - 1 # Actualiza el numero de instruccion con respecto a la nueva linea que debe irse
                    else:
                        self.cantInstruccionesActuales += 1 #Incrementa el contador de instructions

            def GOTOV():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo) #Mete el valor guardado en memoria al operando izquierdo

                    if not operandoIzquierdo: # Si es Falso
                        self.cantInstruccionesActuales += 1 #Incrementa el contador de instructions
                    else:
                        self.cantInstruccionesActuales = dirResultado - 1 #Actualiza el numero de instruccion con respecto a la nueva linea que debe irse


            def RETURN(): #Resuelve la operacion del return y modifica el contador de instrucciones pendientes
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    resultado = operandoIzquierdo
                    memoriaActual.ModificaValor(dirResultado, resultado)
                    self.cantInstruccionesActuales += 1 

            def ERA():
                    # Crea un espacio en memoria donde guarda las variables locales y temporales de la funcion llamada
                    funcionLlamada['funcion'] = self.dirFunciones.RegresaFuncion(dirOperandoIzquierdo)
                    funcionLlamada['memoria'] = Memoria()
                    self.parametroActual = 0
                    self.MemoriaLocal(funcionLlamada)
                    self.MemoriaTemporal(funcionLlamada)
                    self.cantInstruccionesActuales += 1 

            def IGUALIGUAL(): #Regresa True o False al resolver el operador ==
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    operandoDerecho = memoriaActual.Valor(dirOperandoDerecho)
                    resultado = operandoIzquierdo == operandoDerecho
                    memoriaActual.ModificaValor(dirResultado, resultado)
                    self.cantInstruccionesActuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion

            def MENORQUE(): #Regresa True o False al resolver el operador > 
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    operandoDerecho = memoriaActual.Valor(dirOperandoDerecho)
                    resultado = operandoIzquierdo < operandoDerecho
                    memoriaActual.ModificaValor(dirResultado, resultado)
                    self.cantInstruccionesActuales += 1 

            def MAYORQUE(): #Regresa True o False al resolver el operador <
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    operandoDerecho = memoriaActual.Valor(dirOperandoDerecho)
                    resultado = operandoIzquierdo > operandoDerecho
                    memoriaActual.ModificaValor(dirResultado, resultado)
                    self.cantInstruccionesActuales += 1 

            def MENORIGUAL(): #Regresa True o False al resolver el operador <=
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    operandoDerecho = memoriaActual.Valor(dirOperandoDerecho)
                    resultado = operandoIzquierdo <= operandoDerecho
                    memoriaActual.ModificaValor(dirResultado, resultado)
                    self.cantInstruccionesActuales += 1

            def MAYORIGUAL(): #Regresa True o False al resolver el operador >=
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    operandoDerecho = memoriaActual.Valor(dirOperandoDerecho)
                    resultado = operandoIzquierdo >= operandoDerecho
                    memoriaActual.ModificaValor(dirResultado, resultado)
                    self.cantInstruccionesActuales += 1

            def DIFERENTE(): #Regresa True o False al resolver el operador !=
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    operandoDerecho = memoriaActual.Valor(dirOperandoDerecho)
                    resultado = operandoIzquierdo != operandoDerecho
                    memoriaActual.ModificaValor(dirResultado, resultado)
                    self.cantInstruccionesActuales += 1

            def ARREGLO(): #Resuelve arreglos, recibe el indice, limite inferior y superior y revisa si el indice esta dentro de los limites.
                    indice = memoriaActual.Valor(dirOperandoIzquierdo)
                    limInf = dirOperandoDerecho
                    limSup = dirResultado

                    if indice >= limInf and indice < limSup:
                        self.cantInstruccionesActuales += 1
                    else:
                        print("Index out of range")
                        sys.exit()

            def PARAMETRO(): # Recibe el valor del parametro y la direccion en la que esta
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    direccionParametro = funcionLlamada['funcion']['Parameters']['Addresses'][self.parametroActual]
                    self.parametroActual += 1
                    funcionLlamada['memoria'].ModificaValor(direccionParametro, operandoIzquierdo)
                    self.cantInstruccionesActuales += 1

            def GOSUB(): # Guarda el numero de instruccion al cual se debe regresar despues
                    numeroInstrucionLista.append(self.cantInstruccionesActuales)
                    apuntadorLocalLista.append(memoriaActual.memLocales)
                    apuntadorTempLista.append(memoriaActual.memTemporales)
                    memoriaActual.memLocales = funcionLlamada['memoria'].memLocales
                    memoriaActual.memTemporales = funcionLlamada['memoria'].memTemporales
                    self.cantInstruccionesActuales = dirResultado - 1

            def ENDPROC(): #Hace un clear de la tabla de variables 
                    funcionLlamada.clear()
                    memoriaActual.memLocales = apuntadorLocalLista.pop()
                    memoriaActual.memTemporales = apuntadorTempLista.pop()
                    self.cantInstruccionesActuales = numeroInstrucionLista.pop() + 1

            def CREATURTLE(): #Inicializa el objeto Turtle
                    self.turtle = True
                    self.turtleActual = turtle.Turtle()
                    self.cantInstruccionesActuales += 1

            def AVANZA(): # Recibe la distancia que se movera y mueve la tortuga
                    operandoIzquierdo = int(memoriaActual.Valor(dirOperandoIzquierdo))
                    self.turtleActual.forward(operandoIzquierdo)
                    self.cantInstruccionesActuales += 1

            def TURDERECHA(): #Recibe los grados en el cual la tortuga girará hacia la derecha y la gira
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    self.turtleActual.right(90)
                    self.turtleActual.forward(operandoIzquierdo)
                    self.cantInstruccionesActuales += 1

            def TURIZQUIERDA(): #Recibe los grados en el cual la tortuga girará hacia la izquierda y la gira
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    self.turtleActual.left(90)
                    self.turtleActual.forward(operandoIzquierdo)
                    self.cantInstruccionesActuales += 1

            def CIRCULO(): #Recibe el radio del circulo a crear, y crea un ciruclo
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    self.turtleActual.circle(operandoIzquierdo)
                    self.cantInstruccionesActuales += 1

            def CUADRO(): # Recibe el tamaño del lado del cuadrado y crea un cuadro
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    self.turtleActual.forward(operandoIzquierdo)
                    self.turtleActual.left(90)
                    self.turtleActual.forward(operandoIzquierdo)
                    self.turtleActual.left(90)
                    self.turtleActual.forward(operandoIzquierdo)
                    self.turtleActual.left(90)
                    self.turtleActual.forward(operandoIzquierdo)
                    self.turtleActual.left(90)
                    self.cantInstruccionesActuales += 1

            def RECTANGULO(): # Recibe la altura y anchura del rectangulo y lo dibuja
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    operandoDerecho = memoriaActual.Valor(dirOperandoDerecho)
                    self.turtleActual.forward(operandoIzquierdo)
                    self.turtleActual.left(90)
                    self.turtleActual.forward(operandoDerecho)
                    self.turtleActual.left(90)
                    self.turtleActual.forward(operandoIzquierdo)
                    self.turtleActual.left(90)
                    self.turtleActual.forward(operandoDerecho)
                    self.turtleActual.left(90)
                    self.cantInstruccionesActuales += 1

            def TRIANGULO(): # Recibe el tamaño del triangulo EQUILATERO y lo dibuja
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    self.turtleActual.forward(operandoIzquierdo)
                    self.turtleActual.left(120)
                    self.turtleActual.forward(operandoIzquierdo)
                    self.turtleActual.left(120)
                    self.turtleActual.forward(operandoIzquierdo)
                    self.cantInstruccionesActuales += 1

            def INICIAFILL(): #Inicializa el fill
                    self.turtleActual.begin_fill()
                    self.cantInstruccionesActuales +=1

            def TERMINAFILL(): #Termina el fill
                    self.turtleActual.end_fill()
                    self.cantInstruccionesActuales += 1

            def TERMINATURTLE(): #Termina la tortuga
                    turtle.done()
                    self.cantInstruccionesActuales += 1
                    

            def FILL(): #Recibe el color del rellenado y rellena la figura con este color
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    nombreColor = operandoIzquierdo
                    self.turtleActual.fillcolor(nombreColor)
                    self.cantInstruccionesActuales += 1

            def COLORPEN(): # Recibe el color de la pluma y dibuja con este color
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    nombreColor = operandoIzquierdo
                    self.turtleActual.pencolor(nombreColor)
                    self.cantInstruccionesActuales += 1

            def INPUT(): # Recibe una expresion a guardar en una variable
                    tipoVariable = dirOperandoIzquierdo
                    mensaje = memoriaActual.Valor(dirOperandoDerecho)
                    valorInput = input(str(mensaje) + "\n")
                    TipoValorInput = self.TipoInput(valorInput)
                    valorInput = self.ModificaTipoInput(valorInput)
                    if TipoValorInput == tipoVariable:
                        memoriaActual.ModificaValor(dirResultado, valorInput)
                    else:
                        sys.exit()

                    self.cantInstruccionesActuales += 1

                    
            #Diccionario de funciones/instrucciones
            opciones = {
                        '+': SUMA,
                        '-' : RESTA,
                        '*' : MULTIPLICACION,
                        '/' : DIVISION,
                        '=' : IGUAL,
                        'PRINT' : IMPRIME,
                        'GOTO' : GOTO,
                        'GOTOF' : GOTOF,
                        'GOTOV' : GOTOV,
                        'RETURN' : RETURN,
                        'ERA' : ERA,
                        '==' : IGUALIGUAL,
                        '<' : MENORQUE,
                        '>' : MAYORQUE,
                        '<=' : MENORIGUAL,
                        '>=' : MAYORIGUAL,
                        '!=' : DIFERENTE,
                        'VER' : ARREGLO,
                        'PARAMETER' : PARAMETRO,
                        'GOSUB' : GOSUB,
                        'ENDPROC' : ENDPROC,
                        'TUR_INICIA' : CREATURTLE,
                        'TUR_TERMINA' : TERMINATURTLE,
                        'TUR_FORWARD' : AVANZA,
                        'TUR_RIGHT' : TURDERECHA,
                        'TUR_LEFT' : TURIZQUIERDA,
                        'TUR_CIRCLE' : CIRCULO,
                        'TUR_SQUARE' : CUADRO,
                        'TUR_RECTANGLE' : RECTANGULO,
                        'TUR_TRIANGLE' : TRIANGULO,
                        'TUR_INICIAFILL' : INICIAFILL,
                        'TERMINAFILL' : TERMINAFILL,
                        'TUR_FILL' : FILL,
                        'TUR_COLORPEN' : COLORPEN,
                        'INICIAFILL'   : INICIAFILL,
                        'INPUT'     : INPUT,

            }

            #Llamada al switch
            ans = opciones[instruccionDiccionario]
            ans()

        

            








         
