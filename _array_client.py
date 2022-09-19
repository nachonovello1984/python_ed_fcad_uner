from data_structures.linear.stacks import ArrayStack
from data_structures.linear.queues import ArrayQueue
from data_structures.linear.util import h1, h2

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