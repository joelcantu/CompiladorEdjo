from dirFuncion import DirFuncion
from memoria import Memoria
from ast import literal_eval
import turtle
import sys

class MaquinaVirtual():

    print("entro")

    def __init__(self, memoria, dirFunciones, instructions):
        self.memoria = memoria
        self.dirFunciones = dirFunciones
        self.instructions =instructions
        self.cantInstrucciones = len(self.instructions)
        self.cantInstruccionesActuales = 0
        self.parametroActual = 0 # Es EL parametro de la funcion (guarda si es el primero, segundo o tercer parametro)
        self.turtleActual = turtle.Turtle()

    def MemoriaLocal(self, funcionLlamada):
        for i in range (funcionLlamada['funcion']['LocalVariables']['int']):
            funcionLlamada['memoria'].MemoriaLocal('int')
        for i in range (funcionLlamada['funcion']['LocalVariables']['decimal']):
            funcionLlamada['memoria'].MemoriaLocal('decimal')
        for i in range (funcionLlamada['funcion']['LocalVariables']['string']):
            funcionLlamada['memoria'].MemoriaLocal('string')
        for i in range (funcionLlamada['funcion']['LocalVariables']['bool']):
            funcionLlamada['memoria'].MemoriaLocal('bool')

    def MemoriaTemporal(self, funcionLlamada):
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

        # Imprime de nuevo los cuadruplos
        print("Quadruplos de VM")
        a = self.cantInstruccionesActuales
        b = self.cantInstrucciones

        #print(a)
        #print(b)
 
        # Ciclo para generacion de cuadruplos e imprimir
        while self.cantInstruccionesActuales < self.cantInstrucciones:
            instruccionActual = self.instructions[self.cantInstruccionesActuales]

            if print_step_by_step == 'Y':
                print(instruccionActual)

            instruccionDiccionario = instruccionActual.operador # InstruccionDiccionario contiene la "instruccion" del cuadruplo (Ej. '+', 'GOTO', etc)
            dirOperandoIzquierdo = instruccionActual.operandoIzq
            dirOperandoDerecho = instruccionActual.operandoDer
            dirResultado = instruccionActual.resultado # Direccion donde el resultado es guardado



            if isinstance(dirOperandoIzquierdo, dict):
                dirOperandoIzquierdo = memoriaActual.Valor(
                    dirOperandoIzquierdo['index_address'])

            if isinstance(dirOperandoDerecho, dict):
                dirOperandoDerecho = memoriaActual.Valor(
                    dirOperandoDerecho['index_address'])

            if isinstance(dirResultado, dict):
                dirResultado = memoriaActual.Valor(
                    dirResultado['index_address'])


            #AQUIIIII EMPIEZAAA MI MADAFUCKIN SWITCH
            def SUMA():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    operandoDerecho = memoriaActual.Valor(dirOperandoDerecho)
                    resultado = operandoIzquierdo + operandoDerecho
                    memoriaActual.ModificaValor(dirResultado, resultado)
                    self.cantInstruccionesActuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion

            def RESTA():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    operandoDerecho = memoriaActual.Valor(dirOperandoDerecho)
                    resultado = operandoIzquierdo - operandoDerecho
                    memoriaActual.ModificaValor(dirResultado, resultado)
                    self.cantInstruccionesActuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion

            def MULTIPLICACION():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    operandoDerecho = memoriaActual.Valor(dirOperandoDerecho)
                    resultado = operandoIzquierdo * operandoDerecho
                    memoriaActual.ModificaValor(dirResultado, resultado)
                    self.cantInstruccionesActuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion

            def DIVISION():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    operandoDerecho = memoriaActual.Valor(dirOperandoDerecho)

                    # Valida que no se ejecute una division por 0
                    if operandoDerecho == 0:
                        print("ERROR! Division por 0 no es valido")
                        sys.exit()
                    else:
                        if isinstance(operandoIzquierdo, float) or isinstance(operandoDerecho, float):
                            resultado = operandoIzquierdo / operandoDerecho
                        else:
                            resultado = int(operandoIzquierdo / operandoDerecho)

                        memoriaActual.ModificaValor(dirResultado, resultado)
                        self.cantInstruccionesActuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion

            def IGUAL():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    resultado = operandoIzquierdo
                    memoriaActual.ModificaValor(dirResultado, resultado)
                    self.cantInstruccionesActuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion

            def IMPRIME():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    print(str(operandoIzquierdo))
                    self.cantInstruccionesActuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion

            def GOTO():
                    self.cantInstruccionesActuales = dirResultado - 1

            def GOTOF():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)

                    if not operandoIzquierdo:
                        self.cantInstruccionesActuales = dirResultado - 1
                    else:
                        self.cantInstruccionesActuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion

            def GOTOV():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)

                    if not operandoIzquierdo:
                        self.cantInstruccionesActuales += 1
                    else:
                        self.cantInstruccionesActuales = dirResultado - 1


            def RETURN():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    resultado = operandoIzquierdo
                    memoriaActual.ModificaValor(dirResultado, resultado)
                    self.cantInstruccionesActuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion


            #NOOOO FUNCIONAA ERAAAAAAA 
            def ERA():
                    # Crea un espacio en memoria donde guarda las variables locales y temporales de la funcion llamada
                    funcionLlamada['funcion'] = self.dirFunciones.RegresaFuncion(dirOperandoIzquierdo)
                    funcionLlamada['memoria'] = Memoria()
                    self.parametroActual = 0
                    self.MemoriaLocal(funcionLlamada)
                    self.MemoriaTemporal(funcionLlamada)
                    self.cantInstruccionesActuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion

            def IGUALIGUAL():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    operandoDerecho = memoriaActual.Valor(dirOperandoDerecho)
                    resultado = operandoIzquierdo == operandoDerecho
                    memoriaActual.ModificaValor(dirResultado, resultado)
                    self.cantInstruccionesActuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion

            def MENORQUE():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    operandoDerecho = memoriaActual.Valor(dirOperandoDerecho)
                    resultado = operandoIzquierdo < operandoDerecho
                    memoriaActual.ModificaValor(dirResultado, resultado)
                    self.cantInstruccionesActuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion

            def MAYORQUE():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    operandoDerecho = memoriaActual.Valor(dirOperandoDerecho)
                    resultado = operandoIzquierdo > operandoDerecho
                    memoriaActual.ModificaValor(dirResultado, resultado)
                    self.cantInstruccionesActuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion

            def MENORIGUAL():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    operandoDerecho = memoriaActual.Valor(dirOperandoDerecho)
                    resultado = operandoIzquierdo <= operandoDerecho
                    memoriaActual.ModificaValor(dirResultado, resultado)
                    self.cantInstruccionesActuales += 1

            def MAYORIGUAL():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    operandoDerecho = memoriaActual.Valor(dirOperandoDerecho)
                    resultado = operandoIzquierdo >= operandoDerecho
                    memoriaActual.ModificaValor(dirResultado, resultado)
                    self.cantInstruccionesActuales += 1

            def DIFERENTE():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    operandoDerecho = memoriaActual.Valor(dirOperandoDerecho)
                    resultado = operandoIzquierdo != operandoDerecho
                    memoriaActual.ModificaValor(dirResultado, resultado)
                    self.cantInstruccionesActuales += 1

            def PARAMETRO():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    direccionParametro = funcionLlamada['funcion']['Parameters']['Addresses'][self.parametroActual]
                    self.parametroActual += 1
                    funcionLlamada['memoria'].ModificaValor(direccionParametro, operandoIzquierdo)
                    self.cantInstruccionesActuales += 1

            def GOSUB():
                    numeroInstrucionLista.append(self.cantInstruccionesActuales)
                    apuntadorLocalLista.append(memoriaActual.memLocales)
                    apuntadorTempLista.append(memoriaActual.memTemporales)
                    memoriaActual.memLocales = funcionLlamada['memoria'].memLocales
                    memoriaActual.memTemporales = funcionLlamada['memoria'].memTemporales
                    self.cantInstruccionesActuales = dirResultado - 1

            def ENDPROC():
                    funcionLlamada.clear()
                    memoriaActual.memLocales = apuntadorLocalLista.pop()
                    memoriaActual.memTemporales = apuntadorTempLista.pop()
                    self.cantInstruccionesActuales = numeroInstrucionLista.pop() + 1

            def CREATURTLE():
                    self.turtleActual = turtle.Turtle()
                    self.cantInstruccionesActuales += 1

            def AVANZA():
                    operandoIzquierdo = int(memoriaActual.Valor(dirOperandoIzquierdo))
                    self.turtleActual.forward(operandoIzquierdo)
                    self.cantInstruccionesActuales += 1

            def TURDERECHA():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    self.turtleActual.right(90)
                    self.turtleActual.forward(operandoIzquierdo)
                    self.cantInstruccionesActuales += 1

            def TURIZQUIERDA():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    self.turtleActual.left(90)
                    self.turtleActual.forward(operandoIzquierdo)
                    self.cantInstruccionesActuales += 1

            def CIRCULO():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    self.turtleActual.circle(operandoIzquierdo)
                    self.cantInstruccionesActuales += 1

            def CUADRO():
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

            def RECTANGULO():
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

            def TRIANGULO():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    self.turtleActual.forward(operandoIzquierdo)
                    self.turtleActual.left(120)
                    self.turtleActual.forward(operandoIzquierdo)
                    self.turtleActual.left(120)
                    self.turtleActual.forward(operandoIzquierdo)
                    self.cantInstruccionesActuales += 1

            def INICIAFILL():
                    self.turtleActual.begin_fill()
                    self.cantInstruccionesActuales +=1

            def TERMINAFILL():
                    self.turtleActual.end_fill()
                    self.cantInstruccionesActuales += 1

            def TERMINATURTLE():
                    turtle.done()
                    self.cantInstruccionesActuales += 1
                    

            def FILL():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    nombreColor = operandoIzquierdo
                    print(nombreColor)
                    self.turtleActual.fillcolor(nombreColor)
                    self.cantInstruccionesActuales += 1

            def COLORPEN():
                    operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
                    nombreColor = operandoIzquierdo
                    self.turtleActual.pencolor(nombreColor)
                    self.cantInstruccionesActuales += 1
                    
            #diccionario de funciones/instrucciones
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

            }

            #llamada al switch
            ans = opciones[instruccionDiccionario]
            ans()

        

            








         