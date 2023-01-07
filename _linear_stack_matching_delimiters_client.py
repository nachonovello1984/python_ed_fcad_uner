from data_structures import ArrayStack

def coinciden_simbolos(expresion : str) -> bool:
    izquierda = "({["
    derecha = ")}]"
    
    stack = ArrayStack()
    
    for c in expresion:
        if c in izquierda:
            stack.push(c)
        elif c in derecha:
            if stack.is_empty():
                return False
            if derecha.index(c) != izquierda.index(stack.pop()):
                return False
            
    return stack.is_empty()

expresion1 = "[(5+x)-(y+z)]"
expresion2 = "[(5+x)-(y+z]"
expresion3 = "[(5+x)-(y+z])"

print(f"expresión1: {expresion1} -> ", coinciden_simbolos(expresion1))
print(f"expresión1: {expresion2} -> ", coinciden_simbolos(expresion2))
print(f"expresión1: {expresion3} -> ", coinciden_simbolos(expresion3))

