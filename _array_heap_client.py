from data_structures import ArrayHeap

heap = ArrayHeap()

heap.add(20, 'A')
heap.add(30, 'B')
heap.add(10, 'C')
heap.add(35, 'D')

print(heap)

print(f"{' VACIADO DE HEAP ':*^60}")

while not heap.is_empty():
    print("heap.min():", heap.min())
    heap.remove_min()