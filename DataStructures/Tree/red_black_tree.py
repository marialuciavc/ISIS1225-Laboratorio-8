class rbt_nodo:
    def __init__(self, llave, valor, color= ROJO):
        self.llave     = llave
        self.valor     = valor
        self.color     = color
        self.izquierda = None
        self.derecha   = None
        
def _es_rojo(nodo):
        if nodo is None:
            return False
        return nodo.color == ROJO

def _rotar_izquierda(nodo):
    x              = nodo.derecha
    nodo.derecha   = x.izquierda
    x.izquierda    = nodo
    x.color        = nodo.color
    nodo.color     = ROJO
    return x

def _rotar_derecha(nodo):
    x           = nodo.izquierda
    nodo.izquierda = x.derecha
    x.derecha      = nodo
    x.color        = nodo.color
    nodo.color     = ROJO
    return x


    
    
        
    
        
    