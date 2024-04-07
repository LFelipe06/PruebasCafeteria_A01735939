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
    
    
    return "Valid beverage"