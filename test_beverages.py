# Set de tests para la función new_beverage(). Debe cumplir con los siguientes cirterios:
# - Nombre debe de ser alfebético
# - Nombre debe de tener de 2 a 15 caracteres de longitud
# - Los elementos de la lista de tamaños debe de ser entero
# - Los elementos de la lista de tamaños está dentro del rango de 1 a 14
# - Los elementos de la lista de tamaños deben de ser ingresados en orden ascendente
# - La lista de tamaños debe de contener de 1 a 5 elementos
# - Un valor tipo string (nombre) es el primero en la entrada
# - Una sola coma separa los elementos de la lista de tamaños
# - La entrada no contiene espacios en blanco 

from main import new_beverage

def test_beverage_1():
    assert new_beverage("Tea", [12, 24, 36]) == "Valid beverage"

def test_beverage_2():
    assert new_beverage("Tea4two", [12, 24, 36]) == "Valid beverage"

def test_beverage_3():
    assert new_beverage("E", [12, 24, 36]) == "Valid beverage"

def test_beverage_4():
    assert new_beverage("EspressoEspressoEspressoEspressoEspressoEspresso", [12, 24, 36]) == "Valid beverage"


