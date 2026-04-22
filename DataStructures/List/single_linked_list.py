def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }
    return newlist
def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1

    if not is_in_array:
        count = -1
    return count
def add_first(my_list, element):
    new_node = {'info': element, 'next': None}

    if my_list['size'] == 0:
        my_list['first'] = new_node
        my_list['last'] = new_node
    else:
        new_node['next'] = my_list['first']
        my_list['first'] = new_node

    my_list['size'] += 1
    return my_list


def add_last(my_list, element):
    new_node = {'info': element, 'next': None}

    if my_list['size'] == 0:
        my_list['first'] = new_node
        my_list['last'] = new_node
    else:
        my_list['last']['next'] = new_node
        my_list['last'] = new_node

    my_list['size'] += 1
    return my_list


def size(my_list):
    return my_list['size']


def first_element(my_list):
    if my_list['size'] == 0:
        return None
    return my_list['first']['info']


def is_empty(my_list):
    return my_list['size'] == 0


def last_element(my_list):
    if my_list['size'] == 0:
        return None
    return my_list['last']['info']


def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list['size']:
        return None

    if pos == 0:
        removed_node = my_list['first']
        my_list['first'] = removed_node['next']
        if my_list['size'] == 1:
            my_list['last'] = None
    else:
        prev = my_list['first']
        for _ in range(pos - 1):
            prev = prev['next']

        removed_node = prev['next']
        prev['next'] = removed_node['next']

        if removed_node == my_list['last']:
            my_list['last'] = prev

    my_list['size'] -= 1
    return my_list


def remove_first(my_list):
    if my_list['size'] == 0:
        return None

    removed_node = my_list['first']
    my_list['first'] = removed_node['next']

    if my_list['size'] == 1:
        my_list['last'] = None

    my_list['size'] -= 1
    return removed_node['info']


def remove_last(my_list):
    if my_list['size'] == 0:
        return None

    if my_list['size'] == 1:
        removed_node = my_list['last']
        my_list['first'] = None
        my_list['last'] = None
        my_list['size'] = 0
        return removed_node['info']

    prev = my_list['first']
    while prev['next'] != my_list['last']:
        prev = prev['next']

    removed_node = my_list['last']
    prev['next'] = None
    my_list['last'] = prev
    my_list['size'] -= 1
    return removed_node['info']


def insert_element(my_list, element, pos):
    if pos < 0 or pos > my_list['size']:
        return None

    new_node = {'info': element, 'next': None}

    if pos == 0:
        if my_list['size'] == 0:
            my_list['first'] = new_node
            my_list['last'] = new_node
        else:
            new_node['next'] = my_list['first']
            my_list['first'] = new_node

    elif pos == my_list['size']:
        my_list['last']['next'] = new_node
        my_list['last'] = new_node

    else:
        prev = my_list['first']
        for _ in range(pos - 1):
            prev = prev['next']
        new_node['next'] = prev['next']
        prev['next'] = new_node

    my_list['size'] += 1
    return my_list

# Se usó IA como apoyo para entender la lógica de implementación,
# ya que estos casos no se trabajaron en clase.
def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= my_list['size']:
        return None

    current = my_list['first']
    for _ in range(pos):
        current = current['next']

    current['info'] = new_info
    return my_list

# Nota:
# Para implementar esta función se consultó IA como apoyo,
# ya que el intercambio entre posiciones en una lista enlazada
# no se había visto en clase. Se usó únicamente como guía
# para entender los casos especiales y luego adaptarlo al código propio.
def exchange(my_list, pos_1, pos_2): 
    n = my_list['size']
    if pos_1 < 0 or pos_1 >= n or pos_2 < 0 or pos_2 >= n:
        return None

    if pos_1 == pos_2:
        return my_list

    if pos_1 > pos_2:
        pos_1, pos_2 = pos_2, pos_1

    current = my_list['first']
    i = 0
    node1 = None
    node2 = None

    while current is not None:
        if i == pos_1:
            node1 = current
        if i == pos_2:
            node2 = current
            break
        current = current['next']
        i += 1

    node1['info'], node2['info'] = node2['info'], node1['info']
    return my_list

# Se usó IA como apoyo para entender la lógica de implementación,
# ya que estos casos no se trabajaron en clase.
def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos >= my_list['size'] or num_elements < 0:
        return None

    new_list = {'first': None, 'last': None, 'size': 0}

    current = my_list['first']
    for _ in range(pos):
        current = current['next']

    for _ in range(num_elements):
        if current is None:
            break
        add_last(new_list, current['info'])
        current = current['next']

    return new_list

def default_sort_criteria(element_1, element_2):
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted

def selection_sort(my_list, sort_criteria):
    # Obtenemos el tamaño de la lista
    n = size(my_list)
    
    # Recorremos desde el primero hasta el penúltimo
    for i in range(0, n - 1):
        
        # Asumimos que el mínimo está en la posición i
        min_index = i
        
        # Buscamos si hay alguno más pequeño después de i
        for j in range(i + 1, n):
            
            # Obtenemos los elementos a comparar
            # (en linked list esto recorre nodos cada vez)
            element_j = get_element(my_list, j)
            element_min = get_element(my_list, min_index)
            
            # Si el de la posición j es menor, actualizamos el mínimo
            if sort_criteria(element_j, element_min):
                min_index = j
        
        # Si encontramos un mínimo diferente, intercambiamos
        if min_index != i:
            exchange(my_list, i, min_index)
    
    return my_list

def insertion_sort(my_list, sort_criteria):
    # Obtenemos el tamaño de la lista
    n = size(my_list)
    
    # Empezamos desde el segundo elemento
    for i in range(1, n):
        
        # Tomamos el elemento actual que queremos ubicar
        current = get_element(my_list, i)
        
        # j empieza justo a la izquierda del elemento actual
        j = i - 1
        
        # Mientras no lleguemos al inicio Y el de la izquierda
        # sea mayor que el actual
        while j >= 0 and sort_criteria(current, get_element(my_list, j)):
            
            # Intercambiamos para mover el elemento a la izquierda
            exchange(my_list, j, j + 1)
            
            # Seguimos moviéndonos a la izquierda
            j -= 1
    
    return my_list

def shell_sort(my_list, sort_criteria):
    n = size(my_list)
    # Calculamos el gap inicial igual que en ArrayList
    if n <= 1:
        return my_list
    h = 1
    while h < n // 3:
        h = 3 * h + 1
    
    while h >= 1:
        
        # En vez de un índice i, usamos un nodo que avanza por la lista
        # empezamos en el nodo en posición h (el primero que compararemos)
        # para llegar a él, avanzamos h veces desde el inicio
        node_i = my_list['first']
        for _ in range(h):
            node_i = node_i['next']
        # node_i apunta al nodo en posición h
        
        # Mientras node_i exista (no lleguemos al final)
        while node_i is not None:
            
            # Guardamos el valor del nodo actual
            current_val = node_i['info']
            
            # node_j empieza h posiciones atrás de node_i
            # para encontrarlo, vamos desde el inicio hasta (pos_i - h)
            # pero es más fácil: retrocedemos h pasos desde node_i
            # como no podemos ir atrás en linked list,
            # guardamos el nodo h posiciones atrás usando get_element
            # calculamos la posición actual contando desde first
            pos_i = 0
            temp = my_list['first']
            while temp is not node_i:
                temp = temp['next']
                pos_i += 1
            # pos_i ahora tiene la posición numérica de node_i
            
            j = pos_i - h
            
            # Hacemos el Insertion Sort con saltos h
            while j >= 0 and sort_criteria(current_val, get_element(my_list, j)):
                exchange(my_list, j, j + h)
                j -= h
            
            # Avanzamos node_i al siguiente nodo
            node_i = node_i['next']
        
        # Reducimos el gap
        h = h // 3
    
    return my_list


def merge(my_list, left, right, sort_criteria):
    # left y right son dos sublistas ya ordenadas
    # esta función las une en una sola lista ordenada
    
    # i recorre la lista izquierda, j recorre la derecha
    i = 0
    j = 0
    
    # k es la posición en my_list donde vamos a escribir el resultado
    k = 0
    
    # Mientras queden elementos en AMBAS listas
    while i < size(left) and j < size(right):
        
        # Comparamos el elemento actual de cada sublista
        element_left = get_element(left, i)
        element_right = get_element(right, j)
        
        # Si el de la izquierda es menor o igual, lo ponemos primero
        if sort_criteria(element_left, element_right) or element_left == element_right:
            # Lo escribimos en la posición k de la lista original
            change_info(my_list, k, element_left)
            # Avanzamos en la lista izquierda
            i += 1
        else:
            # Si el de la derecha es menor, lo ponemos primero
            change_info(my_list, k, element_right)
            # Avanzamos en la lista derecha
            j += 1
        
        # En cualquier caso avanzamos en la lista resultado
        k += 1
    
    # Si quedaron elementos en la izquierda que no se procesaron
    # los copiamos todos al resultado
    while i < size(left):
        change_info(my_list, k, get_element(left, i))
        i += 1
        k += 1
    
    # Si quedaron elementos en la derecha que no se procesaron
    # los copiamos todos al resultado
    while j < size(right):
        change_info(my_list, k, get_element(right, j))
        j += 1
        k += 1
    
    return my_list
def merge_sort(my_list, sort_criteria):
    # Obtenemos el tamaño de la lista
    n = size(my_list)
    
    # CONDICIÓN DE PARADA: si la lista tiene 0 o 1 elementos
    # ya está ordenada, no hay nada que hacer
    if n <= 1:
        return my_list
    
    # Encontramos el punto medio para dividir la lista en dos
    mid = n // 2
    
    # Creamos la sublista IZQUIERDA con los primeros 'mid' elementos
    # sub_list(lista, posición_inicio, cantidad_elementos)
    left = sub_list(my_list, 0, mid)
    
    # Creamos la sublista DERECHA con los elementos restantes
    right = sub_list(my_list, mid, n - mid)
    
    # Llamamos a merge_sort RECURSIVAMENTE sobre cada mitad
    # Aquí es donde la función se llama a sí misma con listas más pequeñas
    left = merge_sort(left, sort_criteria)
    right = merge_sort(right, sort_criteria)
    
    # Una vez que ambas mitades están ordenadas, las fusionamos
    my_list = merge(my_list, left, right, sort_criteria)
    
    return my_list

def partition(my_list, lo, hi, sort_criteria):
    # El pivote siempre es el ÚLTIMO elemento del rango actual
    pivot = get_element(my_list, hi)
    
    # i es el índice del último elemento que encontramos
    # que es MENOR que el pivote
    # empieza en lo-1 porque aún no hemos encontrado ninguno
    i = lo - 1
    
    # Recorremos desde lo hasta hi-1 (no incluimos el pivote)
    for j in range(lo, hi):
        
        # Obtenemos el elemento actual
        element_j = get_element(my_list, j)
        
        # Es el elemento actual menor o igual al pivote?
        if sort_criteria(element_j, pivot) or element_j == pivot:
            
            # Encontramos un elemento que va a la izquierda del pivote
            # avanzamos i para hacerle espacio
            i += 1
            
            # Lo intercambiamos a la zona de "menores"
            exchange(my_list, i, j)
    
    # Al final ponemos el pivote en su lugar correcto
    # justo después del último elemento menor (i+1)
    exchange(my_list, i + 1, hi)
    
    # Retornamos la posición donde quedó el pivote
    # para que quick_sort sepa dónde dividir
    return i + 1

def quick_sort(my_list, sort_criteria):
    # Llamamos a la función auxiliar con el rango completo
    # lo=0 es el inicio, size-1 es el final
    quick_sort_helper(my_list, 0, size(my_list) - 1, sort_criteria)
    return my_list


def quick_sort_helper(my_list, lo, hi, sort_criteria):
    # CONDICIÓN DE PARADA: si lo >= hi la sublista tiene
    # 0 o 1 elementos, ya está ordenada, no hay nada que hacer
    if lo < hi:
        
        # Llamamos a partition para ubicar el pivote
        # y obtener su posición final
        pivot_index = partition(my_list, lo, hi, sort_criteria)
        
        # Ordenamos recursivamente la parte IZQUIERDA
        # (todos los menores que el pivote)
        quick_sort_helper(my_list, lo, pivot_index - 1, sort_criteria)
        
        # Ordenamos recursivamente la parte DERECHA
        # (todos los mayores que el pivote)
        quick_sort_helper(my_list, pivot_index + 1, hi, sort_criteria)
        
    