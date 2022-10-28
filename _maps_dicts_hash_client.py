from data_structures import UnsortedTableMap, ChainHashMap, ProbeHashMap

print(f"{'':*^60}")
print(f"{' UnsortedTableMap ':*^60}")
print(f"{'':*^60}")

map = UnsortedTableMap()

lorem_ipsum = """lorem ipsum dolor sit amet, consectetur adipiscing elit. duis nec ligula dapibus, malesuada nibh in, porta massa. donec eget sodales tellus, non venenatis nisi. praesent at lacinia ligula. praesent tristique, arcu nec suscipit facilisis, justo tellus laoreet ex, sit amet pellentesque sem nisi nec ex. phasellus congue dapibus erat, vitae vulputate nulla accumsan eget. praesent mi nisi, pellentesque ut ante sed, rutrum malesuada mauris. aenean sed lacinia orci. sed et diam quis libero pulvinar facilisis. etiam varius eu velit id mattis. sed consequat ex erat. quisque tincidunt malesuada mauris sed faucibus."""
for texto in lorem_ipsum.split():
    palabra = ''.join(c for c in texto if c.isalpha())
    if palabra:
        map[palabra] = 1 + map.get(palabra, 0)
        
print(map)

max_palabra = ''
max_cantidad = 0
for (p, c) in map.items():
    if c > max_cantidad:
        max_palabra = p
        max_cantidad = c
        
print('La palabra más frecuente es:', max_palabra)
print('El número de ocurrencias es:', max_cantidad)

# print(f"{' ChainHashMap ':*^60}")
# print(f"{'':*^60}")

# lorem_chars = "".join([letra for letra in lorem_ipsum if letra.isalpha()])

# chain_hashmap = ChainHashMap()
# for i in lorem_chars:
#     chain_hashmap[i] = 1 + chain_hashmap.get(i, 0)
        
# print(chain_hashmap)

# print("Letra que más se repite:", max(chain_hashmap.items(), key= lambda x : x[1]))

# print(f"{'':*^60}")
# print(f"{' ProbeHashMap ':*^60}")
# print(f"{'':*^60}")

# lorem_chars = "".join([letra for letra in lorem_ipsum if letra.isalpha()])

# probe_hashmap = ProbeHashMap()
# for i in lorem_chars:
#     probe_hashmap[i] = 1 + probe_hashmap.get(i, 0)
        
# print(probe_hashmap)

# print("Letra que más se repite:", max(probe_hashmap.items(), key= lambda x : x[1]))