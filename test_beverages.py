# Set de tests para la función new_beverage(). Debe cumplir con los siguientes cirterios:
# - Nombre debe de ser alfebético
# - Nombre debe de tener de 2 a 15 caracteres de longitud
# - Los elementos de la lista de tamaños debe de ser entero
# - Los elementos de la lista de tamaños está dentro del rango de 1 a 48
# - Los elementos de la lista de tamaños deben de ser ingresados en orden ascendente
# - La lista de tamaños debe de contener de 1 a 5 elementos
# - Un valor tipo string (nombre) es el primero en la entrada
# - Una sola coma separa los elementos de la lista de tamaños
# - La entrada no contiene espacios en blanco 

from main import new_beverage

# Nombre alfabético
def test_beverage_1():
    assert new_beverage("Tea",[12,24,36]) == "Valid beverage"

def test_beverage_2():
    assert new_beverage("Tea4two",[12,24,36]) == "Valid beverage"

# Longitud del nombre
def test_beverage_3():
    assert new_beverage("Espresso",[12,24,36]) == "Valid beverage"

def test_beverage_4():
    assert new_beverage("E",[12,24,36]) == "Valid beverage"

def test_beverage_5():
    assert new_beverage("EspressoEspressoEspressoEspressoEspressoEspresso", [12, 24, 36]) == "Valid beverage"

# Elementos de la lista de tamaños enteros
def test_beverage_6():
    assert new_beverage("Latte",[12,24,36]) == "Valid beverage"
    
def test_beverage_7():
    assert new_beverage("Latte",[12,'venti']) == "Valid beverage"

# Elementos de la lista de tamaños entre 1 y 48
def test_beverage_8():
    assert new_beverage("Frapuccino",[12,24,36]) == "Valid beverage"
    
def test_beverage_9():
    assert new_beverage("Frapuccino",[0,49,50]) == "Valid beverage"

# Elementos de la lista de tamaños en orden ascendente
def test_beverage_10():
    assert new_beverage("CaramelMacciato",[12,24,36]) == "Valid beverage"

def test_beverage_11():
    assert new_beverage("CaramelMacciato",[24,6,12]) == "Valid beverage"

# Numero de elementos de la lista entre 1 y 5
def test_beverage_12():
    assert new_beverage("PinkDrink",[12,24]) == "Valid beverage"
    
def test_beverage_13():
    assert new_beverage("PinkDrink",[]) == "Valid beverage"

def test_beverage_14():
    assert new_beverage("PinkDrink",[6,12,24,36,48,10]) == "Valid beverage"

# Primera variable es un string
def test_beverage_15():
    assert new_beverage("YogurtBerryFrap",[12,24,36]) == "Valid beverage"

def test_beverage_16():
    assert new_beverage([6,12,24],"YogurtBerryFrap") == "Valid beverage"

# Una sola coma separa los elementos de la lista de tamaños
def test_beverage_17():
    assert new_beverage("DragonDrink",[12,24,36]) == "Valid beverage"

# El siguiente caso de prueba evita que se procesen las pruebas
# def test_beverage_18():
#     assert new_beverage("DragonDrink",[12,,24,36]) == "Valid beverage"