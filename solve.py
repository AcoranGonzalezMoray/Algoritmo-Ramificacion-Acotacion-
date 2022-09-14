from node import *

def solve_branch_and_bound_DFS(capacity, items, record_visiting_order = False):
    """"
    :param capacity: capacidad de la mochila
    :param items: items de la mochila
    :param record_visiting_order: activa/desactiva el registro de nodos visitados
    :return: Por ahora sólo devuelve la lista de nodos visitados
    """
    #Recorrido DFS

    # Utilizamos la lista 'alive' como nuestra pila de nodos vivos
    # (pendientes de visitar) para programar nuestro recorrido DFS.

    alive = []
    
    # Utilizamos la lista Visiting_Order como el registro de nodos
    # visitados 

    visiting_order = []

    # 1) Creamos el nodo raiz  el único valor necesario en el nodo es el
    #    indice al primer elemento de la lista (index = 0).
    # ...
    node = Node(0, [], 0, 0)
    # Lo añadimos a la lista de nodos vivos (alive)
    # ...
    alive.append(node)
    # Mientras haya nodos en la lista de nodos vivos
    # ...
    while alive:
        # Avanzamos al siguiente nodo de nuestro recorrido DFS (hacemos un pop
        # de la lista) y lo registramos en nuestro recorrido DFS.

        current = alive.pop()
        if record_visiting_order:
            visiting_order.append(current.index)

        # Si no hemos llegado al final del árbol
        #    1) Ramificamos (branch) por la derecha (append)
        #    2) Ramificamos (branch) por la izquierda (append)
        # ...
        if(current.index<len(items)):
            RightNode = Node(current.index+1, [], 0, 0)
            alive.append(RightNode)

            LeftNode = Node(current.index+1, [], 0, 0)
            alive.append(LeftNode)
    return 0, [], visiting_order