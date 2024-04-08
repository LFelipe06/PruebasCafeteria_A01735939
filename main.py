# Pruebas Sistema de Gestión de Cafetería
# Luis Felipe Hernández Flores, A01735939

def new_beverage(name, sizes):
    # Se valida que la variable correspondiente al nombre de la bebida sea  sea mayor o 
    # igual a 2 y menor o igual a 15 caracteres
    
    # Se valida que todos los caracteres del string sean alfabéticos. 
    
    # Particularmente, todos los elementos como espacios y puntuación no son considerados 
    # elementos alfabéticos, siendo que usando isalpha() se validan dos critérios: a) que 
    # sean elementos alfabéticos y b) (redundantemente) que no haya espacios en el input
    
    # El usar el operador "if not" nos permite validar el criterio pero además permitir 
    # la ejecución de las demás comprobaciones, siendo que en caso de no cumplir con la 
    # comprobación lógica, el programa concluirá retornando "Invalid beverage" para cada 
    # una de estas comprobaciones
    if not ((len(name) >= 2) & (len(name) <= 15) & name.isalpha()):
        return "Invalid beverage"
    
    # Se valida que el número de elementos en el input correspondiente a la lista de tamaños
    # tenga un total de elementos mayor o igual que 1 y menor o igual que 5. 

    # Usando la función isinstance() se corrobora que todos los elementos de la lista sean
    # números enteros mayores o iguales a 1 y menores o iguales a 48
    
    if not (len(sizes) >= 1) & (len(sizes) <= 5) & all(isinstance(x, int) and 1 <= x <= 48 for x in sizes):
        return "Invalid beverage"
    
    # Se valida que los elementos de la lista de tamaños haya sigo ingresada con sus elementos
    # en orden ascendente comparando la variables en la que fueron almacenados y la variable
    # temporal que genera la función sorted(), tomando como atributo la misma lista de tamaños.
    # El verificar la igualdad de estas dos variables nos permite verificar que la lista ingresada
    # esté ordenada en orden ascendente.
    if not (sizes == sorted(sizes)):
        return "Invalid beverage"

    # Finalmente, si el programa aún no ha concluido y retornado "Invalid beverage" en alguna de las
    # comprobaciones lógicas, se retorna "Valid beverage" siendo que cumple con los requerimientos
    # establecidos.
    return "Valid beverage"
