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


    def execute(self, print_step_by_step):
        funcionLlamada = {} # Guarda la funcion cuando es llamada
        parametroActual = 0 # Es EL parametro de la funcion (guarda si es el primero, segundo o tercer parametro)
        memoriaActual = self.memoria 

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
                    funcionLlamada['function'] = self.dirFunciones.get_function(dirOperandoIzquierdo)
                    funcionLlamada['memoria'] = Memoria()
                    parametroActual = 0

                    # Asigna la cantidad de variables locales y globales de la funcion
                    self.request_local_addresses(funcionLlamada)
                    self.request_temporal_addresses(funcionLlamada)
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

          #  def PARAMETRO():

          #          operandoIzquierdo = memoriaActual.Valor(dirOperandoIzquierdo)
          #          direccionParametro = 

#                    left_operand = current_memory.Valor(left_operand_address)
 #                   parameter_adress = funcionLlamada['function']['parameters']['addresses'][parametroActual]
  #                  parametroActual += 1

                    # Stores the value of the parameter in its corresponding function
                    # segment menory
   #                 funcionLlamada['memory'].ModificaValor(parameter_adress, left_operand)

                    # Pass to the next quadruple
    #                self.number_of_current_instruction += 1

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
           #             'PARAMETER' : PARAMETER,
           #             'GOSUB' : GOSUB,
            }

            #llamada al switch
            ans = opciones[instruccionDiccionario]
            ans()

        

            








         