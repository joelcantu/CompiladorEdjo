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
        self.cant_instrucciones = len(self.instructions)
        self.cant_instrucciones_actuales = 0


    def execute(self, print_step_by_step):
        funcion_llamada = {} # Guarda la funcion cuando es llamada
        actual_parameter = 0 # Es EL parametro de la funcion (guarda si es el primero, segundo o tercer parametro)
        memoria_actual = self.memoria 
        local_segment_pointer_list = [] 
        temporal_segment_pointer_list = [] 
        instruction_number_to_back_list = [] # Es el numero de instruccion que regresamos despues de terminar la funcion

        # Imprime de nuevo los cuadruplos
        print("Quadruplos de VM")
        a = self.cant_instrucciones_actuales
        b = self.cant_instrucciones

        #print(a)
        #print(b)
 
        # Ciclo para generacion de cuadruplos e imprimir
        while self.cant_instrucciones_actuales < self.cant_instrucciones:
            instruccion_actual = self.instructions[self.cant_instrucciones_actuales]

            if print_step_by_step == 'Y':
                print(instruccion_actual)

            instruccion_diccionario = instruccion_actual.operador # Instruccion_diccionario contiene la "instruccion" del cuadruplo (Ej. '+', 'GOTO', etc)
            dir_operando_izquierdo = instruccion_actual.operandoIzq
            dir_operando_derecho = instruccion_actual.operandoDer
            dir_resultado = instruccion_actual.resultado # Direccion donde el resultado es guardado



            if isinstance(dir_operando_izquierdo, dict):
                dir_operando_izquierdo = memoria_actual.Valor(
                    dir_operando_izquierdo['index_address'])

            if isinstance(dir_operando_derecho, dict):
                dir_operando_derecho = memoria_actual.Valor(
                    dir_operando_derecho['index_address'])

            if isinstance(dir_resultado, dict):
                dir_resultado = memoria_actual.Valor(
                    dir_resultado['index_address'])


            #AQUIIIII EMPIEZAAA MI MADAFUCKIN SWITCH
            def SUMA():
                    operando_izquierdo = memoria_actual.Valor(dir_operando_izquierdo)
                    operando_derecho = memoria_actual.Valor(dir_operando_derecho)
                    resultado = operando_izquierdo + operando_derecho
                    memoria_actual.ModificaValor(dir_resultado, resultado)
                    self.cant_instrucciones_actuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion

            def RESTA():
                    operando_izquierdo = memoria_actual.Valor(dir_operando_izquierdo)
                    operando_derecho = memoria_actual.Valor(dir_operando_derecho)
                    resultado = operando_izquierdo - operando_derecho
                    memoria_actual.ModificaValor(dir_resultado, resultado)
                    self.cant_instrucciones_actuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion

            def MULTIPLICACION():
                    operando_izquierdo = memoria_actual.Valor(dir_operando_izquierdo)
                    operando_derecho = memoria_actual.Valor(dir_operando_derecho)
                    resultado = operando_izquierdo * operando_derecho
                    memoria_actual.ModificaValor(dir_resultado, resultado)
                    self.cant_instrucciones_actuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion

            def DIVISION():
                    operando_izquierdo = memoria_actual.Valor(dir_operando_izquierdo)
                    operando_derecho = memoria_actual.Valor(dir_operando_derecho)

                    # Valida que no se ejecute una division por 0
                    if operando_derecho == 0:
                        print("ERROR! Division por 0 no es valido")
                        sys.exit()
                    else:
                        if isinstance(operando_izquierdo, float) or isinstance(operando_derecho, float):
                            resultado = operando_izquierdo / operando_derecho
                        else:
                            resultado = int(operando_izquierdo / operando_derecho)

                        memoria_actual.ModificaValor(dir_resultado, resultado)
                        self.cant_instrucciones_actuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion

            def IGUAL():
                    operando_izquierdo = memoria_actual.Valor(dir_operando_izquierdo)
                    resultado = operando_izquierdo
                    memoria_actual.ModificaValor(dir_resultado, resultado)
                    self.cant_instrucciones_actuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion

            def IMPRIME():
                    operando_izquierdo = memoria_actual.Valor(dir_operando_izquierdo)
                    print(str(operando_izquierdo))
                    self.cant_instrucciones_actuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion

            def GOTO():
                    self.cant_instrucciones_actuales = dir_resultado - 1

            def GOTOF():
                    operando_izquierdo = memoria_actual.Valor(dir_operando_izquierdo)

                    if not operando_izquierdo:
                        self.cant_instrucciones_actuales = dir_resultado - 1
                    else:
                        self.cant_instrucciones_actuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion

            def GOTOV():
                    operando_izquierdo = memoria_actual.Valor(dir_operando_izquierdo)

                    if not operando_izquierdo:
                        self.cant_instrucciones_actuales += 1
                    else:
                        self.cant_instrucciones_actuales = dir_resultado - 1


            def RETURN():
                    operando_izquierdo = memoria_actual.Valor(dir_operando_izquierdo)
                    resultado = operando_izquierdo
                    memoria_actual.ModificaValor(dir_resultado, resultado)
                    self.cant_instrucciones_actuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion


            #NOOOO FUNCIONAA ERAAAAAAA 
            def ERA():
                    # Crea un espacio en memoria donde guarda las variables locales y temporales de la funcion llamada
                    funcion_llamada['function'] = self.dirFunciones.get_function(dir_operando_izquierdo)
                    funcion_llamada['memoria'] = Memoria()
                    actual_parameter = 0

                    # Asigna la cantidad de variables locales y globales de la funcion
                    self.request_local_addresses(funcion_llamada)
                    self.request_temporal_addresses(funcion_llamada)
                    self.cant_instrucciones_actuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion

            def IGUALIGUAL():
                    operando_izquierdo = memoria_actual.Valor(dir_operando_izquierdo)
                    operando_derecho = memoria_actual.Valor(dir_operando_derecho)
                    resultado = operando_izquierdo == operando_derecho
                    memoria_actual.ModificaValor(dir_resultado, resultado)
                    self.cant_instrucciones_actuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion

            def MENORQUE():
                    operando_izquierdo = memoria_actual.Valor(dir_operando_izquierdo)
                    operando_derecho = memoria_actual.Valor(dir_operando_derecho)
                    resultado = operando_izquierdo < operando_derecho
                    memoria_actual.ModificaValor(dir_resultado, resultado)
                    self.cant_instrucciones_actuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion

            def MAYORQUE():
                    operando_izquierdo = memoria_actual.Valor(dir_operando_izquierdo)
                    operando_derecho = memoria_actual.Valor(dir_operando_derecho)
                    resultado = operando_izquierdo > operando_derecho
                    memoria_actual.ModificaValor(dir_resultado, resultado)
                    self.cant_instrucciones_actuales += 1 #incrementa el contador deinstructions para continuar con la siguiente intruccion

            def MENORIGUAL():
                    operando_izquierdo = memoria_actual.Valor(dir_operando_izquierdo)
                    operando_derecho = memoria_actual.Valor(dir_operando_derecho)
                    resultado = operando_izquierdo <= operando_derecho
                    memoria_actual.ModificaValor(dir_resultado, resultado)
                    self.cant_instrucciones_actuales += 1

            def MAYORIGUAL():
                    operando_izquierdo = memoria_actual.Valor(dir_operando_izquierdo)
                    operando_derecho = memoria_actual.Valor(dir_operando_derecho)
                    resultado = operando_izquierdo >= operando_derecho
                    memoria_actual.ModificaValor(dir_resultado, resultado)
                    self.cant_instrucciones_actuales += 1

            def DIFERENTE():
                    operando_izquierdo = memoria_actual.Valor(dir_operando_izquierdo)
                    operando_derecho = memoria_actual.Valor(dir_operando_derecho)
                    resultado = operando_izquierdo != operando_derecho
                    memoria_actual.ModificaValor(dir_resultado, resultado)
                    self.cant_instrucciones_actuales += 1

          #  def PARAMETRO():

          #          operando_izquierdo = memoria_actual.Valor(dir_operando_izquierdo)
          #          direccionParametro = 

#                    left_operand = current_memory.Valor(left_operand_address)
 #                   parameter_adress = funcion_llamada['function']['parameters']['addresses'][actual_parameter]
  #                  actual_parameter += 1

                    # Stores the value of the parameter in its corresponding function
                    # segment menory
   #                 funcion_llamada['memory'].ModificaValor(parameter_adress, left_operand)

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
            ans = opciones[instruccion_diccionario]
            ans()

        

            








         