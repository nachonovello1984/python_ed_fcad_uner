from data_structures import ArrayHeap

heap = ArrayHeap()

heap.add(20, 20)
heap.add(30, 30)
heap.add(10, 10)
heap.add(35, 35)

print(f"{' VACIADO DE HEAP ':*^60}")

while not heap.is_empty():
    print(heap.min())
    heap.remove_min()