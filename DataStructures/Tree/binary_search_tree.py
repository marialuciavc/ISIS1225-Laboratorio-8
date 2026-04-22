from DataStructures.Tree import bst_node as node
from DataStructures.List import array_list as sl



def new_map():
    arbol = {'root': None}
    return arbol



def default_compare(llave, nodo_bst):
    llave_nodo = node.get_key(nodo_bst)
    if llave < llave_nodo:
        return -1
    elif llave == llave_nodo:
        return 0
    else:
        return 1



def size_tree(raiz):
    if raiz is None:
        return 0
    return 1 + size_tree(raiz['left']) + size_tree(raiz['right'])


def size(my_bst):
    return size_tree(my_bst['root'])



def insert_node(raiz, llave, valor):
    if raiz is None:
        return node.new_node(llave, valor)

    comparacion = default_compare(llave, raiz)

    if comparacion < 0:
        raiz['left'] = insert_node(raiz['left'], llave, valor)
    elif comparacion > 0:
        raiz['right'] = insert_node(raiz['right'], llave, valor)
    else:
        raiz['value'] = valor

    raiz['size'] = 1 + size_tree(raiz['left']) + size_tree(raiz['right'])
    return raiz


def put(my_bst, key, value):
    my_bst['root'] = insert_node(my_bst['root'], key, value)
    return my_bst



def get_node(raiz, llave):
    if raiz is None:
        return None

    comparacion = default_compare(llave, raiz)

    if comparacion < 0:
        return get_node(raiz['left'], llave)
    elif comparacion > 0:
        return get_node(raiz['right'], llave)
    else:
        return raiz


def get(my_bst, key):
    encontrado = get_node(my_bst['root'], key)
    if encontrado is not None:
        return node.get_value(encontrado)
    return None


def is_empty(my_bst):
    return my_bst['root'] is None



def contains(my_bst, llave):
    encontrado = get(my_bst, llave)
    return encontrado is not None

def key_set_tree(raiz, lista_llaves):
    if raiz is None:
        return lista_llaves
    key_set_tree(raiz['left'], lista_llaves)
    sl.add_last(lista_llaves, node.get_key(raiz))
    key_set_tree(raiz['right'], lista_llaves)
    return lista_llaves


def key_set(my_bst):
    
    lista_llaves = sl.new_list()
    key_set_tree(my_bst['root'], lista_llaves)
    return lista_llaves



def value_set_tree(raiz, lista_valores):
    if raiz is None:
        return lista_valores
    value_set_tree(raiz['left'], lista_valores)
    sl.add_last(lista_valores, node.get_value(raiz))
    value_set_tree(raiz['right'], lista_valores)
    return lista_valores


def value_set(my_bst):
    lista_valores = sl.new_list()
    value_set_tree(my_bst['root'], lista_valores)
    return lista_valores

def get_min_node(raiz):
    
    if raiz['left'] is None:
        return raiz
    return get_min_node(raiz['left'])


def get_min(my_bst):
    if is_empty(my_bst):
        return None
    nodo_minimo = get_min_node(my_bst['root'])
    return node.get_key(nodo_minimo)


def get_max_node(raiz):
    
    if raiz['right'] is None:
        return raiz
    return get_max_node(raiz['right'])


def get_max(my_bst):
    
    if is_empty(my_bst):
        return None
    nodo_maximo = get_max_node(my_bst['root'])
    return node.get_key(nodo_maximo)

def delete_min_tree(raiz):
    if raiz['left'] is None:
        return raiz['right']
    raiz['left'] = delete_min_tree(raiz['left'])
    raiz['size'] = 1 + size_tree(raiz['left']) + size_tree(raiz['right'])
    return raiz


def delete_min(my_bst):
    if is_empty(my_bst):
        return my_bst
    my_bst['root'] = delete_min_tree(my_bst['root'])
    return my_bst



def delete_max_tree(raiz):
    if raiz['right'] is None:
        return raiz['left']
    raiz['right'] = delete_max_tree(raiz['right'])
    raiz['size'] = 1 + size_tree(raiz['left']) + size_tree(raiz['right'])
    return raiz


def delete_max(my_bst):
    if is_empty(my_bst):
        return my_bst
    my_bst['root'] = delete_max_tree(my_bst['root'])
    return my_bst


def height_tree(raiz):

    if raiz is None:
        return 0
    altura_izquierda = height_tree(raiz['left'])
    altura_derecha = height_tree(raiz['right'])
    return 1 + max(altura_izquierda, altura_derecha)


def height(my_bst):

    return height_tree(my_bst['root'])

def keys_range(raiz, llave_inicio, llave_fin, lista_llaves):
    if raiz is None:
        return lista_llaves
    
    comparacion_inicio = default_compare(llave_inicio, raiz)
    comparacion_fin = default_compare(llave_fin, raiz)

    if comparacion_inicio < 0:
        keys_range(raiz['left'], llave_inicio, llave_fin, lista_llaves)
    if comparacion_inicio <= 0 and comparacion_fin >= 0:
        sl.add_last(lista_llaves, node.get_key(raiz))
    if comparacion_fin > 0:
        keys_range(raiz['right'], llave_inicio, llave_fin, lista_llaves)
    
    return lista_llaves


def keys(my_bst, llave_inicio, llave_fin):
    lista_llaves = sl.new_list()
    keys_range(my_bst['root'], llave_inicio, llave_fin, lista_llaves)
    return lista_llaves



def values_range(raiz, llave_inicio, llave_fin, lista_valores):
    if raiz is None:
        return lista_valores
    
    comparacion_inicio = default_compare(llave_inicio, raiz)
    comparacion_fin = default_compare(llave_fin, raiz)

    if comparacion_inicio < 0:
        values_range(raiz['left'], llave_inicio, llave_fin, lista_valores)
    if comparacion_inicio <= 0 and comparacion_fin >= 0:
        sl.add_last(lista_valores, node.get_value(raiz))
    if comparacion_fin > 0:
        values_range(raiz['right'], llave_inicio, llave_fin, lista_valores)
    
    return lista_valores


def values(my_bst, llave_inicio, llave_fin):
    lista_valores = sl.new_list()
    values_range(my_bst['root'], llave_inicio, llave_fin, lista_valores)
    return lista_valores 