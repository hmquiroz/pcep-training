'''BaseException:
Es la clase base para todas las excepciones en Python. Todas las excepciones heredan de esta clase. No se recomienda capturar esta excepción directamente, ya que esto también capturaría excepciones que normalmente no se deben capturar, como KeyboardInterrupt y SystemExit.

Exception:
Es la clase base para todas las excepciones comunes en Python. Todas las excepciones definidas por el usuario deben heredar de esta clase.

SystemExit:
Esta excepción se lanza cuando se llama a la función sys.exit() para salir del programa. Normalmente, esta excepción no se captura, ya que se utiliza para indicar que el programa debe finalizar.

KeyboardInterrupt:
Esta excepción se lanza cuando se presiona la combinación de teclas Ctrl+C en la consola. Normalmente, esta excepción no se captura, ya que se utiliza para interrumpir la ejecución del programa.

Excepciones abstractas:
Son excepciones que se utilizan para representar situaciones excepcionales en lugar de errores específicos. Algunas de estas excepciones incluyen StopIteration, GeneratorExit y SystemError.

ArithmeticError:
Es la clase base para todas las excepciones de errores aritméticos. Algunas excepciones que heredan de esta clase incluyen ZeroDivisionError y OverflowError.

LookupError:
Es la clase base para todas las excepciones de errores de búsqueda. Algunas excepciones que heredan de esta clase incluyen IndexError y KeyError.
'''

'''IndexError:
Esta excepción se lanza cuando se intenta acceder a un índice de una secuencia que está fuera de los límites.
'''
lista = [1, 2, 3]
print(lista[2])  # Lanza IndexError: list index out of range

'''KeyError:
Esta excepción se lanza cuando se intenta acceder a una clave que no existe en un diccionario.'''
diccionario = {"a": 1, "b": 2, "c": 3}
print(diccionario["d"])  # Lanza KeyError: 'd'

'''TypeError:
Esta excepción se lanza cuando se intenta realizar una operación no válida en un tipo de datos.'''
print("3" + 4)  # Lanza TypeError: can only concatenate str (not "int") to str

'''ValueError:
Esta excepción se lanza cuando se intenta realizar una operación con un valor que no es válido para ese tipo de datos.'''
int("hola")  # Lanza ValueError: invalid literal for int() with base 10: 'hola'
