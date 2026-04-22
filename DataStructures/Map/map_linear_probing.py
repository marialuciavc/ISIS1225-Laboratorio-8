import random
from DataStructures.List import array_list as al
from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me


def new_map(num_elements, load_factor, prime=109345121):

    capacity = mf.next_prime(int(num_elements / load_factor))

    scale = random.randint(1, prime - 1)
    shift = random.randint(0, prime - 1)

    table = al.new_list()

    for i in range(capacity):
        entry = me.new_map_entry(None, None)
        al.add_last(table, entry)

    map = {
        "prime": prime,
        "capacity": capacity,
        "scale": scale,
        "shift": shift,
        "table": table,
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0
    }

    return map

def default_compare(key, element):
    # Saco la llave de la entrada que me pasaron
    entry_key = me.get_key(element)
    
    # Comparo la llave buscada con la llave de la entrada
    if key == entry_key:
        return 0       # son iguales
    elif key > entry_key:
        return 1       # key es mayor
    else:
        return -1      # key es menor
def is_available(table, pos):
    # Obtengo la entrada en esa posición (índice desde 0)
    entry = al.get_element(table, pos)
    # Libre si nunca fue usado (None) o si fue borrado ("__EMPTY__")
    if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
        return True
    return False

def find_slot(my_map, key, hash_value):
    first_avail = None
    found = False
    ocupied = False

    while not found:
        if is_available(my_map["table"], hash_value):
            if first_avail is None:
                first_avail = hash_value
            # Si la llave es None, la llave definitivamente no está en la tabla
            entry = al.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
                found = True
        elif default_compare(key, al.get_element(my_map["table"], hash_value)) == 0:
            # Encontré la llave, ya estaba en la tabla
            first_avail = hash_value
            found = True
            ocupied = True
        # Paso al siguiente slot en círculo
        hash_value = (hash_value + 1) % my_map["capacity"]

    return ocupied, first_avail

def put(my_map, key, value):
    # Calculo el hash de la llave
    hash_val = mf.hash_value(my_map, key)

    # Busco el slot donde va esta llave
    ocupied, slot = find_slot(my_map, key, hash_val)

    if ocupied:
        # La llave ya existe, solo actualizo el valor
        entry = al.get_element(my_map["table"], slot)
        me.set_value(entry, value)
    else:
        # La llave es nueva, creo la entrada y la pongo en el slot
        new_entry = me.new_map_entry(key, value)
        al.change_info(my_map["table"], slot, new_entry)

        # Sumo uno al conteo de elementos
        my_map["size"] += 1

        # Actualizo el factor de carga actual
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]

        # Si superé el límite, hago rehash
        if my_map["current_factor"] > my_map["limit_factor"]:
            my_map = rehash(my_map)

    return my_map

def rehash(my_map):
    # Guardo la tabla vieja antes de reemplazarla
    old_table = my_map["table"]
    old_capacity = my_map["capacity"]

    # Creo una tabla nueva con el doble de capacidad (siguiente primo)
    new_capacity = mf.next_prime(old_capacity * 2)

    # Reinicio la tabla con slots vacíos
    new_table = al.new_list()
    for i in range(new_capacity):
        entry = me.new_map_entry(None, None)
        al.add_last(new_table, entry)

    # Actualizo los datos del mapa con la nueva tabla
    my_map["table"] = new_table
    my_map["capacity"] = new_capacity
    my_map["size"] = 0
    my_map["current_factor"] = 0

    # Vuelvo a insertar cada elemento de la tabla vieja en la nueva
    for i in range(old_capacity):
        entry = al.get_element(old_table, i)
        key = me.get_key(entry)
        # Solo inserto si el slot tenía un elemento real (no vacío ni borrado)
        if key is not None and key != "__EMPTY__":
            value = me.get_value(entry)
            my_map = put(my_map, key, value)

    return my_map

def contains(my_map, key):

  
    hash_value = mf.hash_value(my_map, key)


    found, slot = find_slot(my_map, key, hash_value)

    if found:
        return True

    return False

def remove(my_map, key):
    hash_val = mf.hash_value(my_map, key)
    found, slot = find_slot(my_map, key, hash_val)

    if found:
        # Marco el slot como borrado usando las funciones de map_entry
        empty_entry = me.new_map_entry("__EMPTY__", "__EMPTY__")
        al.change_info(my_map["table"], slot, empty_entry)

        my_map["size"] -= 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]

    return my_map

def get(my_map, key):
    hash_val = mf.hash_value(my_map, key)
    found, slot = find_slot(my_map, key, hash_val)

    if found:
        # Obtengo la entrada y retorno su valor usando map_entry
        entry = al.get_element(my_map["table"], slot)
        return me.get_value(entry)

    return None

def size(my_map):
    return my_map["size"]


def is_empty(my_map):
    # Retorno True si no hay ningún elemento en la tabla
    return my_map["size"] == 0

def key_set(my_map):
    # Creo una lista vacía donde voy a guardar todas las llaves
    keys = al.new_list()

    # Recorro todos los slots de la tabla
    for i in range(my_map["capacity"]):
        entry = al.get_element(my_map["table"], i)
        key = me.get_key(entry)

        # Solo agrego si el slot tiene un elemento real
        if key is not None and key != "__EMPTY__":
            al.add_last(keys, key)

    return keys

def value_set(my_map):
    # Creo una lista vacía donde voy a guardar todos los valores
    values = al.new_list()

    # Recorro todos los slots de la tabla
    for i in range(my_map["capacity"]):
        entry = al.get_element(my_map["table"], i)
        key = me.get_key(entry)

        # Solo agrego si el slot tiene un elemento real
        if key is not None and key != "__EMPTY__":
            al.add_last(values, me.get_value(entry))

    return values




