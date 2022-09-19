from data_structures import LinkedStack, LinkedQueue, LinkedList
from data_structures.linear.util import h1, h2

def linked_stack_client() -> None:
    """Pone a prueba LinkedStack y todos sus métodos"""
    h1("LinkedStack")
    stack = LinkedStack()
        
    for i in range(1, 11):
        stack.push(i)
        print("stack.push({}): {} - len(stack): {}".format(i, stack, len(stack)))
        
    h2("LinkedStack completo")
    print(stack)
    
    h2("Vaciado de LinkedStack")
    while not stack.is_empty():
        print("stack.top(): {} - len(stack): {}".format(stack.top(), len(stack)))
        stack.pop()
        
def linked_queue_client() -> None:
    """Pone a prueba LinkedQueue y todos sus métodos"""
    h1("LinkedQueue")
    
    queue = LinkedQueue()
        
    for i in range(1, 11):
        queue.enqueue(i)
        print("queue.enqueue({}): {} - len(queue): {}".format(i, queue, len(queue)))
        
    h2("LinkedQueue completo")
    print(queue)

    h2("Vaciado de LinkedQueue")
    
    while not queue.is_empty():
        print("queue.first(): {} - len(queue): {}".format(queue.first(), len(queue)))
        queue.dequeue()  

def linked_list_client() -> None:
    """Pone a prueba LinkedList y todos sus métodos"""
    h1("LinkedList")
    lista = LinkedList()
        
    for i in range(1, 11):
        lista.append(i)
        print("lista.append({}): {} - len(lista): {}".format(i, i, len(lista)))
        
    h2("LinkedList completo")
    print(lista)
    
    h2("Recorrido de LinkedList")
    i = 0
    for item in lista:
        print(f"lista[{i}]: {item}")
        i += 1

    del lista[len(lista)-1]
    del lista[len(lista)-1]
    lista[len(lista)//2] = 33
        
    print(lista)
    
    del lista[0]
    
    print(lista)

if __name__ == "__main__" and __package__ is None:
    linked_stack_client()
    linked_queue_client()
    linked_list_client()