def new_list():
    newlist = {
        'elements': [],
        'size': 0,
    }
    return newlist

def get_element(my_list, index):
    
    return my_list['elements'][index]


def is_present(my_list, elment, cmp_function):
    
    size = my_list['size']
    if size > 0:
        keyexist = False 
        for keypost in range (0, size):
            info =  my_list['elements'][keypost]
            if cmp_function(elment, info) == 0:
                keyexist = True 
                break
            if keyexist:
                return keypost
    return -1

# ADD FIRST
def add_first(my_list, element):
    my_list['elements'].insert(0, element)
    my_list['size'] += 1
    return my_list

# ADD LAST
def add_last(my_list, element):
    my_list['elements'].append(element)
    my_list['size'] += 1
    return my_list

def size(my_list):
    return my_list['size']

def first_element(my_list):
    if my_list['size'] == 0:
        return None
    return my_list['elements'][0]

def is_empty(my_list):
    return my_list['size'] == 0

def last_element(my_list):
    if my_list['size'] == 0:
        return None
    return my_list['elements'][-1]

def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list['size']:
        return None

    my_list['elements'].pop(pos)
    my_list['size'] -= 1
    return my_list

def remove_first(my_list):
    if my_list['size'] == 0:
        return None

    removed = my_list['elements'].pop(0)
    my_list['size'] -= 1
    return removed

def remove_last(my_list):
    if my_list['size'] == 0:
        return None

    removed = my_list['elements'].pop()
    my_list['size'] -= 1
    return removed

def insert_element(my_list, element, pos):
    if pos < 0 or pos > my_list['size']:
        return None

    my_list['elements'].insert(pos, element)
    my_list['size'] += 1
    return my_list
# Se usó IA como apoyo para entender la lógica de implementación,
# ya que estos casos no se trabajaron en clase.
def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= my_list['size']:
        return None

    my_list['elements'][pos] = new_info
    return my_list
# Se usó IA como apoyo para entender la lógica de implementación,
# ya que estos casos no se trabajaron en clase.
def exchange(my_list, pos_1, pos_2):
    n = my_list['size']
    if pos_1 < 0 or pos_1 >= n or pos_2 < 0 or pos_2 >= n:
        return None

    my_list['elements'][pos_1], my_list['elements'][pos_2] = \
        my_list['elements'][pos_2], my_list['elements'][pos_1]
    return my_list
# Se usó IA como apoyo para entender la lógica de implementación,
# ya que estos casos no se trabajaron en clase.
def sub_list(my_list, pos_i, num_elements):
    if pos_i < 0 or pos_i >= my_list['size'] or num_elements < 0:
        return None

    new_list = {
        'elements': my_list['elements'][pos_i: pos_i + num_elements],
        'size': min(num_elements, my_list['size'] - pos_i)
    }
    return new_list

def default_sort_criteria(element_1, element_2):
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted

def selection_sort(my_list, sort_criteria):
    # Obtenemos cuántos elementos tiene la lista
    n = size(my_list)
    
    # Recorremos desde el primer elemento hasta el penúltimo
    # (el último ya queda solo en su lugar)
    for i in range(0, n - 1):
        
        # Asumimos que el elemento en posición i es el más pequeño
        min_index = i
        
        # Buscamos si hay alguno más pequeño en el resto de la lista
        for j in range(i + 1, n):
            
            # Comparamos: el elemento en j es menor que el mínimo actual?
            # sort_criteria devuelve True si el primero es menor que el segundo
            element_j = get_element(my_list, j)
            element_min = get_element(my_list, min_index)
            
            if sort_criteria(element_j, element_min):
                # Encontramos uno más pequeño, actualizamos el índice del mínimo
                min_index = j
        
        # Si el mínimo no es el que ya estaba en i, los intercambiamos
        if min_index != i:
            exchange(my_list, i, min_index)
    
    return my_list

def insertion_sort(my_list, sort_criteria): #INSERTAR EN EL LUGAR CORRECTO 
    # Obtenemos cuántos elementos tiene la lista
    n = size(my_list)
    
    # Empezamos desde el segundo elemento 
    for i in range(1, n):
        
        # Tomamos el elemento actual que queremos insertar en su lugar correcto
        current = get_element(my_list, i)
        
        # j es el índice que usamos para movernos hacia la izquierda
        j = i - 1
        
        # Mientras no lleguemos al inicio Y el elemento de la izquierda
        # sea MAYOR que el actual (es decir, están en mal orden)
        while j >= 0 and sort_criteria(current, get_element(my_list, j)):
            
            # Movemos el elemento de la izquierda una posición a la derecha
            # para hacerle espacio al elemento actual
            exchange(my_list, j, j + 1)
            
            # Seguimos moviéndonos a la izquierda
            j -= 1
    
    return my_list

def shell_sort(my_list, sort_criteria):
    # Obtenemos el tamaño de la lista
    n = size(my_list)
    
    # Calculamos el gap inicial con (3h+1)
    # empezamos en 1 y subimos hasta encontrar el mayor gap válido
    h = 1
    while h < n // 3:
        h = 3 * h + 1
    # cuando salimos, h es el gap más grande menor que n
    
    # Repetimos mientras haya gap
    while h >= 1:
        
        # Hacemos Insertion Sort con saltos de tamaño h
        for i in range(h, n):
            
            # Tomamos el elemento actual
            current = get_element(my_list, i)
            
            # j empieza h posiciones atrás
            j = i - h
            
            # Mientras no nos salgamos Y el de atrás sea mayor
            while j >= 0 and sort_criteria(current, get_element(my_list, j)):
                
                # Intercambiamos los separados por h
                exchange(my_list, j, j + h)
                
                # Retrocedemos h posiciones
                j -= h
        
        # Reducimos el gap dividiendo entre 3
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
        
    

