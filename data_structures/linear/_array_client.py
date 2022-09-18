# # if para corregir imports de archivos en directorios padre en caso que el proyecto sea
# # utilizado por otros proyectos (vía GitHub por ejemplo).
# # https://stackoverflow.com/questions/6323860/sibling-package-imports
# if __name__ == "__main__" and __package__ is None:
#     from sys import path
#     from os.path import dirname as dir
#     path.append(dir(path[0]))

from stacks import ArrayStack
from queues import ArrayQueue
from util import h1, h2

def array_stack_client() -> None:
    """Pone a prueba ArrayStack y todos sus métodos"""
    h1("ArrayStack")
    stack = ArrayStack()
        
    for i in range(1, 11):
        stack.push(i)
        print("stack.push({}): {} - len(stack): {}".format(i, stack, len(stack)))
    
    h2("ArrayStack completo")
    print(stack)
    
    h2("Vaciado de ArrayStack")
    while not stack.is_empty():
        print("stack.top(): {} - len(stack): {}".format(stack.top(), len(stack)))
        stack.pop()
        
def array_queue_client() -> None:
    """Pone a prueba ArrayQueue y todos sus métodos"""
    h1("ArrayQueue")
    queue = ArrayQueue()
        
    for i in range(1, 11):
        queue.enqueue(i)
        print("queue.enqueue({}): {} - len(queue): {}".format(i, queue, len(queue)))
        
    h2("ArrayQueue completo")
    print(queue)

    h2("Vaciado de ArrayQueue")
    
    while not queue.is_empty():
        print("queue.first(): {} - len(queue): {}".format(queue.first(), len(queue)))
        queue.dequeue()
        

if __name__ == '__main__':  
    array_stack_client()
    array_queue_client()