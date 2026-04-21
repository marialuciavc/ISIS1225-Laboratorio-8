from DataStructures.Tree import rbt_node as node
 
RED = 0
BLACK = 1

def new_map():
    rbt = {
        "raiz": None,
        "type": "RBT"
    }
    return rbt


def compare(key1, key2):
    if key1 < key2:
        return -1
    elif key1 == key2:
        return 0
    else:
        return 1

def is_red(nd):
    if nd is None:
        return False
    return nd["color"] == RED

def size_arbol(nd):
    if nd is None:
        return 0
    return nd["size"]

def cambio_color_del_nodo(nd):
    if nd["color"] == RED:
        nd["color"] = BLACK
    else:       
        nd["color"] = RED

def cambio_de_colores(nd):
    cambio_color_del_nodo(nd)
    cambio_color_del_nodo(nd["left"])
    cambio_color_del_nodo(nd["right"])
    
def rot_left(nd):
    x = nd["right"]
    nd["right"] = x["left"]
    x["left"] = nd
    x["color"] = nd["color"]
    nd["color"] = RED
    x["size"] = nd["size"]
    nd["size"] = 1 + size_arbol(nd["left"]) + size_arbol(nd["right"])
    return x
def rot_right(nd):
    x = nd["left"]
    nd["left"] = x["right"]
    x["right"] = nd
    x["color"] = nd["color"]
    nd["color"] = RED
    x["size"] = nd["size"]
    nd["size"] = 1 + size_arbol(nd["left"]) + size_arbol(nd["right"])
    return x    
def put(my_rbt, key, value):
    my_rbt["raiz"] = insert_node(my_rbt["raiz"], key, value)
    my_rbt["raiz"]["color"] = BLACK
def insert_node(raiz, key, value):
    if raiz is None:
        return node.new_node(key, value, RED)
    cmp = compare(key, node.get_key(raiz))
    if cmp < 0:
        raiz["left"] = insert_node(raiz["left"], key, value)
    elif cmp > 0:
        raiz["right"] = insert_node(raiz["right"], key, value)
    else:
        raiz["value"] = value
    if is_red(raiz["right"]) and not is_red(raiz["left"]):
        raiz = rot_left(raiz)
    if is_red(raiz["left"]) and is_red(raiz["left"]["left"]):
        raiz = rot_right(raiz)
    if is_red(raiz["left"]) and is_red(raiz["right"]):
        cambio_de_colores(raiz)
    raiz["size"] = 1 + size_arbol(raiz["left"]) + size_arbol(raiz["right"])
    return raiz

def get_node(raiz, key):
    
    if raiz is None:
        return None
    cmp = compare(key, node.get_key(raiz))
    if cmp < 0:
        return get_node(raiz["left"], key)
    elif cmp > 0:
        return get_node(raiz["right"], key)
    else:
        return raiz
def get(my_rbt, key):
    valor = get_node(my_rbt["raiz"], key)
    if valor is not None:
        return node.get_value(valor)
    return None
def contains(my_rbt, key):
    return get(my_rbt,key) is not None

def size(my_rbt):
    return size_arbol(my_rbt["raiz"])   

def is_empty(my_rbt):
    return size(my_rbt) == 0    

def minimo(my_rbt):
    if is_empty(my_rbt):
        return None
    return node.get_key(min_node(my_rbt["raiz"]))
def min_node(raiz):
    if raiz["left"] is None:
        return raiz
    else:
        return min_node(raiz["left"])
def maximo(my_rbt):
    if is_empty(my_rbt):
        return None
    return node.get_key(max_node(my_rbt["raiz"]))
def max_node(raiz):
    if raiz["right"] is None:
        return raiz
    else:
        return max_node(raiz["right"])
def height(my_rbt):
    return height_node(my_rbt["raiz"])
def height_node(raiz):
    if raiz is None:
        return 0
    else:
        lefth=height_node(raiz["left"])
        righth=height_node(raiz["right"])
        if lefth > righth:
            return lefth + 1
        else:
            return righth + 1   
