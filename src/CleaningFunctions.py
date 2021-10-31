
def remplazo(x,y):
    '''
    La funcion recibre dos argumentos el argumento que se quiere cambiar(x) y el argumento por el que se quiere cambiar(y)
    x = valor que se tiene que cambiar
    y= valor por el que se quiere cambiar
    '''
    return x == y

def contador(x):
    '''
    Esta funcion recibe una lista que la recorre para sumar las veces que se repite un elemento de la lista. Hay un dic
    donde se guarda el elemento como key y la veces que se repite como valor
    argumentos:
    x = lista de donde sacar las repeticiones
    return el dic donde sale las veces que se repite un elemento
    '''
    cuenta={}
    for i in x:
        cuenta[i] = 0
    for i in x:
        cuenta[i] += 1
    return cuenta
